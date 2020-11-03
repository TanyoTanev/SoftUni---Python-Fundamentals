'''Office Chairs

So you've found a meeting room - phew! You arrive there ready to present, and find that someone has taken one or more of the chairs!!
You need to find some quick.... check all the other meeting rooms to see if all of the chairs are in use.

You will be given a number n representing how many rooms there are. On the next n lines for each room you will get how many chairs
there are and how many of them will be taken. The chairs will be represented by "X"s, then there will be a space " " and a number
representing the taken places. Example: "XXXXX 4" (5 chairs and 1 of them is left free). Keep track of the free chairs, you will need them later.
However if you get to a room where there are more people than chairs, print the following message: "{needed_chairs_in_room} more chairs needed in room
{number_of_room}". If there is enough chairs in each room print: "Game On, {total_free_chairs} free chairs left"
'''

n= int(input())
total_free_chairs=0
if_not_enough=0

for i in range(n):
    string = input()
    room = string.split(' ')
    chairs = room[0]
    number_chairs = 0
    #res = [counter+1 for j in chairs if j=='X']
    for j in chairs:
        if j=='X':
            number_chairs+=1
    #number_chairs = len(res)
    #print(number_chairs)
    if number_chairs < int(room[1]):
        print(f"{int(room[1])-number_chairs} more chairs needed in room {i+1}")
        if_not_enough+=1
    else:
        total_free_chairs = total_free_chairs + (number_chairs-int(room[1]))

if not if_not_enough:
    print(f"Game On, {total_free_chairs} free chairs left")

