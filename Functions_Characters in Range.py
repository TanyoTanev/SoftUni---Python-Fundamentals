'''Characters in Range

Write a function that receives two characters and returns a single string with all the characters in between them according to the ASCII code.
'''

def two_characters(a, b):

    beggining = ord(a)
    end = ord(b)
    string=''
    l1=[]
    for i in range(beggining+1, end):
        l1.append(chr(i))
        l1.append(' ')

    return ''.join(l1)


if __name__ == '__main__':

    a=input()
    b=input()

    print(two_characters(a,b,))
