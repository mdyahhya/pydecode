"""
pyDecode Test Suite

This package contains comprehensive tests for all pyDecode functionality.

Test Modules:
    - test_core.py: Tests for core decoding functions
    - test_mapping.py: Tests for exception mappings
    - test_utils.py: Tests for utility functions
    - test_cli.py: Tests for CLI functionality

Running Tests:
    # Run all tests
    pytest
    
    # Run with coverage
    pytest --cov=pydecode --cov-report=html
    
    # Run specific test file
    pytest tests/test_core.py
    
    # Run specific test
    pytest tests/test_core.py::test_decode_traceback_basic

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
TEST_DIR = Path(__file__).parent
PROJECT_ROOT = TEST_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Test configuration
TEST_TIMEOUT = 30  # seconds
SLOW_TEST_THRESHOLD = 5  # seconds

# Sample tracebacks for testing
SAMPLE_TRACEBACKS = {
    "ValueError": """Traceback (most recent call last):
  File "test.py", line 5, in <module>
    x = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'""",
    
    "ZeroDivisionError": """Traceback (most recent call last):
  File "calc.py", line 10, in divide
    result = a / b
ZeroDivisionError: division by zero""",
    
    "IndexError": """Traceback (most recent call last):
  File "list_test.py", line 3, in <module>
    item = my_list[10]
IndexError: list index out of range""",
    
    "KeyError": """Traceback (most recent call last):
  File "dict_test.py", line 4, in <module>
    value = my_dict['missing_key']
KeyError: 'missing_key'""",
    
    "NameError": """Traceback (most recent call last):
  File "script.py", line 7, in <module>
    print(undefined_variable)
NameError: name 'undefined_variable' is not defined""",
    
    "TypeError": """Traceback (most recent call last):
  File "type_test.py", line 2, in <module>
    result = "5" + 3
TypeError: can only concatenate str (not "int") to str""",
    
    "AttributeError": """Traceback (most recent call last):
  File "attr_test.py", line 3, in <module>
    x.nonexistent_method()
AttributeError: 'int' object has no attribute 'nonexistent_method'""",
    
    "SyntaxError": """  File "syntax_test.py", line 5
    if x == 5
            ^
SyntaxError: invalid syntax""",
    
    "IndentationError": """  File "indent_test.py", line 8
    return result
    ^
IndentationError: unexpected indent""",
    
    "FileNotFoundError": """Traceback (most recent call last):
  File "file_test.py", line 2, in <module>
    with open("nonexistent.txt", "r") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'""",
    
    "ImportError": """Traceback (most recent call last):
  File "import_test.py", line 1, in <module>
    from missing_module import something
ImportError: cannot import name 'something' from 'missing_module'""",
    
    "ModuleNotFoundError": """Traceback (most recent call last):
  File "module_test.py", line 1, in <module>
    import nonexistent_package
ModuleNotFoundError: No module named 'nonexistent_package'"""
}

# Helper function to create test exceptions
def create_test_exception(exception_type: type, message: str = "test error"):
    """
    Create a test exception with a realistic traceback.
    
    Args:
        exception_type: Type of exception to create
        message: Error message
        
    Returns:
        Exception instance with traceback
    """
    try:
        raise exception_type(message)
    except exception_type as e:
        return e


# Test fixtures and utilities
class TestHelper:
    """Helper class with utility methods for tests."""
    
    @staticmethod
    def assert_valid_decoded_output(result: dict):
        """
        Assert that a decoded result has all required fields.
        
        Args:
            result: Dictionary returned from decode functions
        """
        required_fields = [
            'error_type',
            'simple_explanation',
            'fix_suggestion',
            'tags',
            'category',
            'emoji',
            'success'
        ]
        
        for field in required_fields:
            assert field in result, f"Missing required field: {field}"
        
        # Check types
        assert isinstance(result['error_type'], str)
        assert isinstance(result['simple_explanation'], str)
        assert isinstance(result['fix_suggestion'], str)
        assert isinstance(result['tags'], list)
        assert isinstance(result['category'], str)
        assert isinstance(result['emoji'], str)
        assert isinstance(result['success'], bool)
        
        # Check non-empty
        assert len(result['simple_explanation']) > 10, "Explanation too short"
        assert len(result['fix_suggestion']) > 10, "Fix suggestion too short"
        assert len(result['tags']) > 0, "No tags provided"
    
    @staticmethod
    def assert_contains_branding(text: str):
        """
        Assert that text contains pyDecode branding.
        
        Args:
            text: Text to check
        """
        assert "Powered by pyDecode" in text or "Created by Yahya" in text
    
    @staticmethod
    def get_sample_traceback(error_type: str) -> str:
        """
        Get a sample traceback for testing.
        
        Args:
            error_type: Type of error (e.g., 'ValueError')
            
        Returns:
            Sample traceback string
        """
        return SAMPLE_TRACEBACKS.get(error_type, SAMPLE_TRACEBACKS['ValueError'])


# Export test utilities
__all__ = [
    'SAMPLE_TRACEBACKS',
    'create_test_exception',
    'TestHelper',
    'TEST_DIR',
    'PROJECT_ROOT',
    'TEST_TIMEOUT',
    'SLOW_TEST_THRESHOLD'
]
