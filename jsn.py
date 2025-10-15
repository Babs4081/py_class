import json

# def details():
#     name = input("Enter Your Name: ")
#     age = int(input("Enter Age: "))
#     skill = input("Enter Your Skill: ")

#     user_details = {
#         "name" : name,
#         "age" : age,
#         "skill" : skill
#     }
#     with open("user_profile.json", "w") as f:
#         json.dump(user_details, f, indent=4)
#         print("\nProfile Saved Successflly!\n")

# def load_profile():
#     try:
#         with open("user_profile.json", "r") as f:
#             dat = json.load(f)
#             print("\n📜Your Profile Data: \n")
#             print(f"Name: {dat["name"]}")
#             print(f"Age: {dat["age"]}")
#             print(f"Skill: {dat["skill"]}")
#     except FileNotFoundError:
#         print("File Not Found❌")
# while True:
#     print("1. Save Profile")
#     print("2. Load Profile")
#     print("3.Exit")
#     choose = input("Enter choice(1-3): ")
#     if choose == "1":
#         details()
#     elif choose == "2":
#         load_profile()
#     elif choose == "3":
#         print("GoodBye")
#         break

# def user_details():
#     name = input("Enter Your Name: ")
#     theme = input ("Enter theme (Black/White): ")
#     age = int(input("Enter Age: "))

#     user_detail = {
#         "name" : name,
#         "theme" : theme,
#         "age" : age
#     }
#     with open("user.json", "w") as bank:
#         json.dump(user_detail, bank, indent=4)
#         print("\nProfile Saved Successflly!\n")

# def load_profile():
#     try:
#         with open("user.json", "r") as bank:
#             data = json.load(bank)
#             print("\n📜Your Profile Data: \n")
#             print(f"Name: {data["name"]}")
#             print(f"Theme: {data["theme"]}")
#             print(f"Skill: {data["age"]}")
#     except FileNotFoundError:
#         print("File Not Found")
# while True:
#     print("1. Save Profile")
#     print("2. Load Profile")
#     print("3.Exit")
#     choose = input("Enter choice(1-3): ")
# #     if choose == "1":
# #         user_details()
# #     elif choose == "2":
# #         load_profile()
# #     elif choose == "3":
# #         print("GoodBye")
# #         break


# name = input("Enter Your Name: ")
# theme = input ("Enter theme (Black/White): ")
# age = int(input("Enter Age: "))
# try:
#     with open("sav.json", "r") as save:
#         data = json.load(save)
# except FileNotFoundError:
#     data = []

# new_account = {
#     "name" : name,
#     "theme" : theme,
#     "age" : age
# }
# data.append(new_account)
# with open("sav.json", "w") as save:
#     json.dump(data, save, indent=4)
# print(data)
