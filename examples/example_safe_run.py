"""
PyExplain safe_run() Advanced Examples

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
License: MIT
"""

import pyexplain


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
    
    result = pyexplain.safe_run(calculator_code, filename="calculator.py")
    
    if result['success']:
        print("✅ Calculation successful!")
        print(result['output'])
    else:
        print(f"❌ {result['error_type']} occurred!")
        print(f"\n💡 {result['simple_explanation']}")
        print(f"\n🔧 {result['fix_suggestion']}")


def example_list_operations():
    """Example: List operations with index errors."""
    print("\n" + "="*70)
    print("EXAMPLE: List Operations")
    print("="*70)
    
    list_code = """
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

indices_to_check = [0, 2, 4, 6, 8]
for idx in indices_to_check:
    print(f"Accessing index {idx}: {numbers[idx]}")
"""
    
    result = pyexplain.safe_run(list_code, filename="list_processor.py")
    
    if not result['success']:
        print("Error Details:")
        print(f"  Type: {result['error_type']}")
        print(f"  Line: {result['line_number']}")
        print(f"\n{result['emoji']} {result['simple_explanation']}")


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
for i in range(8):
    print(f"F({i}) = {fibonacci(i)}")
"""
    
    result = pyexplain.safe_run(success_code, filename="fibonacci.py")
    
    if result['success']:
        print("✅ Code executed without errors!")
        print(f"\n📤 Output:\n{result['output']}")
        print(f"\n{result['branding']}")


def main():
    """Run all safe_run examples."""
    print("\n" + "🚀"*35)
    print("   PyExplain safe_run() - Advanced Examples")
    print("🚀"*35)
    
    examples = [
        example_calculator,
        example_list_operations,
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
