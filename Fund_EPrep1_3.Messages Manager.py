'''3.Messages Manager
Create a program that manages messages sent and received of users. You need to keep information about username, their sent and received messages.
You will receive the capacity of possible messages kept at once per user. You will be receiving lines with commands until you receive the "Statistics"
 command.  There are three possible commands:
•	"Add={username}={sent}={received}":
o	Add the username, his/her sent and received messages to your records. If person with the given username already exists ignore the line.
•	"Message={sender}={receiver}":
o	Check if both usernames exist and if they do, increase the sender’s sent messages by 1 and the receiver’s received messages by 1.
If anyone reaches the capacity (first check the sender), he/she should be removed from the record and you should print the following message:
	"{username} reached the capacity!"
•	"Empty={username}":
o	Delete all records of the given user, if he exists. If "All" is given as username - delete all records you have.

In the end, you have to print the count of users, each person with his/her messages (the count of both sent and received) sorted in descending order
by the received messages and then by their username in ascending order in the following format:

Users count: {count}
{username} - {messages}
{username} - {messages}
Input
•	On the first line, you will receive the capacity - an integer number in the range [1-10000].
•	You will be receiving lines until you receive the "Statistics" command.
•	The initial messages (sent and received) will always be below the capacity.
•	The input will always be valid.
Output
•	Print the appropriate message after the "Message" command, if someone reaches the capacity.
•	Print the users with their messages in the format described above.
'''

messages = dict()
capacity = int(input())


while True:

    command = input().split('=')
    if command[0] == 'Statistics':
        break

    elif command[0]== 'Add' and command[1] not in messages:

        messages[command[1]] = []
        messages[command[1]].append(int(command[2]))  # SENT
        messages[command[1]].append(int(command[3]))  # RECEIVED

    elif command[0]== 'Message':
         if command[1] in messages and command[2] in messages:
          messages[command[1]][0] = int(messages[command[1]][0]) + 1
          messages[command[2]][1] = int(messages[command[2]][1]) + 1
          if int(messages[command[1]][0]) + int(messages[command[1]][1]) > capacity-1:
             print(f"{command[1]} reached the capacity!")
             messages.pop(command[1])
          if int(messages[command[2]][0]) + int(messages[command[2]][1])  > capacity - 1:
             print(f"{command[2]} reached the capacity!")
             messages.pop(command[2])

    elif command[0] == 'Empty':
        if command[1] == 'All':
            messages = dict()
        if command[1] in messages:
            messages.pop(command[1])


print(f"Users count: {len(messages)}")
#print(messages)

sorted_messages = dict(sorted(messages.items(), key= lambda x: ( -x[1][1], x[0] ), reverse= False))
#print(sorted_messages)

for name in sorted_messages.keys():
    print(f"{name} - {sorted_messages[name][0]+sorted_messages[name][1]}")
