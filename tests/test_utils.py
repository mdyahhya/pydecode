"""
Utility Functions Tests for PyExplain

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import pytest
from pyexplain.utils import (
    extract_error_type,
    extract_error_message,
    extract_line_number,
    extract_file_name,
    sanitize_traceback,
    is_syntax_error,
    categorize_error
)
from tests import SAMPLE_TRACEBACKS


class TestExtractErrorType:
    """Tests for extract_error_type() function."""
    
    def test_extract_valueerror(self):
        tb = SAMPLE_TRACEBACKS['ValueError']
        assert extract_error_type(tb) == 'ValueError'
    
    def test_extract_zerodivisionerror(self):
        tb = SAMPLE_TRACEBACKS['ZeroDivisionError']
        assert extract_error_type(tb) == 'ZeroDivisionError'
    
    def test_extract_empty_string(self):
        assert extract_error_type("") is None


class TestExtractErrorMessage:
    """Tests for extract_error_message() function."""
    
    def test_extract_message_valueerror(self):
        tb = SAMPLE_TRACEBACKS['ValueError']
        msg = extract_error_message(tb)
        assert msg is not None
        assert "invalid literal" in msg.lower()


class TestExtractLineNumber:
    """Tests for extract_line_number() function."""
    
    def test_extract_line_valueerror(self):
        tb = SAMPLE_TRACEBACKS['ValueError']
        line_num = extract_line_number(tb)
        assert line_num is not None
        assert isinstance(line_num, int)
        assert line_num > 0


class TestExtractFileName:
    """Tests for extract_file_name() function."""
    
    def test_extract_filename_valueerror(self):
        tb = SAMPLE_TRACEBACKS['ValueError']
        filename = extract_file_name(tb)
        assert filename is not None
        assert 'test.py' in filename


class TestSanitizeTraceback:
    """Tests for sanitize_traceback() function."""
    
    def test_sanitize_basic(self):
        tb = "  Line 1  \n  Line 2  \n"
        clean = sanitize_traceback(tb)
        assert clean == "Line 1  \n  Line 2"
    
    def test_sanitize_empty(self):
        assert sanitize_traceback("") == ""


class TestIsSyntaxError:
    """Tests for is_syntax_error() function."""
    
    def test_is_syntax_error_true(self):
        tb = SAMPLE_TRACEBACKS['SyntaxError']
        assert is_syntax_error(tb) is True
    
    def test_is_syntax_error_false(self):
        tb = SAMPLE_TRACEBACKS['ValueError']
        assert is_syntax_error(tb) is False


class TestCategorizeError:
    """Tests for categorize_error() function."""
    
    def test_categorize_syntax(self):
        assert categorize_error('SyntaxError') == 'Syntax Errors'
    
    def test_categorize_name(self):
        assert categorize_error('NameError') == 'Name Errors'
    
    def test_categorize_unknown(self):
        assert categorize_error('UnknownError') == 'Other'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
