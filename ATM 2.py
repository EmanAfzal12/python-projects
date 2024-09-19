import time

def atm():
    print("Please insert your card!")
    time.sleep(5)

    password = 0000
    pin = int(input("Enter your pin: "))
    balance = 10000

    if pin == password:
        while True:
            print("""
            1== Check balance
            2== Withdraw
            3== Deposit
            4== Exit""")
            try:
                option = int(input("Please Enter your Choice: "))
            except ValueError:
                print("Please enter a valid option.")
                continue

            if option == 1:
                print(f"Your balance is: {balance}")
            elif option == 2:
                withdraw_amount = int(input("Please enter withdraw amount: "))
                if withdraw_amount > balance:
                    print("Insufficient funds!")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"Your current balance is: {balance}")
            elif option == 3:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print(f"Your updated balance is: {balance}")
            elif option == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Your PIN is wrong! Please try again.")

# Run the ATM function
atm()
