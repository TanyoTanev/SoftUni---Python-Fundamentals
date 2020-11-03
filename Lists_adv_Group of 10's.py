'''Group of 10's

Write a program that receives a list of numbers (string containing integers separated by ", ") and prints lists with the numbers
them into lists of 10's.

Examples:

The numbers 2 8 4 3 fall into the group under 10
The numbers 13 19 14 15 fall into the group under 20
For more details, see the examples below

Input
Output

8, 12, 38, 3, 17, 19, 25, 35, 50

Group of 10's: [8, 3]

Group of 20's: [12, 17, 19]

Group of 30's: [25]

Group of 40's: [38, 35]

Group of 50's: [50]

'''

string = input()#'8, 12, 38, 3, 17, 19, 25, 35, 50'  #
numbers = string.split(', ')
numbers = [int(i) for i in numbers]

#print(numbers)

find_max = max(numbers)
#print(find_max)


groups_count = find_max//10

if find_max % 10 > 0:
    groups_count+=1

groups = [0]*groups_count
#print(groups)

for group in range(groups_count):

    groups[group] = [numbers[i] for i in range(len(numbers)) if 10*group < numbers[i] <= 10*(group+1)]
    print(f"Group of {group+1}0's: {groups[group]}")

#group_of_20 = [numbers[i] for i in range(len(numbers)) if 10< numbers[i] <= 20]
#print(f"Group of 20's: {group_of_20}")

#group_of_30 = [numbers[i] for i in range(len(numbers)) if 20< numbers[i] <= 30]
#print(f"Group of 30's: {group_of_30}")



#print(numbers)