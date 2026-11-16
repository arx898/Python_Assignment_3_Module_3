# Name of the file that stores all employee records.
FILENAME = "employees.txt"


def add_employee(name, emp_id, salary):
    """Append one employee record to the file.

    Parameters:
        name   (str): employee name
        emp_id (str): employee ID
        salary (str or int): employee salary

    Returns:
        bool: True if the record was saved, False if saving failed.
    """
    try:
        # Mode "a" (append) adds a new line and keeps the old records.
        # The file is created automatically if it does not exist yet.
        with open(FILENAME, "a") as file:
            file.write(f"{name} | {emp_id} | {salary}\n")
        return True
    except OSError as error:
        print(f"Error: could not write to {FILENAME} ({error})")
        return False


def read_employees():
    """Read every record from the file.

    Returns:
        list: a list of lines (strings). The list is empty if the file
        does not exist or has no records.
    """
    try:
        # Mode "r" (read) opens the file for reading only.
        with open(FILENAME, "r") as file:
            # Skip blank lines and remove the trailing newline.
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        # No employee was added yet, so the file does not exist.
        return []
    except OSError as error:
        print(f"Error: could not read {FILENAME} ({error})")
        return []


def view_employees():
    """Display all employee records stored in the file."""
    records = read_employees()

    if not records:
        print("No employee records found.")
        return

    print("\n--- Employee Records ---")
    for number, record in enumerate(records, start=1):
        print(f"{number}. {record}")
    print("------------------------")


def get_non_empty_input(prompt):
    """Ask the user for text and repeat until the answer is not empty.

    Returns:
        str: the cleaned (stripped) text entered by the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Try again.")


def get_salary_input(prompt):
    """Ask the user for a salary and repeat until it is a valid number.

    Returns:
        str: the salary exactly as the user typed it (digits only checked),
        so it is saved like the sample: 25000.
    """
    while True:
        value = input(prompt).strip()
        # Accept whole numbers or decimals such as 25000 or 25000.50.
        try:
            if float(value) < 0:
                print("Salary cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Salary must be a number. Try again.")


def show_menu():
    """Print the main menu."""
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")


def main():
    """Run the menu loop until the user chooses Exit."""
    while True:
        show_menu()
        choice = input("Choose Option: ").strip()

        if choice == "1":
            name = get_non_empty_input("Enter Name: ")
            emp_id = get_non_empty_input("Enter ID: ")
            salary = get_salary_input("Enter Salary: ")

            # Only show the success message when the save really worked.
            if add_employee(name, emp_id, salary):
                print("Employee Added Successfully")
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2 or 3.")


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()
