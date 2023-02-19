"""
    Name: Qingtao Pan
    Date: 19/2/2023
    assignment PasswordChecker1
    ----Design a program to check user passwords to match requirements
"""

# pseudocode
# Program PasswordChecker1
#   MIN_PASSWORD_LENGTH = 6
#   MAX_PASSWORD_LENGTH = 10
#   INPUT password
#   password_length = len(password)
#   WHILE (password_length < MIN_PASSWORD_LENGTH
#       OR password_length > MAX_PASSWORD_LENGTH)
#       INPUT password
#       password_length = len(password)
#   ENDWHILE
#   OUTPUT password_length
#   IF password.isalpha THEN
#       OUTPUT "password weak – contains only letters"
#   ELSE IF password.isnumeric THEN
#       OUTPUT "password weak – contains only numbers"
#   ELSE
#       OUTPUT "password strong"
# END

# statement
print('PasswordChecker1 program developed by: "Qingtao Pan"')

# assign constants
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 10

# input
password = input("Enter your password: ")

# processing
password_length = len(password)

# validate the password length
while password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
    password_length = len(input("Re-input your password: "))

# output
print(password_length)

# determine if the password is weak or strong
if password.isalpha():
    print("password weak – contains only letters")
elif password.isnumeric():
    print("password weak – contains only numbers")
else:
    print("password strong")
