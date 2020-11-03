'''2.A Miner Task

You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource
(e.g. Gold, Silver, Copper, and so on) and every even – quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:

{resource} –> {quantity}

The quantities will be in the range [1 … 2 000 000 000]
Examples
Input
Output

Input
Output

Gold
155
Silver
10
Copper
17
stop

Gold -> 155
Silver -> 10
Copper -> 17


gold
155
silver
10
copper
17
gold
15
stop

gold -> 170
silver -> 10
copper -> 17
'''

resourses = dict()

while True:

    command = input()

    if command == 'stop':
        break
    else:
        if command not in resourses:
            resourses[command] = int(input())
        else:
            resourses[command] += int(input())

#print(resourses)


def solve (resourses=dict):

    for (metal) in resourses:
        print(f"{metal} -> {resourses[metal]}")

solve(resourses)