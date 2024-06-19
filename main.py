def show_balance(balance):
    print("show_balance() called")  # Debugging statement
    print("********************")
    print(f"Your Balance is ${balance:.2f}")
    print("********************")

def deposit():
    print("deposit() called")  # Debugging statement
    print("********************")
    try:
        amount = float(input("Enter amount to be deposited: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return 0
    print("********************")
    
    if amount <= 0:
        print("********************")
        print("Invalid amount. Please enter a valid Amount.")
        print("********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("withdraw() called")  # Debugging statement
    print("********************")
    try:
        amount = float(input("Enter Amount to be Withdrawn: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return 0
    print("********************")
    
    if amount > balance:
        print("********************")
        print("Insufficient Balance")
        print("********************")
        return 0
    elif amount <= 0:
        print("********************")
        print("Amount must be greater than 0")
        print("********************")
        return 0
    else:
        return amount

def main():  
    print("main() called")  # Debugging statement
    balance = 0
    is_running = True
    
    while is_running:
        print("********************")
        print("Banking progress")
        print("********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("********************")
        
        choice = input("Enter your choice (1-4): ")
        print(f"User selected choice: {choice}")  # Debugging statement

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank you, have a nice day!")

if __name__ == '__main__':
    print("__name__ == '__main__'")  # Debugging statement
    main()
