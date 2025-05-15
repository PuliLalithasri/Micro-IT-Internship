import time
import os

# Color class for terminal output
class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animated welcome
def welcome_animation():
    clear_screen()
    msg = f"{Colors.HEADER}{Colors.BOLD}🧮 Welcome to the Creative Python Calculator! 🧠{Colors.END}"
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print("\n")

# Calculator operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y
def power(x, y): return x ** y
def mod(x, y): return x % y

# Display menu
def display_menu():
    print(f"""{Colors.CYAN}
Choose an operation:
  1. ➕ Add
  2. ➖ Subtract
  3. ✖️ Multiply
  4. ➗ Divide
  5. 🔼 Power
  6. 🌀 Modulus
  7. ❌ Exit
{Colors.END}""")

# Get input number
def get_number(prompt):
    while True:
        try:
            return float(input(f"{Colors.YELLOW}{prompt}{Colors.END}"))
        except ValueError:
            print(f"{Colors.RED}⚠️ Invalid number. Please try again.{Colors.END}")

# Main calculator loop
def calculator():
    while True:
        display_menu()
        choice = input(f"{Colors.BOLD}Enter choice (1-7): {Colors.END}")
        if choice == '7':
            print(f"{Colors.GREEN}Thank you for using the calculator. Goodbye! 👋{Colors.END}")
            break

        if choice not in ['1','2','3','4','5','6']:
            print(f"{Colors.RED}⚠️ Invalid choice. Please try again.{Colors.END}")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == '1':
                result = add(num1, num2)
                symbol = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                symbol = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                symbol = '×'
            elif choice == '4':
                result = divide(num1, num2)
                symbol = '÷'
            elif choice == '5':
                result = power(num1, num2)
                symbol = '^'
            elif choice == '6':
                result = mod(num1, num2)
                symbol = '%'

            print(f"{Colors.GREEN}{Colors.BOLD}✅ Result: {num1} {symbol} {num2} = {result}{Colors.END}\n")
        except Exception as e:
            print(f"{Colors.RED}❌ Error: {str(e)}{Colors.END}\n")

        time.sleep(1)

# Run the calculator
if __name__ == "__main__":
    welcome_animation()
    calculator()
