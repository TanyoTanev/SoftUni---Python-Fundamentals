'''9.*ForceBook

The force users are struggling to remember which side are the different forceUsers from, because they switch them too often. So you are tasked
to create a web application to manage their profiles. You should store an information for every unique forceUser, registered in the application.
You will receive several input lines in one of the following formats:

{forceSide} | {forceUser}

{forceUser} -> {forceSide}

The forceUser and forceSide are strings, containing any character.

If you receive forceSide | forceUser, you should check if such forceUser already exists, and if not, add him/her to the corresponding side.

If you receive a forceUser -> forceSide, you should check if there is such a forceUser already and if so, change his/her side.
If there is no such forceUser, add him/her to the corresponding forceSide, treating the command as a new registered forceUser.
Then you should print on the console: "{forceUser} joins the {forceSide} side!"

You should end your program when you receive the command "Lumpawaroo". At that point you should print each force side, ordered descending
by forceUsers count, than ordered by name. For each side print the forceUsers, ordered by name.

In case there are no forceUsers in a side, you shouldn`t print the side information.

Input / Constraints

The input comes in the form of commands in one of the formats specified above.
The input ends, when you receive the command "Lumpawaroo".

Output
As output for each forceSide, ordered descending by forceUsers count, then by name,  you must print all the forceUsers, ordered by name alphabetically.

The output format is:
Side: {forceSide}, Members: {forceUsers.Count}
! {forceUser}
! {forceUser}
! {forceUser}

In case there are NO forceUsers, don`t print this side.

Examples
Input
Output
Comments

Light | Gosho
Dark | Pesho
Lumpawaroo

Side: Dark, Members: 1
! Pesho
Side: Light, Members: 1
! Gosho

We register Gosho in the Light side and Pesho in the Dark side. After receiving "Lumpawaroo" we print both sides, ordered by membersCount and
then by name.

Lighter | Royal
Lighter | Tanev
Ivan Ivanov -> Lighter
DCay -> Lighter
Ivan Ivanov -> Darker
Stamat -> Dorker
Lumpawaroo


Darker | Royal
Darker | DCay

Ivan Ivanov joins the Lighter side!
DCay joins the Lighter side!
Side: Lighter, Members: 3
! DCay
! Ivan Ivanov
! Royal

Although Ivan Ivanov doesn`t have profile, we register him and add him to the Lighter side.
We remove DCay from Darker side and add him to Lighter side.
We print only Lighter side because Darker side has no members.
'''

sides = dict()

while True:

    command = input()
    if command == 'Lumpawaroo':
        break
    elif ' | ' in command:
        command = command.split(' | ')    #Light | Gosho
        if command[0] not in sides and command[1] not in [x for v in sides.values() for x in v]:
            sides[command[0]] = [command[1]]
        elif command[0] in sides and command[1] not in [x for v in sides.values() for x in v]:
           sides[command[0]].append(command[1])


    elif ' -> ' in command:
        command = command.split(' -> ')   #DCay -> Lighter

        if command[0] not in [x for v in sides.values() for x in v] and command[1] in sides:
            sides[command[1]].append(command[0])
            print(f"{command[0]} joins the {command[1]} side!")

        elif command[0] not in [x for v in sides.values() for x in v] and command[1] not in sides:
             sides[command[1]] = [ command[0] ]
             print(f"{command[0]} joins the {command[1]} side!")


        elif command [0] in [x for v in sides.values() for x in v] and command[1] in sides:
            for key, value in sides.items():
                for i in range(len(value)):
                  if value[i] == command[0]:
                      del sides[key][i]
                      break
            sides[command[1]].append(command[0])
            print(f"{command[0]} joins the {command[1]} side!")

        else:
            for key, value in sides.items():
                for i in range(len(value)):
                  if value[i] == command[0]:
                      del sides[key][i]
                      break
            sides[command[1]] = [command[0]]
            print(f"{command[0]} joins the {command[1]} side!")




#print(sides)


sorted_sides = dict( sorted(sides.items(), key=lambda x: (-len(x[1]), x[0]), reverse=False) )


for key in sorted_sides:
    sorted_sides[key] = (sorted( sorted_sides[key], key=lambda x:x[0], reverse=False ))

#print(sorted_sides)

for side in sorted_sides:
    if len(sorted_sides[side]):
      print(f"Side: {side}, Members: {len(sorted_sides[side])}")
    for i in range(len(sorted_sides[side])):
        print(f"! {sorted_sides[side][i]}")

