class ATM:
    def __init__(self, account_number, owner, balance=0, pin="0000"):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.transactions = []  # Keep track of deposits, withdrawals, transfers

    # PIN Authentication
    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN!")
            return False

    # Check balance
    def check_balance(self):
        print(f"{self.owner}, your current balance is: ${self.balance}")
        self.transactions.append(f"Checked balance: ${self.balance}")

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
            self.transactions.append(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.balance}")
            self.transactions.append(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")

    # Transfer money to another account
    def transfer(self, amount, recipient_atm):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_atm.balance += amount
            print(f"Transferred ${amount} to {recipient_atm.owner}. New balance: ${self.balance}")
            self.transactions.append(f"Transferred ${amount} to {recipient_atm.owner}")
            recipient_atm.transactions.append(f"Received ${amount} from {self.owner}")
        else:
            print("Transfer failed: Insufficient funds or invalid amount.")

    # View transaction history
    def view_transactions(self):
        print(f"Transaction history for {self.owner}:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print("-", t)

    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transactions.append("Changed PIN")
        else:
            print("Incorrect old PIN! PIN not changed.")


# ===== Interactive Menu =====
def main():
    # Create some ATM accounts
    atm1 = ATM("001", "Alice", 1500, "1234")
    atm2 = ATM("002", "Bob", 1000, "5678")

    atms = {"001": atm1, "002": atm2}

    print("Welcome to Advanced Python ATM!")
    account_number = input("Enter your account number: ")

    if account_number not in atms:
        print("Account not found!")
        return

    current_atm = atms[account_number]
    pin_attempt = input("Enter your PIN: ")

    if not current_atm.authenticate(pin_attempt):
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Change PIN")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            current_atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            current_atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            current_atm.withdraw(amount)
        elif choice == "4":
            recipient_acc = input("Enter recipient account number: ")
            if recipient_acc in atms and recipient_acc != account_number:
                amount = float(input("Enter amount to transfer: "))
                current_atm.transfer(amount, atms[recipient_acc])
            else:
                print("Invalid recipient account!")
        elif choice == "5":
            current_atm.view_transactions()
        elif choice == "6":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            current_atm.change_pin(old_pin, new_pin)
        elif choice == "7":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
