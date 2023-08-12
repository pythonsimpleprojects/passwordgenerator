import random
import string
import tkinter as tk

# Define the uppercase letters
uppercase_letters = string.ascii_uppercase

# Define the lowercase letters by converting the uppercase letters to lowercase
lowercase_letters = uppercase_letters.lower()

# Define the digits
digits = string.digits

# Define the symbols
symbols = "-()[]{}, ; : - -_/\\?+*#*"

# Set the options for the password generator
upper, lower, nums, syms = True, True, True, True

# Initialize the string that will contain all the characters
all_chars = ""

# Add the uppercase letters to the string if the option is selected
if upper:
    all_chars += uppercase_letters

# Add the lowercase letters to the string if the option is selected
if lower:
    all_chars += lowercase_letters

# Add the digits to the string if the option is selected
if nums:
    all_chars += digits

# Add the symbols to the string if the option is selected
if syms:
    all_chars += symbols

# Set the length of the password
length = 25

# Set the number of passwords to generate
amount = 10

# Create a window
window = tk.Tk()
window.title("Password Generator")

# Create a label to display the password
password_label = tk.Label(window, text="Click the button to generate a password")
password_label.pack()

# Define a function to generate a password and display it in the label
def generate_password():
    # Use the random.sample() method to generate a password of the specified length
    password = "".join(random.sample(all_chars, length))
    # Update the label with the generated password
    password_label.config(text=password)

# Create a button to generate a password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Start the main loop of the window
window.mainloop()