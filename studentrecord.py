import json
import random
def idgen():
    return random.randint(100, 150)
id
def load_data():
    try:
        with open("student.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("student.json", "w") as bank:
        json.dump(data, bank, indent=4)

def record():
    data = load_data()
    name = input("Enter Your Name: ")
    age = (input("Enter Age: "))
    clas = input("Enter Your Class: ")
    id = idgen()
   
    student_record = {
        "name" : name,
        "age" : age,
        "class" : clas,
        "id" : id
    }
    data.append(student_record)
    save_data(data)
    for s in data:
        print("Record Saved Successfully")
        print(f"Name: {s["name"]}")
        print(f"Age: {s["age"]}")
        print(f"Class: {s["class"]}")
        print(f"Student Id: {s["id"]}")
def  view_data():
    data = load_data()
    for s in data:
        print(f"Id: {s["id"]} | Name: {s["name"]} | Class: {s["class"]}")
        print()
        print(f"{type({s["id"]})}")
def search():
    data = load_data()
    check_id = int(input("Enter  Id: "))
    for s in data:
        if str(check_id) in str(s["id"]):
            print("Student Found")
            print(f"Id: {s["id"]} | Name: {s["name"]} | Class: {s["class"]}")
        else: 
            print("Student Not Found")
            


def menu():
    print("\nStudent Record Manager\n")
    print("1. Add Student Details")
    print("2. View all Student")
    print("3. Search Student By Id")
    print("4. Exit")

while True:
    menu()
    choose = input("Enter a number(1-4): ")
    if choose == "1":
        record()
    elif choose == "2":
        view_data()
    elif choose == "3":
        search()