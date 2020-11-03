'''Faro Shuffle

A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in
the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list

['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]
Write a program that receives a single string (cards separated by a space) and on the second line receives a number of
faro shuffles that have to be made. Print the state of the deck after the shuffle

Note: The length of the deck of cards will always be an even number'''

string = input()
cards = string.split()
number_shuffles = int(input())

a = cards.pop(0)
b = cards.pop()
#print(a, b)

for shuffles in range(1,number_shuffles+1):

#print(cards)
    if shuffles==1:
        end_slice=len(cards)//2
        cards1=cards[0:end_slice]
        cards2=cards[end_slice:len(cards)+1]

        counter =0
        new_cards = [0]*(len(cards))
    else:
        end_slice = len(new_cards) // 2
        cards1 = new_cards[0:end_slice]
        cards2 = new_cards[end_slice:len(new_cards) + 1]

        counter = 0

    for i in range(0,len(cards),2):

         new_cards[i]=cards2[counter]
         new_cards[i+1]=cards1[counter]
         counter+=1
    #print(counter)
    #print(new_cards)

new_cards.insert(0, a) # add to the last element of the list
new_cards.append(b) # add to the last element of the list
print(new_cards)