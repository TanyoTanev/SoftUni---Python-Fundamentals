'''5.SoftUni Parking
SoftUni just got a new parking lot. It's so fancy, it even has online parking validation. Except the online service doesn't work.
It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
Write a program, which validates a parking place for an online service. Users can register to park and unregister to leave.
The program receives 2 types of commands:
"register {username} {licensePlateNumber}":
The system only supports one car per user at the moment, so if a user tries to register another license plate, using the same username,
the system should print:
"ERROR: already registered with plate number {licensePlateNumber}"

If the aforementioned checks passes successfully, the plate can be registered, so the system should print:
 "{username} registered {licensePlateNumber} successfully"

"unregister {username}":

If the user is not present in the database, the system should print:
"ERROR: user {username} not found"

If the aforementioned check passes successfully, the system should print:
"{username} unregistered successfully"

After you execute all of the commands, print all the currently registered users and their license plates in the format:
"{username} => {licensePlateNumber}"

Input
First line: n – number of commands – integer
Next n lines: commands in one of the two possible formats:
Register: "register {username} {licensePlateNumber}"
Unregister: "unregister {username}"
The input will always be valid and you do not need to check it explicitly.

Examples
Input
Output

5
register John CS1234JS
register George JAVA123S
register Andy AB4142CD
register Jesica VR1223EE
unregister Andy

John registered CS1234JS successfully
George registered JAVA123S successfully
Andy registered AB4142CD successfully
Jesica registered VR1223EE successfully
Andy unregistered successfully
John => CS1234JS
George => JAVA123S
Jesica => VR1223EE

4
register Jony AA4132BB
register Jony AA4132BB
register Linda AA9999BB
unregister Jony
Jony registered AA4132BB successfully
ERROR: already registered with plate number AA4132BB
Linda registered AA9999BB successfully
Jony unregistered successfully
Linda => AA9999BB

6
register Jacob MM1111XX
register Anthony AB1111XX
unregister Jacob
register Joshua DD1111XX
unregister Lily
register Samantha AA9999BB

Jacob registered MM1111XX successfully
Anthony registered AB1111XX successfully
Jacob unregistered successfully
Joshua registered DD1111XX successfully
ERROR: user Lily not found
Samantha registered AA9999BB successfully
Joshua => DD1111XX
Anthony => AB1111XX
Samantha => AA9999BB
'''

parking_place = {}

N = int(input())

for i in range(N):
    command = input().split(' ')
    if command[0] == 'register':
       if command[1] not in parking_place:
        parking_place[command[1]] = command[2]
        print(f"{command[1]} registered {parking_place[command[1]]} successfully")
       else:
        print(f"ERROR: already registered with plate number {parking_place[command[1]]}")


    elif command[0] == 'unregister':
        if command[1] in parking_place:
            parking_place.pop(command[1])
            print(f"{command[1]} unregistered successfully")
        else:
            print(f"ERROR: user {command[1]} not found")


#print(parking_place)

[ print(f"{user} => {parking_place[user]}") for user in parking_place ]