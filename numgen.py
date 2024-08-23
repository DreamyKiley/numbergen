import random
import os

def generate_random_number(length):
    if 1 <= length <= 64:
        return ''.join(random.choices('0123456789', k=length))
    else:
        return "Input must be between 1 and 64."

def clear_prompt():
    # Clear the console screen for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Random Number Generator")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def main():
    clear_prompt()
    while True:
        try:
            print_green("How many digits (1-64) or type 'exit' to quit?")
            length_input = input().strip()  # Read input on a new line
            if length_input.lower() == 'exit':
                print_red("Exiting the program.")
                break

            length = int(length_input)
            if 1 <= length <= 64:
                print_red(generate_random_number(length))
            else:
                print("Please enter a number between 1 and 64.")
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'exit' to quit.")

if __name__ == "__main__":
    main()
