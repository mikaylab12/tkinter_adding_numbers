# tkinter exercise
from tkinter import *
# defining the functions
# adding the numbers
def add_numbers():
    add_numbers = int(entry_1.get()) + int(entry_2.get())
    label_text.set(add_numbers)
# clearing the numbers
def clear_numbers():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
# exiting the program
def exit_program():
    return root.destroy()

root = Tk()
label_text = StringVar()
root.geometry("600x150")
root.title("Adding Numbers")

# the first label and entry and their places
label_1 = Label(root, text="Please enter your first number: ")
label_1.place(x=50, y=0)
entry_1 = Entry(root)
entry_1.place(x=300, y=0)
# the second label and entry and their places
label_2 = Label(root, text="Please enter your second number: ")
label_2.place(x=50, y=25)
entry_2 = Entry(root)
entry_2.place(x=300, y=25)
# the third label(result) and entry and their places
label_result = Label(root, text="Your Answer :")
label_result.place(x=50, y=50)
entry_result = Entry(root, state="readonly")
entry_result.place(x=300, y=50)

add = Label(root, text="", textvariable=label_text).place(x=302, y=52)

# add button and its place
a_button = Button(root, text="Add", command=add_numbers)
a_button.place(x=120, y=100)

# clear button and its place
c_button = Button(root, text="Clear", command=clear_numbers)
c_button.place(x=210, y=100)

# exit button and its place
e_button = Button(text="Exit", command=exit_program)
e_button.place(x=300, y=100)

root.mainloop()
