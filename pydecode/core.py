"""
pyDecode Core Module

This module contains the main decoding logic for converting Python errors
and exceptions into beginner-friendly explanations.

Core Functions:
    - decode_traceback(traceback_text: str) -> dict
    - decode_exception(exception: Exception) -> dict
    - safe_run(code: str, filename: str) -> dict

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import sys
import traceback as tb_module
from typing import Dict, Optional, Any, Union
from io import StringIO
import contextlib

from pydecode.mapping import get_exception_mapping
from pydecode.utils import (
    extract_error_type,
    extract_error_message,
    extract_line_number,
    extract_file_name,
    extract_function_name,
    sanitize_traceback,
    format_exception_from_object,
    categorize_error,
    add_branding_footer,
    truncate_long_message,
    is_syntax_error,
    parse_syntax_error_details
)
from pydecode._version import __branding__, __version__


def decode_traceback(traceback_text: str, add_branding: bool = True) -> Dict[str, Any]:
    """
    Decode a raw Python traceback string into a beginner-friendly explanation.
    
    This is the main function of pyDecode. It takes any Python error traceback
    and converts it into simple English with helpful suggestions.
    
    Args:
        traceback_text: Raw traceback string from Python (e.g., from sys.exc_info())
        add_branding: Whether to add "Powered by pyDecode" footer (default: True)
        
    Returns:
        Dictionary containing:
            - error_type: Type of exception (e.g., 'ValueError')
            - original_message: Original error message from Python
            - simple_explanation: 2-3 line beginner-friendly explanation
            - fix_suggestion: One-line fix suggestion
            - line_number: Line number where error occurred (if available)
            - file_name: Filename where error occurred (if available)
            - function_name: Function where error occurred (if available)
            - tags: List of categorization tags
            - category: Error category (e.g., 'Syntax Errors')
            - emoji: Emoji representing the error type
            - branding: Branding text (if add_branding=True)
            - success: Always False for errors
            - raw_traceback: Original traceback (sanitized)
            
    Example:
        >>> tb = '''Traceback (most recent call last):
        ...   File "test.py", line 5, in <module>
        ...     result = 10 / 0
        ... ZeroDivisionError: division by zero'''
        >>> decoded = decode_traceback(tb)
        >>> print(decoded['simple_explanation'])
        You tried to divide by zero. This is not allowed in mathematics or Python. 🚫
        >>> print(decoded['fix_suggestion'])
        Check your code to make sure the denominator is never zero before dividing.
    """
    # Input validation
    if not traceback_text or not isinstance(traceback_text, str):
        return {
            "error_type": "InvalidInput",
            "original_message": "No traceback provided",
            "simple_explanation": "pyDecode needs a valid error traceback to decode. Please provide error text.",
            "fix_suggestion": "Make sure you're passing a Python error message to decode_traceback().",
            "line_number": None,
            "file_name": None,
            "function_name": None,
            "tags": ["invalid_input"],
            "category": "Input Error",
            "emoji": "⚠️",
            "branding": __branding__ if add_branding else None,
            "success": False,
            "raw_traceback": ""
        }
    
    # Sanitize the traceback
    clean_traceback = sanitize_traceback(traceback_text)
    
    # Extract error information
    error_type = extract_error_type(clean_traceback)
    error_message = extract_error_message(clean_traceback)
    line_number = extract_line_number(clean_traceback)
    file_name = extract_file_name(clean_traceback)
    function_name = extract_function_name(clean_traceback)
    
    # Get explanation from mapping
    mapping = get_exception_mapping(error_type or "__unknown__")
    
    # Build result dictionary
    result = {
        "error_type": error_type or "UnknownError",
        "original_message": truncate_long_message(error_message or "No message provided"),
        "simple_explanation": mapping["simple_explanation"],
        "fix_suggestion": mapping["fix_suggestion"],
        "line_number": line_number,
        "file_name": file_name,
        "function_name": function_name,
        "tags": mapping["tags"],
        "category": categorize_error(error_type),
        "emoji": mapping["emoji"],
        "branding": __branding__ if add_branding else None,
        "success": False,
        "raw_traceback": clean_traceback
    }
    
    # Add syntax error specific details if applicable
    if is_syntax_error(clean_traceback):
        syntax_details = parse_syntax_error_details(clean_traceback)
        result["syntax_details"] = syntax_details
    
    return result


def decode_exception(exception: Exception, add_branding: bool = True) -> Dict[str, Any]:
    """
    Decode an Exception object directly into a beginner-friendly explanation.
    
    This function is useful when you catch an exception and want to decode it
    immediately without converting to a string first.
    
    Args:
        exception: Python Exception object (e.g., from except block)
        add_branding: Whether to add "Powered by pyDecode" footer (default: True)
        
    Returns:
        Dictionary with same structure as decode_traceback()
        
    Example:
        >>> try:
        ...     my_list = [1, 2, 3]
        ...     print(my_list[10])
        ... except Exception as e:
        ...     decoded = decode_exception(e)
        ...     print(decoded['simple_explanation'])
        You tried to access an item in a list or sequence by index, but that position does not exist...
    """
    if not isinstance(exception, BaseException):
        return {
            "error_type": "InvalidInput",
            "original_message": "Not a valid exception object",
            "simple_explanation": "pyDecode needs a valid Exception object. Please pass an exception caught in try-except.",
            "fix_suggestion": "Use decode_exception() only with exception objects from except blocks.",
            "line_number": None,
            "file_name": None,
            "function_name": None,
            "tags": ["invalid_input"],
            "category": "Input Error",
            "emoji": "⚠️",
            "branding": __branding__ if add_branding else None,
            "success": False,
            "raw_traceback": ""
        }
    
    # Format exception to traceback string
    traceback_text = format_exception_from_object(exception)
    
    # Use decode_traceback to process
    return decode_traceback(traceback_text, add_branding=add_branding)


def safe_run(code: str, filename: str = "<string>", globals_dict: Optional[dict] = None,
             locals_dict: Optional[dict] = None, add_branding: bool = True) -> Dict[str, Any]:
    """
    Safely execute Python code and automatically decode any errors that occur.
    
    This function runs Python code in a controlled environment and catches any
    exceptions, automatically decoding them into beginner-friendly explanations.
    
    Args:
        code: Python code string to execute
        filename: Filename to use in traceback (default: "<string>")
        globals_dict: Global namespace for execution (default: clean namespace)
        locals_dict: Local namespace for execution (default: same as globals)
        add_branding: Whether to add "Powered by pyDecode" footer (default: True)
        
    Returns:
        Dictionary containing:
            If successful:
                - success: True
                - output: Captured stdout output
                - result: Return value (if any)
                - branding: Branding text (if add_branding=True)
                
            If error occurred:
                - success: False
                - All fields from decode_traceback()
                - output: Any output before the error
                
    Example:
        >>> code = '''
        ... x = 10
        ... y = 0
        ... result = x / y
        ... print(result)
        ... '''
        >>> result = safe_run(code)
        >>> if not result['success']:
        ...     print(result['simple_explanation'])
        ...     print(result['fix_suggestion'])
        You tried to divide by zero. This is not allowed in mathematics or Python. 🚫
        Check your code to make sure the denominator is never zero before dividing.
    """
    # Input validation
    if not code or not isinstance(code, str):
        return {
            "success": False,
            "error_type": "InvalidInput",
            "original_message": "No code provided",
            "simple_explanation": "pyDecode needs valid Python code to run. Please provide a code string.",
            "fix_suggestion": "Pass a string containing Python code to safe_run().",
            "line_number": None,
            "file_name": None,
            "function_name": None,
            "tags": ["invalid_input"],
            "category": "Input Error",
            "emoji": "⚠️",
            "branding": __branding__ if add_branding else None,
            "output": "",
            "raw_traceback": ""
        }
    
    # Prepare namespaces
    if globals_dict is None:
        globals_dict = {"__name__": "__main__", "__file__": filename}
    if locals_dict is None:
        locals_dict = globals_dict
    
    # Capture stdout
    stdout_capture = StringIO()
    
    try:
        with contextlib.redirect_stdout(stdout_capture):
            # Compile the code
            compiled_code = compile(code, filename, 'exec')
            
            # Execute the code
            exec(compiled_code, globals_dict, locals_dict)
        
        # Success case
        captured_output = stdout_capture.getvalue()
        return {
            "success": True,
            "output": captured_output,
            "result": locals_dict.get('result', None),  # If code sets 'result' variable
            "branding": __branding__ if add_branding else None,
            "message": "Code executed successfully! ✅"
        }
        
    except Exception as e:
        # Error case - decode the exception
        captured_output = stdout_capture.getvalue()
        
        # Get the full traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_text = ''.join(tb_module.format_exception(exc_type, exc_value, exc_traceback))
        
        # Decode the error
        decoded = decode_traceback(traceback_text, add_branding=add_branding)
        
        # Add output to result
        decoded["output"] = captured_output
        
        return decoded


def format_decoded_output(decoded: Dict[str, Any], include_technical: bool = False,
                         color: bool = False) -> str:
    """
    Format a decoded error dictionary into a human-readable string.
    
    Args:
        decoded: Dictionary returned from decode_traceback() or decode_exception()
        include_technical: Whether to include technical details (default: False)
        color: Whether to include ANSI color codes (default: False)
        
    Returns:
        Formatted string ready for printing
        
    Example:
        >>> decoded = decode_traceback(some_error)
        >>> print(format_decoded_output(decoded))
        
        ╔══════════════════════════════════════════════════════╗
        ║  ZeroDivisionError                                   ║
        ╚══════════════════════════════════════════════════════╝
        
        💡 Simple Explanation:
        You tried to divide by zero...
    """
    if not decoded or not isinstance(decoded, dict):
        return "Invalid decoded data"
    
    # ANSI color codes (if enabled)
    RED = '\033[91m' if color else ''
    GREEN = '\033[92m' if color else ''
    YELLOW = '\033[93m' if color else ''
    BLUE = '\033[94m' if color else ''
    MAGENTA = '\033[95m' if color else ''
    CYAN = '\033[96m' if color else ''
    RESET = '\033[0m' if color else ''
    BOLD = '\033[1m' if color else ''
    
    # Build output
    lines = []
    
    # Header
    error_type = decoded.get('error_type', 'Error')
    emoji = decoded.get('emoji', '⚠️')
    
    lines.append("")
    lines.append("╔" + "═" * 70 + "╗")
    lines.append(f"║  {BOLD}{RED}{emoji} {error_type}{RESET}" + " " * (68 - len(error_type) - 2) + "║")
    lines.append("╚" + "═" * 70 + "╝")
    lines.append("")
    
    # Simple Explanation
    lines.append(f"{BOLD}{CYAN}💡 Simple Explanation:{RESET}")
    lines.append(decoded.get('simple_explanation', 'No explanation available'))
    lines.append("")
    
    # Fix Suggestion
    lines.append(f"{BOLD}{GREEN}🔧 How to Fix:{RESET}")
    lines.append(decoded.get('fix_suggestion', 'No suggestion available'))
    lines.append("")
    
    # Location information (if available)
    if decoded.get('file_name') or decoded.get('line_number'):
        lines.append(f"{BOLD}{YELLOW}📍 Error Location:{RESET}")
        if decoded.get('file_name'):
            lines.append(f"   File: {decoded['file_name']}")
        if decoded.get('line_number'):
            lines.append(f"   Line: {decoded['line_number']}")
        if decoded.get('function_name'):
            lines.append(f"   Function: {decoded['function_name']}")
        lines.append("")
    
    # Technical details (optional)
    if include_technical:
        lines.append(f"{BOLD}{MAGENTA}🔍 Technical Details:{RESET}")
        lines.append(f"   Category: {decoded.get('category', 'Unknown')}")
        lines.append(f"   Original Message: {decoded.get('original_message', 'N/A')}")
        lines.append(f"   Tags: {', '.join(decoded.get('tags', []))}")
        lines.append("")
    
    # Branding footer
    if decoded.get('branding'):
        lines.append("─" * 72)
        lines.append(f"{BOLD}{BLUE}{decoded['branding']}{RESET}")
        lines.append("")
    
    return '\n'.join(lines)


# Public API
__all__ = [
    'decode_traceback',
    'decode_exception',
    'safe_run',
    'format_decoded_output'
]
