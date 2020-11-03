'''Password Validator

Write a function that checks if a given password is valid. Password validations are:
The length should be 6 - 10 characters (inclusive)
It should consists only letters and digits
It should have at least 2 digits
If a password is valid print "Password is valid".
If it is NOT valid, for every unfulfilled rule print a message:
"Password must be between 6 and 10 characters"
"Password must consist only of letters and digits"
"Password must have at least 2 digits"

Examples'''

def password_validator (string):

    result  = []
    digits = 0
    digits_letters =0

    if len(string)< 6 or len(string)>10:
        result.append('Password must be between 6 and 10 characters')


    for i in range(len(string)):
        code_i = ord(string[i])
        if (code_i< 48 or (code_i>57 and code_i<65) or (91<= code_i <=96) or (123 <= code_i <= 127)) and digits_letters==0:
            result.append('Password must consist only of letters and digits')
            digits_letters=1
        if 48<=code_i<=57:
            digits+=1

    if digits<2:
        result.append('Password must have at least 2 digits')

    return result

if __name__ == '__main__':

    result = password_validator(input())
    if result:
      for i in range(len(result)):

       print(result[i])
    else:
        print('Password is valid')