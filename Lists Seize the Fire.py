'''Seize the Fire
The group of adventurists have gone on their first task. Now they have to walk through fire - literally. They have to use all of the
water they have left. Your task is to help them survive.

Create a program that calculates the water that is needed to put out a "fire cell", based on the given information about its "fire level"
and how much it gets affected by water.

First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.
They will be given in the following format:

"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"
Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each of the fire types,
and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.

Type of Fire
Range

High
81 - 125

Medium
51 - 80

Low
1 - 50

If a cell is valid, you have to put it out by reducing the water with its value. Putting out fire also takes effort and you need to calculate it.
Its value is equal to 25% of the cell’s value. In the end you will have to print the total effort. Keep putting out cells until you run out of water.
If you don’t have enough water to put out a given cell – skip it and try the next one. In the end, print the cells you have put out in the following
format:

"Cells:

 - {cell1}
 - {cell2}
 - {cell3}
……

 - {cellN}"
"Effort: {effort}"

In the end, print the total fire you have put out from all of the cells in the following format: "Total Fire: {totalFire}"

Input / Constraints

On the 1st line you are going to receive the fires with their cells in the format described above – integer numbers in the range [1…500]
On the 2nd line, you are going to be given the water – an integer number in the range [0….100000]
'''

string = input()
fire = string.split('#')
water = int(input())
a=0

for i in range(len(fire)):
    fire[i] = fire[i].split(' = ')

#print(fire[1][1])

#Проверка за валидност на клетките

#print(len(fire))
i=0

while i < len(fire):

  if fire[i][0] == 'High':
      if int(fire[i][1]) < 81 or int(fire[i][1]) > 125:
           fire.remove(fire[i])
           i-=1

  elif fire[i][0] == 'Medium':
      if int(fire[i][1]) < 51 or int(fire[i][1]) > 80:
           fire.remove(fire[i])
           i -= 1

  elif fire[i][0] == 'Low':
      if int(fire[i][1]) < 1 or int(fire[i][1]) > 50:
           fire.remove(fire[i])
           i -= 1

  i+=1

#print(len(fire))
#print(fire[0][1])
#print(fire[1][0])
#fire.remove(fire[1])

#print(fire[1][1])
#print(fire[1])
#print(fire)

i = 0
effort = 0

while i < len(fire):
    if water >=int(fire[i][1]) and water > 0:
        water= water - int(fire[i][1])
        effort=effort + int(fire[i][1])
    else:
        fire.remove(fire[i])
        i -= 1
    i+=1

#print(fire)
#print(water)
print('Cells:')
for i in range(len(fire)):
    print(f" - {fire[i][1]}")
print(f"Effort: {effort/4:.2f}")
print(f"Total Fire: {effort}")



