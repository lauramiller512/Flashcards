import os, sys, random

# This is looping through all the words in my flashcards list
def print_card(card):
    for word in card:
        print (word, "      ",)
    print ("")

print ("Flash card script version 0.3 by Akkana Peck.\n")
print ("On seeing a word, think of the answer then hit return.")
print ("Then hit return again to see the next word.")
print ("But if you got it wrong, type anything besides q before hitting Return")
print ("and the word will be added to a list to be presented more often.")
print ("q<Return> quits.")
print ("")

# If there are more than 1 cardset in the flashcards folder
if len(sys.argv) > 1 :
    cardset = sys.argv[1]
    print ("Using cards from set '" + cardset + "'")
else :
    cardset = "all"

cardfile = os.path.join(os.path.expanduser("~"), ".flashcards", cardset)
if (os.path.exists(cardfile)) :
    exec(open(cardfile))
else :
    cardfile = os.path.join(os.path.expanduser("~"), "flashcards", cardset)
    if (os.path.exists(cardfile)) :
        exec(open(cardfile))

# Need to define cards properly!
def missed_cards(cards):   
    while True :
        card = random.choice(cards)
        which = random.choice(card)

        print (which),
        if input() == "q" :
            break
        print_card(card)

        ans = input()
        if ans == "q" :
            break
        if ans != "" :
    #         # Save another copy of this word in the list
            cards.append(card)

# If the length of cards is greater than 0
if len(cards) > 0 :
    print ("Read", len(card), "cards from", cardfile)

    print ("")

bonus_words = len(cards)

# Print the ones missed
print ("\nMissed:")
for card in cards[bonus_words:] :
    print_card(card)
