# PyExplain 🔍

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/pyexplain.svg)](https://badge.fury.io/py/pyexplain)

**Python Errors, Explained Simply!**

PyExplain is a Python library that takes raw Python error tracebacks and converts them into simple, easy-to-understand explanations with helpful fix suggestions. Perfect for beginners learning Python, educators teaching programming, and anyone who wants clearer error messages.

## ✨ Features

- 🎯 **90+ Exception Mappings** - Covers all standard Python exceptions and warnings
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

pip install pyexplain

### Basic Usage


import pyexplain

Example 1: Decode a traceback string
traceback_text = """Traceback (most recent call last):
File "script.py", line 5, in <module>
result = 10 / 0
ZeroDivisionError: division by zero"""

result = pyexplain.decode_traceback(traceback_text)
print(result['simple_explanation'])

Output: You tried to divide by zero. This is not allowed in mathematics or Python. 🚫
print(result['fix_suggestion'])

Output: Check your code to make sure the denominator is never zero before dividing.

undefined
Example 2: Decode an exception directly
try:
x = int("not_a_number")
except Exception as e:
result = pyexplain.decode_exception(e)
print(result['simple_explanation'])
print(result['fix_suggestion'])
undefined
Example 3: Run code safely
code = """
my_list =​
print(my_list)​
"""

result = pyexplain.safe_run(code)
if not result['success']:
print(result['simple_explanation'])
print(result['fix_suggestion'])

---

## 📖 Documentation

### Main Functions

#### `decode_traceback(traceback_text, add_branding=True)`
Decode a raw Python traceback string.

**Returns:** Dictionary with error_type, simple_explanation, fix_suggestion, line_number, file_name, tags, category, emoji, branding, success

#### `decode_exception(exception, add_branding=True)`
Decode an Exception object directly.

#### `safe_run(code, filename="<string>", add_branding=True)`
Execute Python code safely with automatic error decoding.

#### `format_decoded_output(decoded, include_technical=False, color=False)`
Format decoded error into human-readable string.

---

## 🎓 Example Output



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
Powered by PyExplain ● Created by Yahya


### CLI Usage


Basic usage
pyexplain script.py

With technical details
pyexplain script.py --technical

Without colors
pyexplain script.py --no-color

Show version
pyexplain --version


---

## 🛠️ Supported Errors

PyExplain supports **90+ built-in Python exceptions**, including:

- Syntax Errors (SyntaxError, IndentationError, TabError)
- Name & Attribute Errors (NameError, AttributeError)
- Type & Value Errors (TypeError, ValueError)
- Arithmetic Errors (ZeroDivisionError, OverflowError)
- Lookup Errors (IndexError, KeyError)
- Import Errors (ImportError, ModuleNotFoundError)
- File & OS Errors (FileNotFoundError, PermissionError)
- Runtime Errors (RuntimeError, RecursionError)
- And many more...

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.


Development setup
git clone https://github.com/mdyahhya/pyexplain.git
cd pyexplain
pip install -e ".[dev]"
pytest


---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Md. Yahya Ab. Wahid Mundewadi**  
Email: yahyabuilds@gmail.com  
Company: [Dominal Group](https://dominal.in)  
GitHub: [@mdyahhya](https://github.com/mdyahhya)

---

**Powered by PyExplain ● Created by Yahya**

*Making Python errors understandable for everyone!* 🎉



