'''*10.SoftUni Exam Results

Judge statistics on the last Programing Fundamentals exam was not working correctly, so you have the task to take all the submissions and analyze
them properly. You should collect all the submissions and print the final results and statistics about each language that the participants submitted
their solutions in.

You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished".
You should store each username and his submissions and points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user
from the contest, but preserve his submissions in the total count of submissions for each language.

After receiving "exam finished" print each of the participants, ordered descending by their max points, then by username, in the following format:

Results:
{username} | {points}
…

After that print each language, used in the exam, ordered descending by total submission count and then by language name, in the following format:
Submissions:

{language} – {submissionsCount}
…

Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}".
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];

Output
Print the exam results for each participant, ordered descending by max points and then by username, in the following format:
Results:
{username} | {points}
…

After that print each language, ordered descending by total submissions and then by language name, in the following format:
Submissions:
{language} – {submissionsCount}
…

Allowed working time / memory: 100ms / 16MB.
Examples
Input
Output
Comment

Pesho-Java-84
Gosho-C#-84
Gosho-C#-70
Kiro-C#-94
exam finished

Results:
Kiro | 94
Gosho | 84
Pesho | 84
Submissions:
C# - 3
Java - 1

We order the participant descending by max points and then by name, printing only the username and the max points.
After that we print each language along with the count of submissions, ordered descending by submissions count, and then by language name.

Pesho-Java-91
Gosho-C#-84
Kiro-Java-90
Kiro-C#-50
Kiro-banned
exam finished

Results:
Pesho | 91
Gosho | 84
Submissions:
C# - 2
Java - 2

Kiro is banned so he is removed from the contest, but he`s submissions are still preserved in the languages submissions count.
So althou there are only 2 participants in the results, there are 4 submissions in total.
'''

exam = dict()
persons = dict()

while True:

    command = input()

    if command == 'exam finished':
        break

    else:
        command = command.split('-')

        if len(command) == 3:                  # {username}-{language}-{points}
           command[2] = int(command[2])

           if command[1] not in exam.keys():
               exam[command[1]] = {command[0]: []}
               exam[command[1]][command[0]].append(command[2])
               persons[command[0]] = [command[2]]

           elif command[1] in exam.keys():        # {username}-{language}-{points}
                if command[0] not in exam[command[1]]:
                   exam[command[1]][command[0]] = []
                   exam[command[1]] [command[0]].append(command[2])  #=  (command[2])
                   if command[0] in persons:
                    persons[command[0]].append(command[2])
                   else:
                    persons[command[0]] = [command[2]]


                else: # if person is inside
                    exam[command[1]][command[0]].append(command[2]) # = (exam[command[1]][command[0]], command[2])
                    persons[command[0]].append(command[2])

        elif len(command) == 2:  # {username}-banned

             for key in exam.keys():
                 if command[0] in exam[key]:
                     exam[key][command[0]].append(-1)  # MEANS BANNED
                     persons[command[0]].append(-1) # MEANS BANNED


#print(exam)
#print(persons)

sorted_exam = dict(sorted(exam.items(), key = lambda x: (-len(x[1]), x[0]), reverse=False))
#print(sorted_exam)
sorted_persons = dict(sorted(persons.items(), key= lambda x: (-max(x[1]), x[0]), reverse= False))
#print(persons)
#print(sorted_persons)


print(f"Results:")

for person in sorted_persons.keys():
    if -1 not in sorted_persons[person]:
          print(f"{person} | {max(sorted_persons[person])}")

#print(sorted_exam)

print(f"Submissions:")
for key in sorted_exam.keys():
    submissions = 0
    for person in sorted_exam[key]:
        if -1 not in sorted_exam[key][person]:
          submissions += len(sorted_exam[key][person])
        else:
            submissions += len(sorted_exam[key][person])-1

    print(f"{key} - {submissions}")


