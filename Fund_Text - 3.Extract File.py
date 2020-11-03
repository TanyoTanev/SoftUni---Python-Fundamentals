'''3.Extract File

Write a program that reads the path to a file and subtracts the file name and its extension.

Examples
Input
Output

C:\Internal\training-internal\Template.pptx
File name: Template
File extension: pptx
C:\Projects\Data-Structures\LinkedList.cs
File name: LinkedList
File extension: cs
'''

path = input()

rev_path = path[::-1]
file_extention = ''
file_name = ''

for i in range(len(rev_path)):
    if rev_path[i] !='.':
        file_extention += rev_path[i]

    else:
        idx = i
        break

for i in range(idx+1,len(rev_path)):
    if ord(rev_path[i]) != 92 :
        file_name +=rev_path[i]
    else:
        break


file_extention = file_extention[::-1]
file_name = file_name[::-1]

print(f"File name: {file_name}")
print(f"File extension: {file_extention}")