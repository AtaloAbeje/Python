# Random Module
import random

# Random Numbers
print(random.random())   # --> 0.18293170298474837

# Random Numbers IN RANGE
print("You rolled a " + str(random.randrange(1, 7)))  # --> You rolled a 5

# Random Choices 
lotteryWinners = random.sample(range(5), 2)
print(lotteryWinners)                      # --> [3, 4]


# Random Choice from an array
possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))         # --> cat


# Random shuffle an array
cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)                               # --> ['Ace', 'Jack', 'Queen', 'King']