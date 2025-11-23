# pyDecode 🔍

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pydecode.svg)](https://badge.fury.io/py/pydecode)

**Convert Python errors into beginner-friendly explanations!**

pyDecode is a Python library that takes raw Python error tracebacks and converts them into simple, easy-to-understand explanations with helpful fix suggestions. Perfect for beginners learning Python, educators teaching programming, and anyone who wants clearer error messages.

## ✨ Features

- 🎯 **92+ Exception Mappings** - Covers all standard Python exceptions and warnings
- 💡 **Beginner-Friendly** - Explains errors in simple, jargon-free English (2-3 lines)
- 🔧 **Fix Suggestions** - Provides actionable solutions for each error
- 🚀 **Safe Code Execution** - Run Python code safely with automatic error decoding
- 📝 **Multiple Input Methods** - Decode traceback strings or exception objects
- 🎨 **Formatted Output** - Beautiful, readable error explanations
- 🏷️ **Categorization** - Organizes errors by type with tags
- 🌐 **Pure Python** - Works everywhere Python runs (3.8+)
- 📦 **Zero Dependencies** - Uses only Python standard library

---

## 🚀 Quick Start

### Installation
pip install pydecode


### Basic Usage

import pydecode

Example 1: Decode a traceback string
traceback_text = """Traceback (most recent call last):
File "script.py", line 5, in <module>
result = 10 / 0
ZeroDivisionError: division by zero"""

result = pydecode.decode_traceback(traceback_text)
print(result['simple_explanation'])

Output: You tried to divide by zero. This is not allowed in mathematics or Python. 🚫
print(result['fix_suggestion'])

Output: Check your code to make sure the denominator is never zero before dividing.
undefined

Example 2: Decode an exception directly
try:
x = int("not_a_number")
except Exception as e:
result = pydecode.decode_exception(e)
print(result['simple_explanation'])
print(result['fix_suggestion'])
undefined

Example 3: Run code safely
code = """
my_list =​
print(my_list)​
"""

result = pydecode.safe_run(code)
if not result['success']:
print(result['simple_explanation'])
print(result['fix_suggestion'])

---

## 📖 Documentation

### Main Functions

#### `decode_traceback(traceback_text, add_branding=True)`
Decode a raw Python traceback string.

**Parameters:**
- `traceback_text` (str): Raw traceback string
- `add_branding` (bool): Include "Powered by pyDecode" footer

**Returns:** Dictionary with keys:
- `error_type`: Exception name (e.g., 'ValueError')
- `original_message`: Original Python error message
- `simple_explanation`: Beginner-friendly explanation
- `fix_suggestion`: How to fix the error
- `line_number`: Line where error occurred
- `file_name`: File where error occurred
- `tags`: List of classification tags
- `category`: Error category
- `emoji`: Visual indicator
- `branding`: Footer text
- `success`: Always False for errors

#### `decode_exception(exception, add_branding=True)`
Decode an Exception object directly.

**Parameters:**
- `exception` (Exception): Python exception object
- `add_branding` (bool): Include branding footer

**Returns:** Same as `decode_traceback()`

#### `safe_run(code, filename="<string>", add_branding=True)`
Execute Python code safely with automatic error decoding.

**Parameters:**
- `code` (str): Python code to execute
- `filename` (str): Filename for traceback display
- `add_branding` (bool): Include branding footer

**Returns:** Success dict or error dict with decoded information

#### `format_decoded_output(decoded, include_technical=False, color=False)`
Format decoded error into human-readable string.

**Parameters:**
- `decoded` (dict): Result from decode functions
- `include_technical` (bool): Show technical details
- `color` (bool): Use ANSI color codes

**Returns:** Formatted string ready for printing

---

## 🎓 Examples

### Example Output


╔══════════════════════════════════════════════════════════════════════╗
║ 🚫 ZeroDivisionError ║
╚══════════════════════════════════════════════════════════════════════╝

💡 Simple Explanation:
You tried to divide by zero. This is not allowed in mathematics or Python. 🚫

🔧 How to Fix:
Check your code to make sure the denominator is never zero before dividing.

📍 Error Location:
File: calculator.py
Line: 15
Function: divide

────────────────────────────────────────────────────────────────────────
Powered by pyDecode ● Created by Yahya


### CLI Usage

Run Python files with automatic error decoding:


Basic usage
pydecode script.py

With technical details
pydecode script.py --technical

Without colors
pydecode script.py --no-color

Show version
pydecode --version


---

## 🛠️ Supported Errors

pyDecode supports **92+ built-in Python exceptions**, including:

### Syntax Errors
- SyntaxError, IndentationError, TabError

### Name & Attribute Errors
- NameError, UnboundLocalError, AttributeError

### Type & Value Errors
- TypeError, ValueError, UnicodeError family

### Arithmetic Errors
- ZeroDivisionError, OverflowError, FloatingPointError

### Lookup Errors
- IndexError, KeyError, LookupError

### Import Errors
- ImportError, ModuleNotFoundError

### File & OS Errors
- FileNotFoundError, PermissionError, OSError family

### Runtime Errors
- RuntimeError, RecursionError, NotImplementedError

### And many more...

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

Clone the repository
git clone https://github.com/mdyahhya/pydecode.git
cd pydecode

Install development dependencies
pip install -e ".[dev]"

Run tests
pytest

Run tests with coverage
pytest --cov=pydecode --cov-report=html

Format code
black pydecode tests

Lint code
ruff check pydecode tests


---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Md. Yahya Ab. Wahid Mundewadi**  
Email: yahyabuilds@gmail.com  
Company: [Dominal Group](https://dominal.in)  
GitHub: [@mdyahhya](https://github.com/mdyahhya)

---

## 🙏 Acknowledgments

- Inspired by the need to make Python more accessible to beginners
- Built with ❤️ for the Python community

---

## 📊 Stats

- **92+ Exception Mappings**
- **Pure Python** - No external dependencies
- **Python 3.8+** - Wide compatibility
- **100% Open Source** - MIT Licensed

---

**Powered by pyDecode ● Created by Yahya**

*Making Python errors understandable for everyone!* 🎉








