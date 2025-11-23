"""
PyExplain Utility Functions Module

This module contains helper functions for parsing tracebacks, extracting
error information, formatting output, and handling various edge cases.

All functions are designed to work with Python 3.8+ and use only the
standard library for maximum compatibility.

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import re
import sys
import traceback
from typing import Dict, List, Optional, Tuple, Any, Union


def extract_error_type(traceback_text: str) -> Optional[str]:
    """
    Extract the error/exception type from a traceback string.
    
    Args:
        traceback_text: Raw traceback string from Python
        
    Returns:
        Exception type name (e.g., 'ValueError', 'TypeError') or None
        
    Example:
        >>> tb = "Traceback (most recent call last):\\n  File...\\nValueError: invalid literal"
        >>> extract_error_type(tb)
        'ValueError'
    """
    if not traceback_text or not isinstance(traceback_text, str):
        return None
    
    # Pattern to match exception types at the end of traceback
    patterns = [
        r'^(\w+(?:\.\w+)*Error):\s*',
        r'^(\w+(?:\.\w+)*Exception):\s*',
        r'^(\w+(?:\.\w+)*Warning):\s*',
        r'^(KeyboardInterrupt|SystemExit|GeneratorExit|StopIteration|StopAsyncIteration):\s*',
        r'^([A-Z]\w+):\s*',
    ]
    
    lines = [line.strip() for line in traceback_text.strip().split('\n') if line.strip()]
    if not lines:
        return None
    
    last_line = lines[-1]
    
    for pattern in patterns:
        match = re.search(pattern, last_line)
        if match:
            return match.group(1)
    
    first_word = last_line.split(':')[0].split()[0] if ':' in last_line or ' ' in last_line else last_line
    if first_word and first_word[0].isupper():
        return first_word
    
    return None


def extract_error_message(traceback_text: str) -> Optional[str]:
    """Extract the error message from a traceback string."""
    if not traceback_text or not isinstance(traceback_text, str):
        return None
    
    lines = [line.strip() for line in traceback_text.strip().split('\n') if line.strip()]
    if not lines:
        return None
    
    last_line = lines[-1]
    
    if ':' in last_line:
        parts = last_line.split(':', 1)
        if len(parts) == 2:
            message = parts[1].strip()
            return message if message else None
    
    return None


def extract_line_number(traceback_text: str) -> Optional[int]:
    """Extract the line number where the error occurred."""
    if not traceback_text or not isinstance(traceback_text, str):
        return None
    
    pattern = r'line\s+(\d+)'
    matches = re.findall(pattern, traceback_text)
    if matches:
        return int(matches[-1])
    
    return None


def extract_file_name(traceback_text: str) -> Optional[str]:
    """Extract the filename where the error occurred."""
    if not traceback_text or not isinstance(traceback_text, str):
        return None
    
    pattern = r'File\s+["\']([^"\']+)["\']'
    matches = re.findall(pattern, traceback_text)
    if matches:
        return matches[-1]
    
    return None


def extract_function_name(traceback_text: str) -> Optional[str]:
    """Extract the function name where the error occurred."""
    if not traceback_text or not isinstance(traceback_text, str):
        return None
    
    pattern = r'in\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*$'
    
    lines = traceback_text.split('\n')
    for line in reversed(lines):
        if 'File' in line and 'in' in line:
            match = re.search(pattern, line.strip())
            if match:
                func_name = match.group(1)
                if func_name not in ['<module>', '<lambda>', '<listcomp>', '<dictcomp>', '<setcomp>']:
                    return func_name
                elif func_name == '<module>':
                    return 'main script'
    
    return None


def format_code_snippet(code: str, line_number: int, context_lines: int = 2) -> str:
    """Format a code snippet with line numbers and highlight the error line."""
    if not code:
        return ""
    
    lines = code.split('\n')
    total_lines = len(lines)
    
    start = max(0, line_number - context_lines - 1)
    end = min(total_lines, line_number + context_lines)
    
    result = []
    for i in range(start, end):
        line_num = i + 1
        line_content = lines[i]
        
        if line_num == line_number:
            result.append(f"{line_num:3d} | {line_content}  <-- Error here")
        else:
            result.append(f"{line_num:3d} | {line_content}")
    
    return '\n'.join(result)


def sanitize_traceback(traceback_text: str) -> str:
    """Clean and sanitize a traceback string for processing."""
    if not traceback_text:
        return ""
    
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', traceback_text)
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


def is_syntax_error(traceback_text: str) -> bool:
    """Check if the error is a syntax-related error."""
    syntax_errors = ['SyntaxError', 'IndentationError', 'TabError']
    error_type = extract_error_type(traceback_text)
    return error_type in syntax_errors if error_type else False


def get_python_version() -> str:
    """Get the current Python version as a string."""
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.patch}"


def format_exception_from_object(exc: Exception) -> str:
    """Format an exception object into a traceback string."""
    return ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__))


def categorize_error(error_type: str) -> str:
    """Categorize an error into a broader category."""
    if not error_type:
        return "Unknown"
    
    categories = {
        "Syntax Errors": ["SyntaxError", "IndentationError", "TabError"],
        "Name Errors": ["NameError", "UnboundLocalError"],
        "Type Errors": ["TypeError"],
        "Value Errors": ["ValueError", "UnicodeError", "UnicodeDecodeError", 
                        "UnicodeEncodeError", "UnicodeTranslateError"],
        "Import Errors": ["ImportError", "ModuleNotFoundError"],
        "File Errors": ["FileNotFoundError", "FileExistsError", "PermissionError",
                       "IsADirectoryError", "NotADirectoryError", "OSError", "IOError"],
        "Arithmetic Errors": ["ZeroDivisionError", "OverflowError", "FloatingPointError"],
        "Index Errors": ["IndexError", "KeyError", "LookupError"],
        "Attribute Errors": ["AttributeError"],
        "Runtime Errors": ["RuntimeError", "RecursionError", "NotImplementedError"],
        "System Errors": ["SystemError", "MemoryError", "SystemExit", 
                         "KeyboardInterrupt", "GeneratorExit"],
        "Assertion Errors": ["AssertionError"],
    }
    
    for category, errors in categories.items():
        if error_type in errors:
            return category
    
    return "Other"


def add_branding_footer(text: str) -> str:
    """Add PyExplain branding footer to output text."""
    from pyexplain._version import __branding__
    
    separator = "\n" + "─" * 60 + "\n"
    return f"{text}{separator}{__branding__}\n"


def truncate_long_message(message: str, max_length: int = 200) -> str:
    """Truncate very long error messages for readability."""
    if not message or len(message) <= max_length:
        return message
    
    return message[:max_length - 3] + "..."


def parse_syntax_error_details(traceback_text: str) -> Dict[str, Any]:
    """Parse additional details from syntax errors (caret position, etc.)."""
    details = {
        "has_caret": False,
        "caret_position": None,
        "problematic_line": None
    }
    
    lines = traceback_text.split('\n')
    
    for i, line in enumerate(lines):
        if '^' in line and i > 0:
            details["has_caret"] = True
            details["caret_position"] = line.index('^')
            details["problematic_line"] = lines[i - 1].strip() if i > 0 else None
            break
    
    return details


__all__ = [
    'extract_error_type',
    'extract_error_message',
    'extract_line_number',
    'extract_file_name',
    'extract_function_name',
    'format_code_snippet',
    'sanitize_traceback',
    'is_syntax_error',
    'get_python_version',
    'format_exception_from_object',
    'categorize_error',
    'add_branding_footer',
    'truncate_long_message',
    'parse_syntax_error_details'
]
