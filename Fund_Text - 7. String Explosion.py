'''7.String Explosion

Explosions are marked with '>'. Immediately after the mark, there will be an integer, which signifies the strength of the explosion.
You should remove x characters (where x is the strength of the explosion), starting after the punch character ('>').
If you find another explosion mark ('>') while you’re deleting characters, you should add the strength to your previous explosion.
When all characters are processed, print the string without the deleted characters.
You should not delete the explosion character – '>', but you should delete the integers, which represent the strength.

Input
You will receive single line with the string.
Output
Print what is left from the string after explosions.

Constraints
You will always receive a strength for the punches
The path will consist only of letters from the Latin alphabet, integers and the char '>'
The strength of the punches will be in the interval [0…9]

Examples
Input
Output
Comments

abv>1>1>2>2asdasd
abv>>>>dasd

1st explosion is at index 3 and it is with strength of 1. We delete only the digit after the explosion character.
The string will look like this: abv>>1>2>2asdasd
2nd explosion is with strength one and the string transforms to this: abv>>>2>2asdasd
3rd explosion is now with strength of 2. We delete the digit and we find another explosion. At this point the string looks like this: abv>>>>2asdasd.
4th explosion is with strength 2. We have 1 strength left from the previous explosion, we add the strength of the current explosion to what is
left and that adds up to a total strength of 3. We delete the next three characters and we receive the string abv>>>>dasd

We do not have any more explosions and we print the result: abv>>>>dasd

pesho>2sis>5a>9akarate>9hexmaster

pesho>is>a>karate>master
'''

word = input()
explosion_strength = 0
word_to_print = ''

while word:

    if word[0] != '>':
        word_to_print += word[0]
        word = word[1:]


    else: #word[0] == '>':

        explosion_strength += int(word[1]) - 1
        word_to_print += word[0]
        word = word[2:]
        if explosion_strength:
            while explosion_strength and word:
                if word[0] != '>':
                    word=word[1:]
                    explosion_strength -= 1
                else:
                    word_to_print +=word[0]
                    explosion_strength += int(word[1])-1
                    word = word[2:]


#print(explosion_strength)
#print(f"word e: {word}")
print(word_to_print)