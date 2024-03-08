import argparse
import os
import re
from ._wheel_repair import WheelRepair
from ._version import __version__
from . import _dll_utils


def _subdir_suffix(s: str) -> str:
    """Helper for argument parser for validating a subdirectory suffix."""
    if not s or any(c in r'<>:"/\|?*' or ord(c) < 32 for c in s) or \
            any(s.endswith(x) for x in ('.dist-info', '.data', ' ', '.')):
        raise argparse.ArgumentTypeError(f'Invalid subdirectory suffix {s!r}')
    return s


def _dll_names(s: str) -> str:
    """Helper for argument parser for validating a list of DLL names"""
    for dll_name in filter(None, map(str.strip, s.split(os.pathsep))):
        if any(c in r'<>:"/\|?*' or ord(c) < 32 for c in dll_name):
            raise argparse.ArgumentTypeError(f'Invalid DLL name {dll_name!r}')
    return s


def _namespace_pkgs(s: str) -> str:
    for namespace_pkg in filter(None, s.split(os.pathsep)):
        if any(c in r'<>:"/\|?*' or ord(c) < 32 for c in namespace_pkg) or not re.fullmatch(r'[^.]+(\.[^.]+)*', namespace_pkg):
            raise argparse.ArgumentTypeError(f'Invalid namespace package {namespace_pkg!r}')
    return s


def main():
    """Main function"""
    # parse arguments
    parser = argparse.ArgumentParser(description=f'Delvewheel {__version__}: Create self-contained wheels for Windows')
    subparsers = parser.add_subparsers(dest='command', required=True)
    parser_show_description = 'Search a wheel for external DLL dependencies'
    parser_show = subparsers.add_parser('show', help=parser_show_description, description=parser_show_description)
    parser_repair_description = 'Vendor in external DLL dependencies of a wheel'
    parser_repair = subparsers.add_parser('repair', help=parser_repair_description, description=parser_repair_description)
    parser_needed_description = 'List the direct DLL dependencies of a single executable'
    parser_needed = subparsers.add_parser('needed', help=parser_needed_description, description=parser_needed_description)
    for subparser in (parser_show, parser_repair):
        subparser.add_argument('wheel', nargs='+', help='wheel(s) to show or repair')
        subparser.add_argument('--add-path', default='', metavar='PATHS', help=f'additional path(s) to search for DLLs, {os.pathsep!r}-delimited')
        subparser.add_argument('--add-dll', default='', metavar='DLLS', type=_dll_names, help=f'force inclusion of DLL name(s), {os.pathsep!r}-delimited')
        subparser.add_argument('--no-dll', default='', metavar='DLLS', type=_dll_names, help=f'force exclusion of DLL name(s), {os.pathsep!r}-delimited')
        subparser.add_argument('--ignore-in-wheel', action='store_true', help="don't search for or vendor in DLLs that are already in the wheel")
        subparser.add_argument('-v', action='count', default=0, help='verbosity')
        subparser.add_argument('--extract-dir', help=argparse.SUPPRESS)
        subparser.add_argument('--test', default='', help=argparse.SUPPRESS)  # comma-separated testing options, internal use only
    parser_repair.add_argument('-w', '--wheel-dir', dest='target', default='wheelhouse', help='directory to write repaired wheel')
    parser_repair.add_argument('--no-mangle', default='', metavar='DLLS', type=_dll_names, help=f'DLL names(s) not to mangle, {os.pathsep!r}-delimited')
    parser_repair.add_argument('--no-mangle-all', action='store_true', help="don't mangle any DLL names")
    parser_repair.add_argument('--strip', action='store_true', help='strip DLLs that contain trailing data when name-mangling')
    parser_repair.add_argument('-L', '--lib-sdir', default='.libs', type=_subdir_suffix, help='directory suffix in package to store vendored DLLs (default .libs)')
    parser_repair.add_argument('--namespace-pkg', default='', metavar='PKGS', type=_namespace_pkgs, help=f'namespace package(s), {os.pathsep!r}-delimited')
    parser_repair.add_argument('--no-diagnostic', action='store_true', help=argparse.SUPPRESS)  # don't write diagnostic information to DELVEWHEEL metadata file
    parser_repair.add_argument('--include-symbols', action='store_true', help='include .pdb symbol files with vendored DLLs')
    parser_needed.add_argument('file', help='path to a DLL or PYD file')
    parser_needed.add_argument('-v', action='count', default=0, help='verbosity')
    args = parser.parse_args()

    # handle command
    if args.command in ('show', 'repair'):
        add_paths = dict.fromkeys(os.path.abspath(path) for path in args.add_path.split(os.pathsep) if path)
        add_dlls = set(dll_name.lower() for dll_name in args.add_dll.split(os.pathsep) if dll_name)
        no_dlls = set(dll_name.lower() for dll_name in args.no_dll.split(os.pathsep) if dll_name)

        intersection = add_dlls & no_dlls
        if intersection:
            raise ValueError(f'Cannot force both inclusion and exclusion of {intersection}')

        if add_paths:
            os.environ['PATH'] = f'{os.pathsep.join(add_paths)}{os.pathsep}{os.environ["PATH"]}'

        for wheel in args.wheel:
            wr = WheelRepair(wheel, args.extract_dir, add_dlls, no_dlls, args.ignore_in_wheel, args.v, args.test.split(','))
            if args.command == 'show':
                wr.show()
            else:  # args.command == 'repair'
                no_mangles = set(dll_name.lower() for dll_name in args.no_mangle.split(os.pathsep) if dll_name)
                namespace_pkgs = set(tuple(namespace_pkg.split('.')) for namespace_pkg in args.namespace_pkg.split(os.pathsep) if namespace_pkg)
                wr.repair(args.target, no_mangles, args.no_mangle_all, args.strip, args.lib_sdir, not args.no_diagnostic and 'SOURCE_DATE_EPOCH' not in os.environ, namespace_pkgs, args.include_symbols)
    else:  # args.command == 'needed'
        for dll_name in sorted(_dll_utils.get_direct_needed(args.file, args.v), key=str.lower):
            print(dll_name)


if __name__ == '__main__':
    main()
