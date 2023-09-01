# This code is a simple calculator application built using the Tkinter library in Python. 
#It creates a graphical user interface (GUI) with buttons representing numbers, arithmetic operators,
# and functions for performing calculations. The calculator allows users to input numbers, perform arithmetic operations,
# and clear the input field.

# Updated on: 8/29/2023
# Updated by: 
#Gulzat Kaipova
#Alinura Sultanova

# This imports all the classes and functions from the tkinter module,
#allowing you to use them without needing to explicitly reference the module each time.
from tkinter import *

# Create the main application window
root = Tk()

#Set the title of the application window
root.title("Simple Calculator")

# Create an entry widget for user input
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define a function to handle button clicks and update the input field
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Define a function to handle button clicks and update the input field
def button_clear():
    e.delete(0, END)

# Define a function to handle operator buttons (+, -, *, /) and store the first number
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# Define a function to perform calculations when the equal button is pressed
def button_equal():
    second_number = e.get()   #Get the value entered in the entry widget as the second number
    e.delete(0, END)   # Clear the entry widget for the next input
    if num_operator == '+':    # Check the operator stored in 'num_operator' and perform the corresponding calculation
        e.insert(0, f_num + int(second_number))   # Perform addition
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))    # Perform multiplication
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))    # Perform division
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))    # Perform subtraction
    else:
        e.insert(0, "Invalid!!!")    # Display 'Invalid!!!' if operator is unrecognized


# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

# Create number and operator buttons using lambda functions to handle clicks
button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Create operator buttons using lambda functions
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Arrange buttons using grid layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Start the main event loop

root.mainloop()