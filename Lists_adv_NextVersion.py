'''Next Version
You're fed up about changing the version of your software manually. Instead, you will create a little script that will make it for you.

You will be given a version as in this example: "1.3.4". You have to find the next version and print it ("1.3.5" from the example).
The only rule is that the numbers cannot be greater than 9. If that happens, set the current number to 0 and increase the number before it.
For more clarification, see the examples. Note: there will be no case where the first number will get greater than 9
'''
string = input()#'1.9.9'  #
version = string.split('.')

version = [int(i) for i in version]

#print(version)


if version[2]==9:
    version[2]=0
    if version[1]==9:
        version[0]=version[0]+1
        version[1]=0
    else:
        version[1]=version[1]+1
else:
    version[2] = version[2] + 1

#print(version)
print(f"{version[0]}.{version[1]}.{version[2]}")