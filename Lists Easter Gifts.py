'''* Easter Gifts
As a good friend, you decide to buy presents for your friends.Create a program that helps you plan the gifts for your
friends and family. First, you are going to receive the gifts you plan on buying оn a single line, separated by space, in the following format:

"{gift1} {gift2} {gift3}… {giftn}"

Then you will start receiving commands until you read the "No Money" message. There are three possible commands:

"OutOfStock {gift}"
Find the gifts with this name in your collection, if there are any, and change their values to "None".

"Required {gift} {index}"
Replace the value of the current gift on the given index with this gift, if the index is valid.
"JustInCase {gift}"
Replace the value of your last gift with this one. In the end, print the gifts on a single line, except the ones with value "None", separated by
a single space in the following format:

"{gift1} {gift2} {gift3}… {giftn}"

Input / Constraints

On the 1st line you are going to receive the names of the gifts, separated by a single space.

On the next lines, until the "No Money" command is received, you will be receiving commands.

The input will always be valid.

'''
OUTOFSTOCK = 'OutOfStock'
REQUIRED = 'Required'
JUSTINCASE = 'JustInCase'

string = input()
gifts = string.split(' ')
#print(gifts)
command=()

#print(len(gifts))

#command=input()
#command=command.split(' ')

while True:
    command= input()
    if command == 'No Money':
        break
       #command = input()
    command = command.split(' ')
    #print(command)



    if command[0] == OUTOFSTOCK:

        gifts = [sub.replace( command[1], 'None') for sub in gifts]

    elif command[0] == REQUIRED and int(command[2]) <= (len(gifts)-1) and int(command[2])>=0:

       gifts[int(command[2])]=command[1]  #gifts = [sub.replace( gifts[int(command[2])], command[1]) for sub in gifts]

    elif command[0] == JUSTINCASE and len(gifts)>0:
        gifts[len(gifts)-1] = command[1]
        #gifts = [sub.replace( gifts[len(gifts)-1], command[1]) for sub in gifts]




for i in range(len(gifts)):
    if gifts[i] !='None':
        print(f"{gifts[i]}",end=' ')