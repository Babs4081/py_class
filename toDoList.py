#                         # TO LIST LOOP               
# tasks = []
# def myMenu():
#     print("\n==== TO-DO LIST MENU =====")
#     print("1. View Tasks")
#     print("2. Add Task")
#     print("3. Remove Task")
#     print("4. Exit")
# while True:
#     myMenu()
#     choice = (input("Enter your choice(1-4): "))
#     if choice == "1":
#         if not tasks:
#             print("\nNo Tasks Found!")
#         else:
#             print("\nYour Tasks:")
#             for i, task in enumerate(tasks, start=1):
#                 print(f"{i}. {tasks}")
#     elif choice == "2":
#         task = input("Enter a new task: ")
#         tasks.append(task)
#         print(f"Task '{task} added!")
#     elif choice == "3":
#         if not tasks:
#             print("\nNo tasks to remove!")
#         else:
#             for i, task in enumerate(tasks, start=1):
#                 print(f"{i}. {task}")
#             try:
#                 task_num = int(input("Enter the task number to remove:"))
#                 removed = tasks.pop(task_num -1)
#                 print(f"Task '{removed} removed!")
#             except (ValueError, IndexError):
#                 print("Invalid task number!")
#     elif choice == "4":
#         print("Goodbye! ✔")  
#         break  
#     else:
#         print("Invalid choice, please enter 1-4. ")
                                #SCORE RECORD LOOP           
# scoreRecord = []
# def myRec():
#     print("\nScore Record System")
#     print("1. View Score Record")
#     print("2. Add New Score")
#     print("3. Remove Score")
#     print("4. Exit")
# while True:
#     myRec()
#     choice = input("Enter Choice(1-4):")
#     if choice == "1":
#         if not scoreRecord :
#             print("\nNo Score Record Found!")
#         else :
#             print("\nYour Score Record")
#             for i , score in enumerate(scoreRecord, start=1):
#                 print(f"{i}. {score}")
#     elif choice == "2":
#         scoreAdd = int(input("Enter Score:"))
#         scoreRecord.append(scoreAdd)
#         print(f"Score {scoreAdd} added ✔")
#     elif choice == "3":
#         if not scoreRecord :
#             print("\nNo Score To Remove ❗")
#         else :
#             for i, score in enumerate(scoreRecord, start=1):
#                 print(f"{i}. {score}")
#             try :
#                 score_num = int(input("Enter Score number to remove:"))
#                 removed = scoreRecord.pop(score_num -1)
#                 print(f"Score {removed} has been removed ✔")
#             except (ValueError, IndexError):
#                 print("Invalid Score Number")
#     elif choice == "4":
#         print("Goodbye😊")
#         break
#     else:
#         print("Invalid Score,Enter 1-4: ")
        
                                        #BOOK LIBRARY SYSTEM 
# bookRec = []
# def mybookRec():
#     print("\nLibray Books")
#     print("1. View Library Books")
#     print("2. Add Library Book")
#     print("3. Remove Library Book")
#     print("4. Exit Library")
# while True :
#     mybookRec()
#     choose = int((input("Enter Number(1-4):")))
#     if choose == "1":
#         if not bookRec :
#             print("\nNo Book Found❗")
#         else :
#             print("\nLibrary Books")
#             for i, books in enumerate(bookRec, start=1):
#                 print(f"{i}. {books}")
#     elif choose == "2":
#         bookAdd = input("Enter Book Name:")
#         bookRec.append(bookAdd)
#         print(f"New Book {bookAdd} Added ✔")
#     elif choose == "3":
#         if not bookRec :
#             print("No Library Book Found")
#         else:
#             print("\nLibrary Books")
#             for i, books in enumerate(bookRec, start=1):
#                 print(f"{i}. {books}")
#             try:
#                 bookDel = int(input("Enter Book Number To Delete"))
#                 delete = bookRec.pop(bookDel)
#                 print(f"Book {delete} has been removed✔")
#             except(IndexError,ValueError):
#                 print("Invalid Number")
#     elif choose == "4":
#         print("Goodbye Gay 😊😊😒😒")
#         break
#     else :
#         print("Invalid Number Please Enter 1-4")
                                    #Music Playlist Manager
