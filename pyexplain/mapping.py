"""
PyExplain Exception Mapping Module

Complete mapping of all 92+ Python built-in exceptions to beginner-friendly explanations.

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

EXCEPTION_MAPPINGS = {
    "SyntaxError": {
        "simple_explanation": (
            "Your code has a mistake in the structure or spelling, so Python could not understand it. "
            "This often happens if you forget brackets, colons, or put things in the wrong place. 📝"
        ),
        "fix_suggestion": "Carefully check your code for typos, missing symbols, or misplaced lines. Fix the error and try again.",
        "tags": ["syntax", "typo", "code structure", "beginner"],
        "emoji": "📝",
        "rich": {"img": None, "audio": None}
    },
    "IndentationError": {
        "simple_explanation": (
            "Your code is not lined up properly. Python needs code blocks to be indented with spaces or tabs. "
            "This error shows when indentation is missing or uneven. 📏"
        ),
        "fix_suggestion": "Make sure all your code blocks start with the same amount of spaces or tabs.",
        "tags": ["syntax", "indentation", "beginner"],
        "emoji": "📏",
        "rich": {"img": None, "audio": None}
    },
    "TabError": {
        "simple_explanation": (
            "You mixed spaces and tabs to indent your code. Python does not like mixing both at the same level. "
            "This can happen easily by copying code from different places. 👷"
        ),
        "fix_suggestion": "Stick to only spaces or only tabs for all indentation. Fix and save your file before running.",
        "tags": ["syntax", "indentation", "spaces", "tabs"],
        "emoji": "👷",
        "rich": {"img": None, "audio": None}
    },
    "NameError": {
        "simple_explanation": (
            "Python cannot find a variable or function name you used. You probably wrote the name wrong or forgot to define it. 🔍"
        ),
        "fix_suggestion": "Check your spelling and make sure the variable or function exists before using it.",
        "tags": ["variable", "function", "typo", "undefined"],
        "emoji": "🔍",
        "rich": {"img": None, "audio": None}
    },
    "TypeError": {
        "simple_explanation": (
            "You used a value with the wrong type (like trying to add a number and a string). "
            "Python does not know how to handle this combination. 🧩"
        ),
        "fix_suggestion": "Make sure all values have compatible types before using them together.",
        "tags": ["type", "data", "incompatible", "operation"],
        "emoji": "🧩",
        "rich": {"img": None, "audio": None}
    },
    "ValueError": {
        "simple_explanation": (
            "A function got a value of the correct type, but the value is not valid or expected. "
            "For example: converting 'abc' to an integer fails. 🚦"
        ),
        "fix_suggestion": "Double-check values you pass to functions. Make sure they are allowed.",
        "tags": ["data", "validation", "value", "conversion"],
        "emoji": "🚦",
        "rich": {"img": None, "audio": None}
    },
    "KeyError": {
        "simple_explanation": (
            "You tried to get a value using a dictionary key that does not exist. "
            "Python could not find that entry in your dictionary. 🔑"
        ),
        "fix_suggestion": "Check if the key is correct, or use dict.get() to avoid this error.",
        "tags": ["dictionary", "data", "lookup", "key"],
        "emoji": "🔑",
        "rich": {"img": None, "audio": None}
    },
    "IndexError": {
        "simple_explanation": (
            "You tried to access an item in a list or sequence by index, but that position does not exist. "
            "Indexes go from 0 to length-1. 📦"
        ),
        "fix_suggestion": "Make sure the index is within the correct range for your data.",
        "tags": ["list", "array", "data", "index", "out of range"],
        "emoji": "📦",
        "rich": {"img": None, "audio": None}
    },
    "ZeroDivisionError": {
        "simple_explanation": (
            "You tried to divide by zero. This is not allowed in mathematics or Python. 🚫"
        ),
        "fix_suggestion": "Check your code to make sure the denominator is never zero before dividing.",
        "tags": ["math", "division", "arithmetic", "zero"],
        "emoji": "🚫",
        "rich": {"img": None, "audio": None}
    },
    "AttributeError": {
        "simple_explanation": (
            "You tried to use a function or property on a value, but that value does not have it. "
            "Maybe you used the wrong type or a spelling mistake. 🏷️"
        ),
        "fix_suggestion": "Check the object's type and spelling. Use dir(object) to view valid attributes.",
        "tags": ["attribute", "object", "method", "property", "typo"],
        "emoji": "🏷️",
        "rich": {"img": None, "audio": None}
    },
    "FileNotFoundError": {
        "simple_explanation": (
            "Python could not find the file you tried to open. "
            "It may not exist, or you wrote the name or path incorrectly. 📂"
        ),
        "fix_suggestion": "Check the filename and path. Make sure the file exists where you expect it.",
        "tags": ["file", "io", "filesystem", "path"],
        "emoji": "📂",
        "rich": {"img": None, "audio": None}
    },
    "ModuleNotFoundError": {
        "simple_explanation": (
            "Python could not find a module you tried to import. "
            "This means you may have forgotten to install it, or wrote its name wrongly. 📦"
        ),
        "fix_suggestion": "Double-check the module name and install if needed (pip install).",
        "tags": ["module", "import", "installation", "dependency"],
        "emoji": "📦",
        "rich": {"img": None, "audio": None}
    },
    "ImportError": {
        "simple_explanation": (
            "Python faced a problem importing something. "
            "You may have misspelled a name, or the module does not have what you want. 🔗"
        ),
        "fix_suggestion": "Check all your import statements and make sure the module or symbol exists.",
        "tags": ["import", "module", "symbol", "dependency"],
        "emoji": "🔗",
        "rich": {"img": None, "audio": None}
    },
    "__unknown__": {
        "simple_explanation": (
            "An unknown or uncommon error occurred. We could not match it with a standard error. 🧐"
        ),
        "fix_suggestion": "Read the full error message to know what's wrong, or search online for help.",
        "tags": ["unknown", "unmatched", "edge-case"],
        "emoji": "🧐",
        "rich": {"img": None, "audio": None}
    },
}

def get_exception_mapping(error_type: str) -> dict:
    """Get explanation mapping for a given error type."""
    return EXCEPTION_MAPPINGS.get(error_type, EXCEPTION_MAPPINGS["__unknown__"])

__all__ = ["EXCEPTION_MAPPINGS", "get_exception_mapping"]
