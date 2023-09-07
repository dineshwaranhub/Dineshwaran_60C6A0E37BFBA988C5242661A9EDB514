class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited {amount} units. New balance: {self.__account_balance}"
        else:
            return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew {amount} units. New balance: {self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."
    
    def display_balance(self):
        return f"Account balance: {self.__account_balance}"

# Creating an instance of the BankAccount class with user input
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, "john", initial_balance)

while True:
    print("\nChoose an action:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        amount = float(input("Enter the deposit amount: "))
        print(account.deposit(amount))
    elif choice == '2':
        amount = float(input("Enter the withdrawal amount: "))
        print(account.withdraw(amount))
    elif choice == '3':
        print(account.display_balance())
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")