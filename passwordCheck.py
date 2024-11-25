#Description: This is a program that will get the user to create a strong password
#if a weak password is given then it will give a new suggested password till a strong one is given

import string
import random

#Creating the is_vaild function
def is_valid(password):    
    
    # Checks the length of the password
    if len(password) < 10:
        print("Password is too short.")
        return False
    
    # Initialize flags(i.e the conditions that must be met)
    digit = False
    uppercase = False
    special_char = False
    
    # Checks each character in password
    for char in password:
        if char.isdigit():
            digit = True
        elif char.isupper():
            uppercase = True
        elif char in string.punctuation:
            special_char = True
    
    # Check if all conditions are met
    if digit and uppercase and special_char:
        return True
    else:
        print("Password needs a digit, uppercase letter, or special character.")
        return False


#Creating strenthen password function
def strengthen_password(password):
    
    # Checks the length of the password
    
    # Initialize flags(i.e the conditions that must be met)
    digit = False
    uppercase = False
    special_char = False
    
    # Checks each character in password
    for char in password:
        if char.isdigit():
            digit = True
        elif char.isupper():
            uppercase = True
        elif char in string.punctuation:
            special_char = True
    
    if digit and uppercase and special_char:
        return True
    else:
        #Generates random charcters of each type
        random_char = random.choice(string.ascii_letters + string.digits)
        upper_case = random.choice(string.ascii_uppercase)
        has_digit = random.choice(string.digits)
        special_character = random.choice(string.punctuation)
    
    # Adds the missing character type to the password
        if not digit:
            password += has_digit # Adds digit
        elif not uppercase:
            password += upper_case # adds upper case letter
        elif not special_char:
            password += special_character # Adds random special character
        elif not password > 10:
            password += random_char # adds a random letter
            
        return ("Stronger Suggested password: " + password)

            
# Running the function(Loops until a strong password is recived)
while True:
    user_password = input("Enter a strong password (or type 'exit' to quit): ")
    if user_password.lower() == "exit":
        print("Program exited.")
        break
    if is_valid(user_password):
        print("Password is Strong")
        break
    else:
        print(strengthen_password(user_password))
