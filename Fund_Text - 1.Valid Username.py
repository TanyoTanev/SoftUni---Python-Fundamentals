'''1. Valid Usernames
Write a program that reads user names on a single line (joined by ", ") and prints all valid usernames.
A valid username is:
 Has length between 3 and 16 characters
 Contains only letters, numbers, hyphens and underscores
 Has no redundant symbols before, after or in between

Examples
Input
Output

sh, too_long_username, !lleg@l ch@rs, jeffbutt
jeffbutt
Jeff, john_45, ab, cd, peter-ivanov, @smith

Jeff
John45
peter-ivanov
'''


names = input().split(", ")
valid_names = [ names[i] for i in range(len(names))]

#print(valid_names)

for name in names:

    for k in range(len(name)):

        ch = name[k]
        if len(name) <= 3 or len(name) >= 16 or 0 <= ord(ch) <= 44 or  46<= ord(ch) <=47 or 58 <= ord(ch) <= 64 or 91 <= ord(ch) <= 94 or ord(ch)== 96 or 123 <= ord(ch) <= 127:

            valid_names.remove(name)
            break
        #else:
         #  if names[i] not in valid_names:
          #     valid_names.append(names[i])

for i in range(len(valid_names)):
   print(valid_names[i])