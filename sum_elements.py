MAX = 100  # Maximum number of elements

def get_integer_input(prompt: str) -> int:
    """Prompt the user for an integer input and handle invalid inputs."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_number_of_elements() -> int:
    """Prompt the user to enter the number of elements and validate the range."""
    while True:
        n = get_integer_input(f"Enter the number of elements (1-{MAX}): ")
        if 1 <= n <= MAX:
            return n
        print(f"Invalid input. Please provide a number between 1 and {MAX}.")

def get_integer_list(n: int) -> list[int]:
    """Prompt the user to enter a list of integers."""
    print(f"Enter {n} integers:")
    return [get_integer_input(f"Enter integer {i + 1}: ") for i in range(n)]

def calculate_sum(numbers: list[int]) -> int:
    """Calculate the sum of a list of integers."""
    return sum(numbers)

def main():
    """Main function to handle user input and calculate the sum of integers."""
    print("Welcome to the Sum Calculator!")
    
    n = get_number_of_elements()
    arr = get_integer_list(n)
    total = calculate_sum(arr)
    
    print("Sum of the numbers:", total)

if __name__ == "__main__":
    main()