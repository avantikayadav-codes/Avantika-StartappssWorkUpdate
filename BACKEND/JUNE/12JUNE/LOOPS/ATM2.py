balance = 10000   
pin = 1234
entered_pin = int(input("Enter your PIN: "))
if entered_pin == pin:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print(f"Your balance is: {balance}")
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited {amount}. New balance: {balance}")
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print(f"Withdrew {amount}. New balance: {balance}")
        elif choice == 4:
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice!")
else:
    print("Incorrect PIN!")