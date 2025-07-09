bank_balance = 100000
user_pin = 1979

options = {
        1:"check bank balence",
        2:"withdraw",
        3:"deposit"
    }

attempts = 3
while attempts > 0:
    pin = int(input("Enter your pin = "))
    if pin == user_pin:
        print("Select one of the option below:")
        print("1.check your balance")
        print("2.withdraw")
        print("3.deposit")
        select_option = int(input("select an option = "))

        if select_option == 1:
            print("$",bank_balance)

        elif select_option == 2:
            money = int(input("Enter money you want = "))
            print("Here is your cash = ",money)
            bank_balance = bank_balance-money
            print("Remaining bank balance = ","$",bank_balance)

        elif select_option == 3:
            deposit = int(input("enter the money you want to deposit = "))
            bank_balance = bank_balance+deposit
            print("Your balance = ","$",bank_balance)

        else:
            print("invalid option selected!")
            input("Press enter to close...")
        break

    else:
        attempts -= 1
        print("Enter correct pin!!")
        print(f"Incorrect PIN. you have {attempts} attempt(s) left./n")

        if attempts == 0:
            print("Too many attempts access denied.")
            input("Press enter to close...")