'''6.Replace Repeating Chars

Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.

Examples
Input
Output

aaaaabbbbbcdddeeeedssaa
abcdedsa

qqqwerqwecccwd
qwerqwecwd

'''

big_word = input()

word = big_word[0]
big_word = big_word[1:]


i=0

while len(big_word) >0:

      if big_word[0] == word[-1]:
          big_word = big_word[1:]
      else:
          word +=big_word[0]
          big_word = big_word[1:]


print(big_word)
print(word)