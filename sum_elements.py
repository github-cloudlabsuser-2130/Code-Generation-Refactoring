# A refactored version of the program to sum user-provided integers.

MAX = 100

def calculate_sum(arr):
    """Calculate the sum of a list of integers."""
    return sum(arr)

def get_integer_input(prompt):
    """Prompt the user for an integer input and handle invalid inputs."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """Main function to handle user input and calculate the sum of integers."""
    print("Welcome to the Sum Calculator!")
    
    # Get the number of elements
    n = get_integer_input("Enter the number of elements (1-100): ")
    if not 1 <= n <= MAX:
        print(f"Invalid input. Please provide a number between 1 and {MAX}.")
        return

    # Get the integers from the user
    arr = []
    print(f"Enter {n} integers:")
    for i in range(n):
        num = get_integer_input(f"Enter integer {i + 1}: ")
        arr.append(num)

    # Calculate and display the sum
    total = calculate_sum(arr)
    print("Sum of the numbers:", total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")