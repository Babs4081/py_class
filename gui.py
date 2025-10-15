import tkinter as tk
from tkinter import ttk
# window = tk.Tk()
# window.title("Babs Calculator")
# window.geometry("3000x2000")

# label = tk.Label(window, text="Hello, Babs", font=("Arial", 14))
# label.pack(pady=150)

# def say_hello():
#     label.config(text="You clicked the button!")

# button = tk.Button(window, text="Click Me", command=say_hello)
# button.pack(pady=20)

# window.mainloop()


# window = tk.Tk()
# window.title("Greetings")
# window.geometry("450x300")

# label = tk.Label(window, text="Enter Your Name: ", font=("Arial", 12))
# label.pack(pady=10)

# entry = tk.Entry(window, font=("Arial", 12))
# entry.pack(pady=5)

# output = tk.Label(window, text="", font=("Arial", 12), fg="blue")
# output.pack(pady=10)

# def greet():
#     name = entry.get()
#     if name.strip() == "":
#         output.config(text="Please enter your name first!!")
#     else:
#         output.config(text=f"Hello!! {name}")

# button = tk.Button(window, text="Greet User", command=greet)
# button.pack(pady=20)

# window.mainloop()


window = tk.Tk()
window.title("Styling")
window.geometry("500x300")

label = tk.Label(
    window,
    text="Hello",
    bg="lightblue",
    fg="darkblue",
    font=("Arial", 14, "italic", "bold"),
    relief="groove",
    borderwidth=2
)
label.pack(pady=5)

label.configure()

window.mainloop()
