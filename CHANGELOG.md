# Changelog

All notable changes to PyExplain will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-23

### 🎉 Initial Release

#### Added
- **Core Functionality**
  - `decode_traceback()` - Decode raw Python traceback strings
  - `decode_exception()` - Decode Exception objects directly
  - `safe_run()` - Execute Python code safely with automatic error decoding
  - `format_decoded_output()` - Format decoded errors into readable strings
  - `decode()` - Smart decode function that accepts strings or exceptions

- **Exception Coverage**
  - Complete mapping for 90+ built-in Python exceptions and warnings
  - Beginner-friendly explanations for all error types
  - One-line fix suggestions for each error
  - Categorization and tagging system

- **Utility Functions**
  - `extract_error_type()` - Extract exception type from traceback
  - `extract_error_message()` - Extract error message
  - `extract_line_number()` - Extract line number
  - `extract_file_name()` - Extract filename
  - `extract_function_name()` - Extract function name
  - `sanitize_traceback()` - Clean and normalize tracebacks
  - `categorize_error()` - Categorize errors into groups

- **Command-Line Interface**
  - `pyexplain` command - Run Python files with error decoding
  - `pyexplain-run` alias command
  - Multiple CLI flags (--version, --technical, --no-color, etc.)

- **Internationalization (i18n)**
  - i18n framework stub for future translations
  - Hinglish translation stub (demonstration)

- **Documentation**
  - Comprehensive README.md
  - Complete API documentation
  - Usage examples (6+ scenarios)
  - Contributing guidelines
  - Security policy

- **Testing**
  - Complete test suite with pytest
  - Test coverage configuration
  - GitHub Actions CI/CD workflows

- **Package Features**
  - Pure Python implementation (no dependencies)
  - Python 3.8+ support
  - Cross-platform compatibility
  - MIT License
  - PyPI-ready packaging

#### Technical Details
- **Author:** Md. Yahya Ab. Wahid Mundewadi
- **Email:** yahyabuilds@gmail.com
- **Company:** Dominal Group
- **License:** MIT
- **Python Version:** 3.8+
- **Dependencies:** None

#### Branding
- All output includes: "Powered by PyExplain ● Created by Yahya"

---

## [Unreleased]

### Planned Features
- Full Hinglish translations
- Additional language support
- Web-based error decoder
- VS Code extension
- Jupyter notebook integration
- Performance optimizations

---

**Powered by PyExplain ● Created by Yahya**
