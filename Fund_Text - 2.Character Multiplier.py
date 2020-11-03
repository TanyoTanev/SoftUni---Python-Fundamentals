'''2.Character Multiplier

Create a program that receives two strings on a single lines seperated by space and prints the sum of their character codes multiplied
(multiply str1[0] with str2[0] and add to the total sum). Then continue with the next two characters. If one of the strings is longer than the other,
add the remaining character codes to the total sum without multiplication.

Examples
Input
Output

Gosho Pesho
53253
123 522
7647


9700
'''

words = input().split(' ')
total_sum = 0

if len(words[0]) >= len(words[1]):
  word_1 = words[0]
  word_2 = words[1]
else:
    word_1= words[1]
    word_2 = words[0]

#print(word_1)
#print(word_2)

for i in range(len(word_1)):

    if i <= len(word_2) - 1:
        total_sum += ord(word_1[i])*ord(word_2[i])
    else:
        total_sum += ord(word_1[i])

print(total_sum)