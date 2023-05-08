# initialize account balances
account_balances = {"marzok": 5000, "ahmed": 8000, "mohamed": 3000}

# define function for withdrawing cash
def withdraw(name, amount):
    if name in account_balances:
        if amount <= account_balances[name]:
            account_balances[name] -= amount
            print("Withdrawal successful. New balance for account", name, "is", account_balances[name])
        else:
            print("Withdrawal failed. Insufficient balance.")
    else:
        print("Account not found.")

# define function for depositing cash
def deposit(name, amount):
    if name in account_balances:
        account_balances[name] += amount
        print("Deposit successful. New balance for account", name, "is", account_balances[name])
    else:
        print("Account not found.")

# define function for checking account balance
def check_balance(name):
    if name in account_balances:
        print("Account balance for", name, "is", account_balances[name])
    else:
        print("Account not found.")

# define main function for interacting with ATM
def main():
    while True:
        print("\nWelcome to the ATM!")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                name = input("Enter account holder's name: ")
                amount = int(input("Enter amount to withdraw: "))
                withdraw(name, amount)
            elif choice == '2':
                name = input("Enter account holder's name: ")
                amount = int(input("Enter amount to deposit: "))
                deposit(name, amount)
            elif choice == '3':
                name = input("Enter account holder's name: ")
                check_balance(name)
            else:
                print("Thank you for using the ATM!")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


'''

/* by using list 

# ATM Machine using List

# Initialize variables
balance = 0
transaction_history = []

# Define functions
def deposit(amount):
    global balance
    balance += amount
    transaction_history.append(f"Deposit: {amount}")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        transaction_history.append(f"Withdrawal: {amount}")
    else:
        print("Insufficient funds")

def display_balance():
    print(f"Current Balance: {balance}")

def display_transactions():
    print("Transaction History:")
    for transaction in transaction_history:
        print(transaction)

# Main program
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Display Transactions")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        deposit(amount)
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        withdraw(amount)
    elif choice == "3":
        display_balance()
    elif choice == "4":
        display_transactions()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

'''



