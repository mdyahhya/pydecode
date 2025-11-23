"""
PyExplain - Convert Python Errors into Beginner-Friendly Explanations

PyExplain is a Python library that takes raw Python error tracebacks and
converts them into simple, easy-to-understand explanations with helpful
fix suggestions. Perfect for beginners learning Python!

Quick Start:
    >>> import pyexplain
    >>> 
    >>> # Decode a traceback string
    >>> traceback_text = "ValueError: invalid literal for int()"
    >>> result = pyexplain.decode_traceback(traceback_text)
    >>> print(result['simple_explanation'])
    >>> 
    >>> # Decode an exception directly
    >>> try:
    ...     x = int("abc")
    ... except Exception as e:
    ...     result = pyexplain.decode_exception(e)
    ...     print(result['fix_suggestion'])
    >>> 
    >>> # Run code safely and auto-decode errors
    >>> code = "print(10 / 0)"
    >>> result = pyexplain.safe_run(code)
    >>> if not result['success']:
    ...     print(result['simple_explanation'])

Main Functions:
    - decode_traceback(traceback_text: str) -> dict
    - decode_exception(exception: Exception) -> dict
    - safe_run(code: str, filename: str = "<string>") -> dict
    - format_decoded_output(decoded: dict) -> str

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
Website: https://dominal.in
License: MIT

GitHub: https://github.com/mdyahhya/pyexplain
PyPI: https://pypi.org/project/pyexplain/
"""

# Version information
from pyexplain._version import (
    __version__,
    __version_info__,
    __title__,
    __description__,
    __url__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
    __company__,
    __company_url__,
    __branding__,
    __python_requires__,
    __python_versions__,
    __status__,
    __release_date__,
    __api_version__,
    get_version,
    get_version_info,
    print_version_info
)

# Core functionality
from pyexplain.core import (
    decode_traceback,
    decode_exception,
    safe_run,
    format_decoded_output
)

# Utilities (advanced users)
from pyexplain.utils import (
    extract_error_type,
    extract_error_message,
    extract_line_number,
    extract_file_name,
    extract_function_name,
    sanitize_traceback,
    categorize_error
)

# Mapping access (for customization)
from pyexplain.mapping import (
    EXCEPTION_MAPPINGS,
    get_exception_mapping
)

# Internationalization
from pyexplain.i18n import (
    translate,
    supported_languages
)


# Define public API
__all__ = [
    # Version info
    '__version__',
    '__version_info__',
    '__title__',
    '__description__',
    '__url__',
    '__author__',
    '__author_email__',
    '__license__',
    '__copyright__',
    '__company__',
    '__company_url__',
    '__branding__',
    '__python_requires__',
    '__python_versions__',
    '__status__',
    '__release_date__',
    '__api_version__',
    'get_version',
    'get_version_info',
    'print_version_info',
    
    # Core functions (PRIMARY API)
    'decode_traceback',
    'decode_exception',
    'safe_run',
    'format_decoded_output',
    
    # Utilities (SECONDARY API)
    'extract_error_type',
    'extract_error_message',
    'extract_line_number',
    'extract_file_name',
    'extract_function_name',
    'sanitize_traceback',
    'categorize_error',
    
    # Mapping (ADVANCED API)
    'EXCEPTION_MAPPINGS',
    'get_exception_mapping',
    
    # i18n (EXPERIMENTAL API)
    'translate',
    'supported_languages'
]


# Package-level convenience function
def decode(input_data, **kwargs):
    """
    Smart decode function that accepts either a traceback string or Exception object.
    
    Args:
        input_data: Either a traceback string or an Exception object
        **kwargs: Additional arguments passed to decode functions
        
    Returns:
        Decoded error dictionary
        
    Example:
        >>> result = pyexplain.decode("ValueError: bad value")
        >>> result = pyexplain.decode(ValueError("bad value"))
    """
    if isinstance(input_data, BaseException):
        return decode_exception(input_data, **kwargs)
    elif isinstance(input_data, str):
        return decode_traceback(input_data, **kwargs)
    else:
        raise TypeError(
            f"decode() expects a string or Exception, got {type(input_data).__name__}"
        )


# Add decode to public API
__all__.append('decode')
