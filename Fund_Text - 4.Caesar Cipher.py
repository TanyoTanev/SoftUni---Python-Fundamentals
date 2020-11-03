'''4. Caesar Cipher

Write a program that returns an encrypted version of the same text. Encrypt the text by shifting each character with three positions forward.
For example A would be replaced by D, B would become E, and so on. Print the encrypted text.

Examples
Input
Output

Programming is cool!
Surjudpplqj#lv#frro$
One year has 365 days.
Rqh#|hdu#kdv#698#gd|v1
'''

word = input()
encrypted = ''

for i in range(len(word)):
    encrypted += chr( ord(word[i]) +3)

print(encrypted)
