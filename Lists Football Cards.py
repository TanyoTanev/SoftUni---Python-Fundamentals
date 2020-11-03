'''Most football fans love it for the goals and excitement. Well, this problem doesn't. You are to handle the referee's
little notebook and count the players who were sent off for fouls and misbehavior.

The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining, the game is stopped
immediately by the referee, and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g the card 'B-7'
means player #7 from team B received a card. (index 6 of the list)

The task: Given a list of cards (could be empty), return the number of remaining players on each team at the end of
the game in the format: "Team A - {players_count}; Team B - {players_count}". If the game was terminated print an additional line:
"Game was terminated"

Note for the random tests: If a player that has already been sent off receives another card - ignore it.

Input
The input (the cards) will come on a single line separated by a single space
Output
Print the remaining players as described above and add another line (as shown above) if the game was terminated
'''

#red_cards = input()


Team_A = []
Team_B = []

string = input()
red_cards = string.split( )


for i in range(0,11):
    Team_A.append("A-" + str(i+1))
    Team_B.append("B-" + str(i+1))

for i in range(len(red_cards)):
     card = red_cards[i]
     if card in Team_A :
       Team_A.remove(card)
     if card in Team_B :
       Team_B.remove(card)

#print(Team_A)
#print(Team_B)

print(f"Team A - {len(Team_A)}; Team B - {len(Team_B)}")
if len(Team_A) < 7 or len(Team_B) < 7:
    print(f"Game was terminated")