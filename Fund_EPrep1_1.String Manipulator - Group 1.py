'''1.String Manipulator - Group 1
Create a program that executes changes over a string. First, you are going to receive the string, then commands.
You will be receiving commands until the "End" command. There are six possible commands:
•	"Translate {char} {replacement}"
o	Replace all occurences of {char} with {replacement}, then print the string.
•	"Includes {string}"
o	Check if the string includes {string} and print "True/False".
•	"Start {string}"
o	Check if the string starts with {string} and print "True/False".
•	"Lowercase"
o	Make the whole string lowercased, then print it.
•	"FindIndex {char}"
o	Find the last index of {char}, then print it.
•	"Remove {startIndex} {count}"
o	Remove {count} characters from the string, starting from {startIndex}, then print it.
Input
•	On the 1st line you are going to receive the string.
•	On the next lines, until the "End" command is received, you will be receiving commands.
•	All commands are case sensitive.
•	The input will always be valid.
Output
•	Print the output of every command in the format described above.
'''

string = input()
command = ''

while True:

    command = input().split(' ')
    if command[0] == 'End':
            break

    if command[0] == 'Translate':
        string = string.replace(command[1],command[2])
        print(string)

    elif command[0] == 'Includes':
        if command[1] in string:
            print(True)
        else:
            print(False)

    elif command[0] == 'Start':
        if string.startswith(command[1]):
            print(True)
        else:
            print(False)

    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif command[0] == 'FindIndex':
         print(string.rfind(command[1]))

    elif command[0] == 'Remove':
         string = string[0: int(command[1])] + string[int(command[1])+int(command[2]):]
         print(string)








