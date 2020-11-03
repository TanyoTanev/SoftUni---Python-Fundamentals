''' Treasury Hunt
The pirates need to carry a treasure chest safely back to the ship. Looting along the way.
Create a program that manages the state of the treasure chest along the way. On the first line you will receive the initial
loot of the treasure chest, which is a string of items separated by a '|'.
"{loot1}|{loot2}|{loot3}… {lootn}"
The following lines represent commands until "Yohoho!" which ends the treasure hunt:
•	Loot {item1} {item2}…{itemn} – pick up treasure loot along the way. Insert the items at the beginning of the chest.
If an item is already contained don't insert it.
•	Drop {index} – remove the loot at the given position and add it at the end of the treasure chest. If the index is invalid skip the command.
•	Steal {count} – someone steals the last count loot items. If there are less items than the given count remove as much as there are.

Print the stolen items separated by ', ':
{item1}, {item2}, {item3} … {itemcount}
In the end output the average treasure gain which is the sum of all treasure items length divided by the count of all items inside the chest
 formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty print the following message:
"Failed treasure hunt."

Input
•	On the 1st line you are going to receive the initial treasure chest (loot separated by '|')
•	On the next lines, until "Yohoho!", you will be receiving commands.

Output
•	Print the output in the format described above.
Constraints
•	The loot items will be strings containing any ASCII code.
•	The indexes will be integers in the range [-200…200]
•	The count will be an integer in the range [1….100]'''

chest = input()
chest = chest.split('|')
stolen = []

while True:

    string = input()
    command = string.split(' ')


    if command[0]=='Yohoho!':
       break

    elif command[0] == 'Loot':

        for i in range(1,len(command)):
            if command[i] not in chest:
                chest = [command[i]] + chest

    elif command[0] == 'Drop':
        if int(command[1]) < len(chest) and int(command[1]) >= 0:
            chest.append(chest.pop(int(command[1])))
        else:
            pass

    elif command[0] == 'Steal':
        if int(command[1]) >= len(chest):
            stolen = chest[:]
            chest = []
        elif 0 <= int(command[1]) < len(chest):
            stolen = chest[ - int(command[1]):]
            chest = chest[: - int(command[1])]

#print(chest)
#print(stolen)

#for i in range(len(stolen)):
    #print(f"{', '}{stolen[i]}", end ="")
print(', '.join(stolen[:]))


treaure_gain = 0
for i in range(len(chest)):
    treaure_gain +=len(chest[i])

if len(chest) == 0:
    print(f"Failed treasure hunt.")
else:
    print(f"Average treasure gain: {treaure_gain/len(chest):.2f} pirate credits.")