# favSong = []
# def musicPlaylist():
#     print("\nMusic Playlist Menu")
#     print("1. View Music Playlist")
#     print("2. Add Music")
#     print("3. Remove Song ")
#     print("4. Exit Playlist")
# while True:
#     musicPlaylist()
#     choose = (input("Enter Number(1-4):"))
#     if choose == "1":
#         if not favSong :
#             print("\nNo Song Found In Music Playlist❗")
#         else :
#             print("\nYour Music Playlist")
#             for i, songs in enumerate(favSong, start=1):
#                 print(f"{i}. {songs}")
#     elif choose == "2":
#         addSong = input("Enter Song:")
#         favSong.append(addSong)
#         print(f"New Song {addSong} added ✔")
#     elif choose == "3":
#         if not favSong :
#             print("\nNo Song Found In Music Playlist❗")
#         else:
#             print("\nYour Music Playlist ")
#             for i, songs in enumerate(favSong, start=1):
#                 print(f"{i}. {songs}")
#             try :
#                 delSong = int(input("Enter Music Number:"))
#                 sRemove =favSong.pop(delSong)
#                 print(f"{delSong} has been removed ✔")
#             except(IndexError, ValueError):
#                 print("Invalid number")
#     elif choose == "4":
#         print("GoodBye Gayyy😒😒")
#         break
#     else:
#         print("Invalid please enter 1-4")
# #addEprice = int(input("Enter Expense Price:"))
#         purchaseList.append(f"{addExpense} - ${addEprice}")
#         print(f"New Expense {addExpense} - ${addEprice} added ✔")

                                        # Expense Tracker
# purchaseList = []
# def expense():
#     print("\nExpense Tracker Menu")
#     print("1. View All Expenses")
#     print("2. Add Expense")
#     print("3. Remove Expense")
#     print("4. Total Expense")
#     print("5. Highest And Lowest Expense")
#     print("6. Exit ")
# while True:
#     expense()
#     choose = input("Enter A Number(1-6): ")
#     if choose == "1":
#         if not purchaseList:
#             print("No Expense Found❗")
#         else:
#             print("\nExpense List")
#             for i, (name, price) in enumerate(purchaseList, start=1):
#                 print(f"{i}. {name} - ${price}")
#     elif choose == "2":
#         addExpense = input("Enter Expense Name:")
#         try:
#             addEprice = float(input("Enter Expense Price: "))
#             if addEprice >= 0:
#                 purchaseList.append((addExpense, addEprice))
#                 print(f"New Expense {addExpense} - ${addEprice} added ✔")
#             else:
#                 print("❌ Amount Cannot Be Negative")
#         except(ValueError, IndexError):
#             print("❌ Invalid Number")
        
#     elif choose == "3":
#         if not purchaseList :
#             print("No Expense To Remove❗")
#         else:
#             print("\nExpense List")
#             for i, (name, price) in enumerate(purchaseList, start=1):
#                 print(f"{i}. {name} - ${price}")
#             try :
#                 delExpense = int(input("Enter the number of expense to delete: "))
#                 if 1 <= delExpense <= len(purchaseList):
#                     removed = purchaseList.pop(delExpense - 1) 
#                     print(f"Expense {removed[0]} - ${removed[1]} has been removed")
#                 else:
#                     print("Invalid Number")         
#             except(IndexError, ValueError):
#                 print("Invalid Number")
#     elif choose == "4":
#         if not purchaseList:
#             print("\nNo Expense Found❗")
#         else:
#             total = sum(price for _, price in purchaseList)
#             print(f"\nTotal Expenses: ${total}")
#     elif choose == "5":
#         if not purchaseList:
#             print("\nNo Expense Found❗")
#         else:
#             highest = max(purchaseList, key=lambda x: x[1])
#             lowest = min(purchaseList, key=lambda x: x[1])
#             print(f"💰 Highest Expense: {highest[0]} - ${highest[1]}")
#             print(f"💸 Lowest Expense: {lowest[0]} - ${lowest[1]}")
#     elif choose == "6":
#         print("GoodBye Gayyy😒😒") 
#         break
#     else:
#         print("Invalid Number")      


                                                # Grocery List Manager
