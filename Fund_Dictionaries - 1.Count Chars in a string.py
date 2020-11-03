'''1.Count Chars in a String

Write a program that counts all characters in a string except for space (' ').
Print all the occurrences in the following format:
{char} -> {occurrences}

Examples
Input
Output

text
t -> 2
e -> 1
x -> 1

text text text
t -> 6
e -> 3
x -> 3
'''
#text = input()#.split(' ')

dd = dict()

#print(dd)

def solve(dd, text=str):


    for i in range(len(text)):
       if text [i] not in dd and text[i] != ' ':
          dd[text[i]] = 1
       elif text[i] in dd and text[i] !=' ':
          dd[text[i]] = dd[text[i]] + 1

    #print(dd)
    return dd


solve(dd,input())
#print(dd['t'])

for key in dd.keys():
    print(f"{key} -> {dd[key]}")