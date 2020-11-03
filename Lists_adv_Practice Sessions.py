'''* Practice Sessions

The racers must practice for the race. Your job is to keep the records of the roads and the time for each lap. The track with the best time
will be the chosen one for the finals.

Write a program, that keeps information about roads and the racers who practice on them.  When the practice begins, you’re going to start receiving
data until you get the "END" message. There are three possible commands:

"Add->{road}->{racer}"
Add the road if it doesn't exist in your collection and add the racer to it.

"Move->{currentRoad}->{racer}->{nextRoad}"
Find the racer on the current road and move him to the next one, only if he exists in the current road. Both roads will always be valid and
will already exist.

"Close->{road}"
Find the road and remove it from the sessions, along with the racers on it if it exists.

In the end, print all of the roads with the racers who have practiced and ordered by the count of the racers in descending order, then by
the roads in ascending order. The output must be in the following format:

Practice sessions:

{road}
++{racer}
++{racer}
++{racer}
………………………..

Input / Constraints

You will be receiving lines of information in the format described above, until you receive the "END" command.
The input will always be in the right format.
Both roads from the "Move" command will always be valid and you don't need to check them explicitly.

Output
Print the roads with their racers in the format described above.
Add->Glencrutchery Road->Giacomo Agostini
Add->Braddan->Geoff Duke
Add->Peel road->Mike Hailwood
Add->Glencrutchery Road->Guy Martin
Move->Glencrutchery Road->Giacomo Agostini->Peel road
Close->Braddan
END

Move->Braddan->John McGuinness->Glen Vine

Add->Glen Vine->Steve Hislop
Add->Ramsey road->John McGuinness
Add->Glen Vine->Ian Hutchinson
Add->Ramsey road->Dave Molyneux

Add->A18 Snaefell mountain road->Mike Hailwood
Add->Braddan->Geoff Duke
Move->A18 Snaefell mountain road->Mike Hailwood->Braddan

Close->A18 Snaefell mountain road
END
'''

practice= []

while True:

    string = input()
    command = string.split('->')

    if command[0]=='END':
       break

    elif command[0] == 'Add':
        pilot_name = command[2].split(',')
        if len([x for x in practice if x[0] == command[1]])>0:

            idx = practice.index([ road for road in practice if road[0]==command[1]][0])
            #print(idx)
            practice[idx][1].extend(pilot_name)
        else:
            practice.append([command[1],pilot_name])

    elif command[0] == 'Move':
        current_road = command[1]
        pilot_name = command[2]
        next_road = command[3]
        idx_road = practice.index([ road for road in practice if road[0]==command[1]][0])
        idx_pilot = None
        for i in range(len(practice[idx_road][1])):
            if practice[idx_road][1][i] == command[2]:
               idx_pilot = i

        #print(idx_pilot)
        if idx_pilot != None :
            idx_next_road = practice.index([road for road in practice if road[0] == command[3]][0])
        #print(idx_next_road)
            practice[idx_next_road][1].append(practice[idx_road][1][idx_pilot])
            practice[idx_road][1].pop(idx_pilot)

    elif command[0] == 'Close':
        idx_road = practice.index([road for road in practice if road[0] == command[1]][0])
        practice.remove(practice[idx_road])

#print([practice[idx_road][1]])
#a=len(practice[idx_road][1])
#print(a)
#print(practice)
#print(practice[0][1][0])

#sorted_practice_asc = practice[0].sort()        #practice, )
#sorted_practice = sorted(practice, key= lambda x:  (len(x[1]), x[0]), reverse=True)

#sorted_practice = sorted(sorted(practice, key= lambda x:  len(x[1]), reverse=True), key = lambda x: (x[0]) , reverse=True)
sorted_practice = sorted(sorted(practice, key = lambda x: (x[0]) , reverse=False), key= lambda x:  len(x[1]), reverse=True)

#print(sorted_practice)

print('Practice sessions:')

for i in range(len(sorted_practice)):
    print(f"{sorted_practice[i][0]}")
    for j in range(len(sorted_practice[i][1])):
     print(f"++{sorted_practice[i][1][j]}")