# groceryList = []
# def myList():
#     print("\nGrocery List Manager.")
#     print("1. Add grocery items with their price and quantity.")
#     print("2. View all groceries in list.")
#     print("3. Remove groceries you no longer need.")
#     print("4. Show total cost of groceries")
#     print("5. Show the most expensive and least expensive items")
#     print("6. Exit List")
# while True:
#     myList()
#     choose = input("Enter a number(1-6): ")
#     if choose == "1":
#         addgName = (input("Enter Grocery Name: "))
#         addgQuan = int(input("Enter Quantity Of The Grocery Bought: "))
#         addgPrice = float(input("Enter Grocery Price: "))
#         groceryList.append((addgName, addgPrice, addgQuan))
#         print(f"Grocery Name: {addgName} Price: ${addgPrice } Quantity: {addgQuan} Total Cost: {addgPrice * addgQuan}")
#     elif choose == "2":
#         if not groceryList:
#             print("\nNo Grocery Found❗")
#         else:
#             print("\nYour Grocery List")
#             for i, (name, price, quantity) in enumerate(groceryList, start=1):
#                 print(f"{i}. {name} ${price} Quantity:{quantity}")
#     elif choose == "3":
#         if not groceryList :
#             print("\nNo Grocery List❗")
#         else:
#             for i, (name, price, quantity) in enumerate(groceryList, start=1):
#                 print(f"{i}. {name} ${price} Quantity:{quantity}")    
#             try: 
#                 delGrocery = int(input("Enter number of the grocery you want to remove: "))
#                 if 1<= delGrocery <= len(groceryList):             
#                     removed = groceryList.pop(delGrocery - 1)
#                     print(f"{removed[0]} ${removed[1]} Quantity:{removed[2]}")
#                 else:
#                     print("Invalid Number")
#             except(ValueError, IndexError):
#                 print("Invalid Input")
#     elif choose == "4":
#         total = sum(quantity * price for (_, quantity, price) in groceryList)
#         print(f"Total Groceries Price:{total}")
#     elif choose == "5":
#         max_item = max(groceryList, key=lambda g: g[1] * g[2])
#         min_item = min(groceryList, key=lambda g: g[1] * g[2])
#         print("\nMost Expenses Grocery")
#         print(f"{max_item[0]} Price:${max_item[1]} Quantity:{max_item[2]} Total:{max_item[1] * max_item[2]}")
 
#         print("Least Expensive Grocery")
#         print(f"{min_item[0]} Price:${min_item[1]} Quantity:{min_item[2]} Total:{min_item[1] * min_item[2]}")
#     elif choose == "6":
#         print("GoodBye Gaaayy😒😒")
#         break
#     else:
#         print("Invalid number please enter 1-4")

#                                                     # Student Grade Manager
# studentRecord = []
# def myGrademanager():
#     print("\nStudent Grade Manager.")
#     print("1. Add Student (Name, ID.)")
#     print("2. Add Grade")
#     print("3. View All Student.")
#     print("4. View Single Student Detail.")
#     print("5. Remove Student.")
#     print("6. Class Statistics.")
#     print("8. Exit")
# while True:
#     myGrademanager()
#     choose = input("Enter a number(1-8): ")
#     if choose == "1":
#         addName = input("Enter Your Name: ")
#         addId = int(input("Enter Id: "))
#         studentRec = {
#             "name": addName,
#             "id":addId,
#             "grade": {}


#         }
#         studentRecord.append(studentRec)
#         print(f"Student Name:{addName} Student Id:{addId} added ✔")
#     elif choose == "2":
#         checkId = int(input("Enter Your Id To Grade: "))
#         for stu in studentRecord:
#             if stu["id"] == checkId:
#                 subject = input("Enter Subject: ")
#                 score = float(input("Enter Score: "))

