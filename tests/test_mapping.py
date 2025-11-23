"""
Exception Mapping Tests for PyExplain

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import pytest
from pyexplain.mapping import EXCEPTION_MAPPINGS, get_exception_mapping


class TestExceptionMappings:
    """Tests for exception mappings completeness and structure."""
    
    def test_all_mappings_have_required_fields(self):
        """Test that all mappings have required fields."""
        required_fields = ['simple_explanation', 'fix_suggestion', 'tags', 'emoji']
        
        for error_type, mapping in EXCEPTION_MAPPINGS.items():
            for field in required_fields:
                assert field in mapping, f"{error_type} missing {field}"
    
    def test_all_explanations_not_empty(self):
        """Test that all explanations are not empty."""
        for error_type, mapping in EXCEPTION_MAPPINGS.items():
            assert len(mapping['simple_explanation']) > 10
            assert len(mapping['fix_suggestion']) > 10
    
    def test_common_errors_present(self):
        """Test that common Python errors are mapped."""
        common_errors = [
            'ValueError', 'TypeError', 'KeyError', 'IndexError',
            'NameError', 'AttributeError', 'SyntaxError', 'IndentationError',
            'ZeroDivisionError'
        ]
        
        for error in common_errors:
            assert error in EXCEPTION_MAPPINGS, f"{error} not mapped"
    
    def test_fallback_exists(self):
        """Test that fallback mapping exists."""
        assert '__unknown__' in EXCEPTION_MAPPINGS


class TestGetExceptionMapping:
    """Tests for get_exception_mapping() function."""
    
    def test_get_valueerror(self):
        mapping = get_exception_mapping('ValueError')
        assert 'value' in mapping['simple_explanation'].lower()
    
    def test_get_typeerror(self):
        mapping = get_exception_mapping('TypeError')
        assert 'type' in mapping['simple_explanation'].lower()
    
    def test_get_unknown_error(self):
        mapping = get_exception_mapping('NonExistentError')
        assert mapping == EXCEPTION_MAPPINGS['__unknown__']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
