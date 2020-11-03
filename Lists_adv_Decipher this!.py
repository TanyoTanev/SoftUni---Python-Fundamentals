'''Decipher this!

You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
For each word:
the second and the last letter are switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)

Example
Input
Output

72olle 103doo 100ya

Hello good day

82yade 115te 103o
'''

string = input()#'82yade 115te 103o'  #input()#'72olle 103doo 100ya'  #
message = string.split(' ')
new_message = [0] * len(message)


for i in range(len(message)):
    word = message[i]

    res = [s for s in word if s.isdigit()]
    a = (''.join(res))

    res = [s for s in word if not s.isdigit()]
    b = (''.join(res))

    second_char = b[-1]
    middle_part=b[1:-1]
    if len(b) >= 2:
        last_char = b[0]
    else:
        last_char =''


    new_message[i]=chr(int(a))+second_char+middle_part+last_char


for i in range(len(new_message)):

    print(new_message[i],end=' ')