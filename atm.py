import json
import os
import random
def acc_gen():
    return random.randint(81000000, 81999999)

# Get absolute path for consistent reads/writes
DATA_FILE = os.path.join(os.getcwd(), "data.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        # Create an empty JSON file if it doesn't exist
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
        print(f"Saving data to: {DATA_FILE}")


def create_account():
    print("\nCreate Account\n")
    acc_no = acc_gen()
    name = input("Enter Your Name: ")
    while True:
        try:
            deposit = int(input("Enter amount to deposit: "))
            if deposit > 0 and deposit < 1000001:
                print(f"${deposit} added to balance")
                break
            else:
                print("Enter a valid number")
        except ValueError:
            print("Enter Only Numbers")
    while True:
        try:
            pin = int(input("Set Pin: "))
            if len(str(pin)) == 4 :
                print(f"Pin Set Successfully. Pin: {pin}")
                break
            else:
                print("Pin must be 4digits")
        except ValueError:
            print("Enter Only Numbers")
    
    try:
        user_detail = {
        "name" : name,
        "bal" : deposit,
        "pin" : pin,
        "account_no" : acc_no
        }   
        data = load_data()
        data.append(user_detail)
        save_data(data)
    except Exception as e:
        print("Error Saving User detail", e)   
    print(f"\n✅ Account created successfully!")
    print(f"Your Account Number: {acc_no}")
    print(f"Your Starting Balance: ${deposit}")
    atm_menu(acc_no)
def atm_menu(account_no):
    while True:
        data = load_data()
        user = next((s for s in data if s["account_no"] == account_no), None)
        if not user:
            print("Account not found!")
            return

        print("\n-----Welcome Babs Microfinance Bank💳💳-----")
        print("-----------------------------------------------")
        print(f"-------Username: {user['name']}")
        print(f"-------Balance: ${user['bal']}")
        print(f"-------Account Number: {user['account_no']}")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Change Pin")
        print("5. Logout\n")

        choice = input("Enter a number (1–5): ")
        if choice == "1":
            deposit(user)
        elif choice == "2":
            withdraw(user)
        elif choice == "3":
            transfer(user)
        elif choice == "4":
            reset(user)
        elif choice == "5":
            login_page()
            break
        else:
            print("Option not implemented yet.")


def login():
        try:
            data = load_data()
            print("\nLOGIN\n")
            acc_no = int(input("\nEnter Your Account Number: "))
            user = next((s for s in data if s["account_no"] == acc_no), None)
            if not user:
                while True:
                    print("Account Not Found❌. Create an Account")
                    choose = input("Do you want to create an account(Yes/No): ")
                    if choose == "Yes":
                        create_account()
                        break
                    elif choose == "No":
                        print("GoodBye Gayyy😒😒")
                        break
                    else:
                        print("Enter Yes/No")
            else:
                try:
                   while True:
                        print(f"Welcome {user["name"]}")
                        pin = int(input("Enter Pin: "))
                        if user["pin"] == pin:
                            print("Access Granted")
                            atm_menu(acc_no)
                            break
                        else:
                            print("Invalid Pin❌")
                except ValueError:
                    print("Enter Number Only")

        except Exception as e:
            print("Error Fam", e)

def view_data():
    data = load_data()
    for s in data:
        print(f"Name: {s["name"]} | Balance: {s["bal"]} | Pin: {s["pin"]} | Account Number: {s["account_no"]}")
        print()
def deposit(user):
    data = load_data()
    current_user = next((s for s in data if s["account_no"] == user["account_no"]), None)
    if not current_user:
        print("User not found!")
        return

    try:
        print("\nDeposit Money\n")
        check_pin = int(input("Enter pin: "))
        if check_pin == current_user["pin"]:
            deposit_amount = int(input("Enter amount to deposit: "))
            if deposit_amount >= 1000001:
                print("Contact Bank To Deposit Large Amount")
            elif deposit_amount > 0:
                current_user["bal"] += deposit_amount
                print(f"${deposit_amount} added to balance. New Balance: {current_user['bal']}")
                save_data(data)
            else:
                print("Invalid amount.")
        else:
            print("Incorrect PIN ❌")
    except ValueError:
        print("Enter numbers only.")

def withdraw(user):
    data = load_data()
    current_user = next((s for s in data if s["account_no"] == user["account_no"]), None)
    if not current_user:
        print("User Not Found❌")
    else:
        while True:
            try:
                print("\nWithdraw Money\n")
                check_pin = int(input("Enter Pin: "))
                if current_user["pin"] == check_pin:
                    withdraw = int(input("Enter amount to withdraw: "))
                    if withdraw > 0 and withdraw <= current_user["bal"]:
                        current_user["bal"] -= withdraw
                        print(f"${withdraw} has been deducted from balance. New balance: {current_user["bal"]}")
                        save_data(data)
                        break
                    else:
                        print("Enter A Valid Amount")
                else:
                    print("Invalid Pin❌")     
            except ValueError:
                print("Enter Numbers Only ")
        
def transfer(user):
    while True:
        data = load_data()
        current_user = next((s for s in data if s["account_no"] == user["account_no"] ), None)
        if not current_user:
            print("Account Not Found")
        else:
            try:
                print("\nTransfer Money\n")
                check_pin = int(input("Enter Pin: "))
                if current_user["pin"] == check_pin:
                    acc_check = int(input("Enter Recipent Account No.: "))
                    recipent = next((s for s in data if s["account_no"] == acc_check), None)
                    if recipent["account_no"] == current_user["account_no"]:
                        print("You cant transfer to yourself ")           
                    elif recipent:
                        print(f"Recipent Name: {recipent["name"]}")
                        trans = int(input("Enter amount to transfer: "))
                        if trans > 0 and trans <= current_user["bal"]:
                            current_user["bal"] -= trans
                            recipent["bal"] += trans
                            print(f"${trans} has been transfered successfully")
                            save_data(data)
                            break
                        else:
                            print("Invalid Amount")
                    else:
                        print("Account Not Found")
                        break
                else:
                    print("Invalid Pin❌")
            except ValueError:
                print("Enter Number Only")

def reset(user):
    while True:
        data = load_data()
        print("\nChange Pin\n")
        current_user = next((s for s in data if s["account_no"] == user["account_no"]))
        try:
            check_pin = int(input("Enter Previous Pin"))
            if current_user["pin"] == check_pin:
                print("PIN RESET")
                new_pin = int(input("Enter a new pin: "))
                if current_user["pin"] == new_pin:
                    print("You cant use old pin\n")
                else:
                    len(str(new_pin)) == 4
                    current_user["pin"] =+ new_pin
                    print(f"Pin Reset Successfully. New Pin: {new_pin}")
                    save_data(data) 
                    break
            else:
                print("Invalid Pin ❌")    
        except ValueError:
            print("Enter Number Only")  

def login_page():
        while True:
            print("\nWelcome Babs Microfinance Bank💳💳")
            print("1. Create An Account")
            print("2. Login ")
            print("3. Exit")
            choose = input("Enter a number(1-2): ")
            if choose == "1":
                create_account()
                break
            elif choose == "2":
                login()
                break
            elif choose == "3":
                print("GoodBye Gayyyy😒😒")
                break
            else:
                print("Enter a number(1-2)")
login_page()
