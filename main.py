"""Mini ATM - a simple console-based ATM simulation."""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3


def verify_pin():
    """Ask for the PIN. Allow up to MAX_ATTEMPTS tries."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("PIN accepted.\n")
            return True
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Wrong PIN. {remaining} attempt(s) left.")
    print("Too many wrong attempts. Card blocked.")
    return False


def read_amount(prompt):
    """Read a positive number from the user. Return None if invalid."""
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def check_balance(balance):
    print(f"Your current balance is: {balance:.2f}")


def deposit(balance):
    amount = read_amount("Enter amount to deposit: ")
    if amount is None:
        return balance
    balance += amount
    print(f"{amount:.2f} deposited successfully.")
    check_balance(balance)
    return balance


def withdraw(balance):
    amount = read_amount("Enter amount to withdraw: ")
    if amount is None:
        return balance
    if amount > balance:
        print("Insufficient balance.")
        return balance
    balance -= amount
    print(f"{amount:.2f} withdrawn successfully.")
    check_balance(balance)
    return balance


def show_menu():
    print("\n===== MINI ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    balance = 5000.0  # starting balance

    print("Welcome to Mini ATM\n")
    if not verify_pin():
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using Mini ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
