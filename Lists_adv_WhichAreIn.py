'''Which are in?

Given two lists of strings print a new list of the strings that contains words from the first list which are substrings of any of
the strings in the second list (only unique values)

Input
There will be 2 lines of input: the two lists separated by ", "

Output
Print the resulting list on the console'''

string = input() #'arp, live, strong'  #
list_1 = string.split(', ')

string2 = input() #'lively, alive, harp, sharp, armstrong' #
list_2 = string2.split(', ')

result = []
#word=


#print(list_1)
#print (list_2)
for index in range(len(list_1)):
    subs = list_1[index]
    res = [i for i in list_2 if subs in i]
    if res:
        result.append(list_1[index])

print(result)