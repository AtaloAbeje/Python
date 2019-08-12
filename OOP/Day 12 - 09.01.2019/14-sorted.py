# Note: by default "sorted" works by comparing 2 elements with  '<'

# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)   # --> [-10, -2, 0, 1, 12, 15]

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))  # --> ['Jerry', 'Linda', 'Sue']
print(sorted(["Sue", "jerry", "linda"]))  # --> ['Sue', 'jerry', 'linda']

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))  #--> ['child', 'favorite', 'is', 'Linda', 'My']
print(sorted(pointsInaGame, reverse=True))  # --> [15, 12, 1, 0, -2, -10]



