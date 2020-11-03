'''Man-o-War
Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line you will receive
the status of the pirate ship, which is a string representing integer sections separated by '>'. On the second line you will receive
the same type of status, but for the warship:
"{section1}>{section2}>{section3}… {sectionn}"
On the third line you will receive the maximum health capacity a section of the ship can reach.
The following lines represent commands until "Retire":

•	Fire {index} {damage} – the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and
if not skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program:
"You won! The enemy ship has sunken."

•	Defend {startIndex} {endIndex} {damage} - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive).
Check if both indexes are valid and if not skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."

•	Repair {index} {health} - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not skip
the command. The health of the section cannot exceed the maximum health capacity.

•	Status – prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of
the maximum health capacity. Print the following:
"{count} sections need repair."

In the end if a stalemate occurs print the status of both ships, which is the sum of their individual sections in the following format:
"Pirate ship status: {pirateShipSum}"
"Warship status: {warshipSum}"
Input
•	On the 1st line you are going to receive the status of the pirate ship (integers separated by '>')
•	On the 2nd line you are going to receive the status of the warship
•	On the 3rd line you are going receive the maximum health a section of a ship can reach.
•	On the next lines, until "Retire", you will be receiving commands.
Output
•	Print the output in the format described above.'''

pirate_ship = input()
pirate_ship = pirate_ship.split('>')

warship = input()
warship = warship.split('>')

health_capacity = int(input())
check = 0

while True:

    string = input()
    command = string.split(' ')


    if command[0]=='Retire':
       break

    elif command[0] == 'Fire':
        if 0 <= int(command[1]) <= len(warship):
            warship[int(command[1])] = int(warship[int(command[1])]) - int(command[2])
            if warship[int(command[1])] <= 0:
                print(f"You won! The enemy ship has sunken.")
                check = 1
                break
        else:
            pass


    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(pirate_ship) and 0 <=end_index <= len(pirate_ship):  # and start_index<= end_index:
            for i in range(start_index, end_index+1):
                pirate_ship[i] = int(pirate_ship[i]) - int(command[3])
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    check = 1
                    break
        else:
          pass

    elif command[0] == 'Repair':
        index = int(command[1])
        if 0 <= int(command[1]) < len(pirate_ship):
            pirate_ship[index] = int(pirate_ship[index]) + int(command[2])
            if int(pirate_ship[index]) > health_capacity:
                pirate_ship[index] = health_capacity
        else:
           pass

    elif command[0] == 'Status':
        count = 0
        for i in range(len(pirate_ship)):
            if float(pirate_ship[i])  < health_capacity * 0.2:
                count += 1

        print(f"{count} sections need repair.")

pirateShipSum = 0
warshipSum = 0

if check == 0:

  for i in range(len(pirate_ship)):
     pirateShipSum += int(pirate_ship[i])

  for i in range(len(warship)):
      warshipSum += int(warship[i])

  print(f"Pirate ship status: {pirateShipSum}")
  print(f"Warship status: {warshipSum}")

#print(warship)
#print(pirate_ship)