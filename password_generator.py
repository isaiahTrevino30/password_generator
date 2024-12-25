import random
import string 

# Generate Password function with parameters of min_length (minimum length of password),
# numbers optional parameter (If the user does want numbers in password), 
# and special characters optional parameter (If user does want special characters in password)
def generate_password(min_length, numbers=True, special_characters = True):
    # Grab all the potential characters (numbers, special characters, letters, punctuation, etc)
    # from ASCII Table between 33 and 126 
    letters = string.ascii_letters 
    digits = string.digits 
    special = string.punctuation 

    # Combine all 3 variables into one kind of list or one large string, 
    # where the program are going to randomly choose from
    # HOWEVER, that string that the program is going to randomly choose from
    # should only contain what the parameters specify
    characters = letters 
    if numbers: # checks if numbers is TRUE
        characters += digits 

    if special_characters: # checks if special_characters is TRUE
        characters += special 

    
    # A loop, during which in each iteration a new character to add in new random generated password
    # The loop will continue until the criteria is met
    pwd = "" # Initialized an empty string password variable
    meets_criteria = False # a Boolean variable that will check to see if password generated meets criteria
    has_number = False # A boolean variable that will check if password generated has a number
    has_special = False # A boolean variable that will check if password generated has a special character
    while not meets_criteria or len(pwd) < min_length: # While the iteration of loop does not meet criteria (whatever it may be) OR the length of password generated is less than the minimum length of password from user input
        # generate a random character to add to password, then IF it's a number, add it, then IF it's a special character, add it
        new_char = random.choice(characters) # pick random elements from the characters string
        pwd += new_char # increment new random character into password 
        if new_char in digits:
            has_number = True 
        elif new_char in special:
            has_special = True 

        # update meets criteria, hard code the variable to TRUE, have the program try to prove that the variable is FALSE
        meets_criteria = True 
        if numbers: # if there is a number, then
            meets_criteria = has_number # if there is a number, it is true, otherwise false
        if special_characters: # if there is a special character, then
            meets_criteria = meets_criteria and has_special # if the criteria has been met AND that there is a special charcter, TRUE, otherwise FALSE

    # return generated password 
    return pwd 
        




    #print(letters, digits, special) # debug output statement
# Ask user for minimum length for password
min_length = int(input('Input the minimum length for your password: '))
# ask user if they want numbers in their password
has_number = input('Do you want to have numbers in your password? (y/n) ').lower() == "y"
# ask user if they want special characters in their password
has_special = input('Do you want to have special characters in your password? (y/n) ').lower() == "y"

# call the function with the user inputs as parameters, and assign the new generated password to pwd variable
pwd = generate_password(min_length, has_number, has_special) 
print('The new generated password is: ')
print(pwd) # output the genrated password