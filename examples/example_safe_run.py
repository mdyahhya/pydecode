"""
pyDecode safe_run() Advanced Examples

Demonstrates advanced usage of the safe_run() function for executing
Python code with automatic error decoding.

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import pydecode


def example_calculator():
    """Example: Simple calculator with error handling."""
    print("\n" + "="*70)
    print("EXAMPLE: Calculator with Error Handling")
    print("="*70)
    
    calculator_code = """
def divide(a, b):
    return a / b

num1 = 100
num2 = 0
result = divide(num1, num2)
print(f"Result: {result}")
"""
    
    result = pydecode.safe_run(calculator_code, filename="calculator.py")
    
    if result['success']:
        print("✅ Calculation successful!")
        print(result['output'])
    else:
        print(f"❌ {result['error_type']} occurred!")
        print(f"\n💡 {result['simple_explanation']}")
        print(f"\n🔧 {result['fix_suggestion']}")


def example_data_processing():
    """Example: Data processing with type errors."""
    print("\n" + "="*70)
    print("EXAMPLE: Data Processing with Type Errors")
    print("="*70)
    
    data_code = """
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": "twenty"}  # Wrong type!
]

total_age = 0
for user in users:
    print(f"Processing {user['name']}...")
    total_age += user['age']

average_age = total_age / len(users)
print(f"Average age: {average_age}")
"""
    
    result = pydecode.safe_run(data_code, filename="data_processor.py")
    
    if not result['success']:
        print(f"Error: {result['error_type']}")
        print(f"\nWhat went wrong:\n{result['simple_explanation']}")
        print(f"\nHow to fix:\n{result['fix_suggestion']}")
        print(f"\nOutput before error:\n{result['output']}")


def example_file_operations():
    """Example: File operations with error handling."""
    print("\n" + "="*70)
    print("EXAMPLE: File Operations")
    print("="*70)
    
    file_code = """
print("Attempting to read file...")
with open("nonexistent_file.txt", "r") as f:
    content = f.read()
    print(content)
"""
    
    result = pydecode.safe_run(file_code, filename="file_reader.py")
    
    if not result['success']:
        formatted = pydecode.format_decoded_output(result, color=False)
        print(formatted)


def example_list_operations():
    """Example: List operations with index errors."""
    print("\n" + "="*70)
    print("EXAMPLE: List Operations")
    print("="*70)
    
    list_code = """
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

indices_to_check = [0, 2, 4, 6, 8]  # Some indices don't exist
for idx in indices_to_check:
    print(f"Accessing index {idx}: {numbers[idx]}")
"""
    
    result = pydecode.safe_run(list_code, filename="list_processor.py")
    
    if not result['success']:
        print("Error Details:")
        print(f"  Type: {result['error_type']}")
        print(f"  Line: {result['line_number']}")
        print(f"  File: {result['file_name']}")
        print(f"\n{result['emoji']} {result['simple_explanation']}")


def example_dictionary_access():
    """Example: Dictionary operations with key errors."""
    print("\n" + "="*70)
    print("EXAMPLE: Dictionary Operations")
    print("="*70)
    
    dict_code = """
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

print(f"Host: {config['host']}")
print(f"Port: {config['port']}")
print(f"Database: {config['database']}")  # This key doesn't exist
"""
    
    result = pydecode.safe_run(dict_code, filename="config_reader.py")
    
    if not result['success']:
        print(f"\n{result['error_type']} at line {result['line_number']}")
        print(f"\n💡 Beginner-friendly explanation:")
        print(f"   {result['simple_explanation']}")
        print(f"\n🔧 Quick fix:")
        print(f"   {result['fix_suggestion']}")


def example_string_operations():
    """Example: String operations with errors."""
    print("\n" + "="*70)
    print("EXAMPLE: String Operations")
    print("="*70)
    
    string_code = """
text = "Hello World"
number = 42

# Trying to add string and number
message = text + number  # This will fail
print(message)
"""
    
    result = pydecode.safe_run(string_code, filename="string_ops.py")
    
    if not result['success']:
        print("Analysis:")
        print(f"  Category: {result['category']}")
        print(f"  Tags: {', '.join(result['tags'])}")
        print(f"\n{result['simple_explanation']}")


def example_function_errors():
    """Example: Function with undefined variables."""
    print("\n" + "="*70)
    print("EXAMPLE: Function with Undefined Variables")
    print("="*70)
    
    function_code = """
def greet(name):
    message = f"Hello, {name}!"
    print(message)
    print(f"Goodbye, {undefined_var}!")  # This will fail

greet("Alice")
"""
    
    result = pydecode.safe_run(function_code, filename="greeter.py")
    
    if not result['success']:
        print(f"Function: {result.get('function_name', 'N/A')}")
        print(f"Line: {result['line_number']}")
        print(f"\n{result['simple_explanation']}")
        print(f"\n{result['branding']}")


def example_successful_execution():
    """Example: Successful code execution."""
    print("\n" + "="*70)
    print("EXAMPLE: Successful Execution")
    print("="*70)
    
    success_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci sequence:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

result = fibonacci(8)
"""
    
    result = pydecode.safe_run(success_code, filename="fibonacci.py")
    
    if result['success']:
        print("✅ Code executed without errors!")
        print(f"\n📤 Output:\n{result['output']}")
        print(f"\n{result['branding']}")
    else:
        print("Unexpected error occurred")


def main():
    """Run all safe_run examples."""
    print("\n" + "🚀"*35)
    print("   pyDecode safe_run() - Advanced Examples")
    print("🚀"*35)
    
    examples = [
        example_calculator,
        example_data_processing,
        example_file_operations,
        example_list_operations,
        example_dictionary_access,
        example_string_operations,
        example_function_errors,
        example_successful_execution
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\n⚠️  Example execution failed: {e}")
    
    print("\n" + "="*70)
    print("All safe_run examples completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
