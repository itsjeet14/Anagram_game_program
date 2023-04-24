import random
# creating list of words to create jumber word
words = ['aPple','banAna','hoRse']

# creating jumble word
word = random.choice(words).lower()
jumble = ''.join(random.sample(word, len(word)))

# chances to attempt
chance = 3
while chance != 0:
    print("Jumble Word: ",jumble)
    guess = input("Enter Answer: ").lower()
    if guess == word:
        print("Correct Answer!!")
        print()
        break
    else:
        chance -= 1
        print()
        print("Attempt left: ",chance)
     
else:
    print("You Lose!!")
    print("Correct Answer: ",word)
print()
print("Thank you for playing!")
