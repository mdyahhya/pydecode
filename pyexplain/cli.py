"""
PyExplain Command-Line Interface (CLI) Module

Command-line tools for using PyExplain directly from the terminal.

Commands:
    pyexplain-run <file.py>  - Run a Python file and decode any errors
    pyexplain --version      - Show version information
    pyexplain --help         - Show help message

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, List

from pyexplain.core import safe_run, format_decoded_output
from pyexplain._version import (
    __version__,
    __title__,
    __description__,
    __author__,
    __company__,
    __branding__,
    print_version_info
)


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog='pyexplain',
        description=f'{__title__} - {__description__}',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f'''
Examples:
  pyexplain script.py              Run script.py and decode any errors
  pyexplain script.py --no-color   Run without colored output
  pyexplain script.py --technical  Show technical error details
  pyexplain --version              Show version information
  pyexplain --help                 Show this help message

{__branding__}
Created by {__author__} | {__company__}
        '''
    )
    
    parser.add_argument(
        'file',
        type=str,
        nargs='?',
        help='Python file to execute and decode errors'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show version information and exit'
    )
    
    parser.add_argument(
        '-t', '--technical',
        action='store_true',
        help='Include technical error details in output'
    )
    
    parser.add_argument(
        '--no-color',
        action='store_true',
        help='Disable colored output'
    )
    
    parser.add_argument(
        '--no-branding',
        action='store_true',
        help='Hide "Powered by PyExplain" branding footer'
    )
    
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Only show errors, suppress normal output'
    )
    
    parser.add_argument(
        '--raw',
        action='store_true',
        help='Show raw Python traceback instead of decoded version'
    )
    
    return parser


def run_file(file_path: str, technical: bool = False, color: bool = True,
            branding: bool = True, quiet: bool = False, raw: bool = False) -> int:
    """Run a Python file and decode any errors that occur."""
    path = Path(file_path)
    
    if not path.exists():
        print(f"❌ Error: File not found: {file_path}", file=sys.stderr)
        return 1
    
    if not path.is_file():
        print(f"❌ Error: Not a file: {file_path}", file=sys.stderr)
        return 1
    
    if not path.suffix == '.py':
        print(f"⚠️  Warning: {file_path} does not have .py extension", file=sys.stderr)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}", file=sys.stderr)
        return 1
    
    if not quiet:
        print(f"🚀 Running {path.name}...\n")
    
    result = safe_run(code, filename=str(path), add_branding=branding)
    
    if result.get('success'):
        if not quiet:
            print("✅ Code executed successfully!\n")
        
        output = result.get('output', '')
        if output:
            print("📤 Output:")
            print(output)
        
        if branding and not quiet:
            print("─" * 72)
            print(f"{__branding__}\n")
        
        return 0
    
    if raw:
        print(result.get('raw_traceback', 'No traceback available'))
    else:
        formatted = format_decoded_output(result, include_technical=technical, color=color)
        print(formatted)
    
    output = result.get('output', '')
    if output and not quiet:
        print("\n📤 Output before error:")
        print(output)
    
    return 1


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.version:
        print_version_info()
        return 0
    
    if not args.file:
        parser.print_help()
        return 1
    
    return run_file(
        file_path=args.file,
        technical=args.technical,
        color=not args.no_color,
        branding=not args.no_branding,
        quiet=args.quiet,
        raw=args.raw
    )


def cli_entry_point():
    """Entry point for console script (used by setuptools)."""
    sys.exit(main())


if __name__ == '__main__':
    sys.exit(main())


__all__ = [
    'main',
    'cli_entry_point',
    'run_file',
    'create_parser'
]
