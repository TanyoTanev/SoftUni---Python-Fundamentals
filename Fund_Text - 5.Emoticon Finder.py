'''	 Emoticon Finder

Find all emoticons in the text. An emoticon always starts with ":" and is followed by a single symbol or letter.
The input will be provided as a single string.

Example
Input
Output

There are so many emoticons nowadays :P I have many ideas :O what input to place here :)

:P
:O
:)

'''

sentence = input()
emotion = ':'

for i in range(len(sentence)):

    if sentence[i] == ':':
        print(emotion + sentence[i+1])