#                 if subject in stu["grade"]:
#                     stu["grade"][subject].append(score)
#                 else:
#                     stu["grade"][subject] = [score]
#                 print(f"Added {score} in {subject} for {stu["name"]}")
#             else:
#                 print("Student not Found")
#     elif choose == "3":
#         if not studentRecord:
#             print("\nNo Student Found❗")
#         else:
#             for stu in studentRecord:
#                 print(f"ID: {stu["id"]} | Name: {stu["name"]}")
#             if stu["grade"]:
#                 for subject, scores in stu["grade"].items():
#                     print(f"  {subject}: {scores}")
#             else:
#                 print("  No grades yet")
#                 print()
#     elif choose == "4":
#         if not studentRecord:
#             print("\nNo Student Found❗")
#         else:
#             checkidd = int(input("Enter Student Id: "))
#             for stu in studentRecord:
#                 if stu["id"] == checkidd:
#                     print(f"Id:{stu["id"]} | Name:{stu["name"]}")
#                     if stu["grade"]:
#                         for i, scores in stu["grade"].items():
#                             print(f"{i}: {scores}")
#                     else:
#                         print("No Grades Yet")
#                         print()
#                     break
#                 else:
#                      print("\n Student Not Found❗")
#     elif choose == "5":
#         if not studentRecord:
#             print("\nNo Student Found❗")
#         else:
#             searchId = int(input("Enter Student Id: "))
#             for stu in studentRecord:
#                 if stu["id"] == searchId:
#                     studentRecord.remove(stu)
#                     print(f"Student {stu["name"]} (ID: {stu["id"]}) has been removed")
#                     break
#                 else:
#                     print("Student not Found")    
#     elif choose == "6":
#         print("\nClass Statistics")
#         print("1. Number Of Student")
#         print("2. Subject Offered")
#         pick = input("Enter number(1-3)")
#         if pick == "1":
#             print(f"Total Number Of Student: {len(studentRecord)}")
#         elif pick == "2":
#             subjects = set()
#             for stu in studentRecord:
#                 for subject in stu["grade"].keys():
#                     subjects.add(subject)
#             if subjects:
#                 print("Subject offered in class:", ",".join(subjects))
#             else:
#                 print("No Subject Found")
                                            # Student Attendance Tracker
# attendanceRec = {}
# def mymenu():
#     print("\nStudent Attendance Tracker")
#     print("1. Add Student")
#     print ("2. Mark Attendance")
#     print("3. View Attendance")
#     print("4. Count Student Present/Absent")
#     print("5. Remove Student")
# while True:
#     mymenu()
#     choose = input("Enter a number(1-6): ")
#     if choose == "1":
#         addName = input("Enter Your Name: ")
#         addId = int(input("Enter Your Id: "))
#         attendanceRec[addId] = {"name": addName, "status": "Unavailable"}
#         print(f"Student {addName} | Id: {addId}")
#         print(attendanceRec)
#     elif choose == "2":
#         searchId = int(input("Enter Id: "))
#         if searchId in attendanceRec:
#             print(f"Student Found: {attendanceRec[addId]["name"]}")
#             attend = input("Enter Present/Absent: ")
#             attendanceRec[searchId]["status"] = attend
#             print(f"{attendanceRec[searchId]["name"]} is {attend}")
#         else:
#             print("Student Not Found")
#     elif choose == "3":
#         if not attendanceRec:
#             print("No Atttendance Record ")
#         else:
#             print("\nAtendance Record")
#             print("-----------------------------")
#             for i, list in attendanceRec.items():
#                 print(f"Name: {list["name"]} | Student Id: {i} Status: {list["status"]}")
#     elif choose == "4":
#         if not attendanceRec:
#             print("No AttendanceRecord to Count")
                                                # Digital Clock

# import tkinter as tk
# from time import strftime

# root = tk.Tk()
# root.title("Digital Clock")

# label = tk.Label(root, font=("ds-digital", 50), background="black", foreground="cyan")
# label.pack(anchor="center")

# def time():
#     current_time = strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
#     label.config(text=current_time)
#     label.after(1000, time)
# time()

# root.mainloop()
