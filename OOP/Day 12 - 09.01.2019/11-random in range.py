# Random Module
import random

# Random Numbers (gives a value between 0-1)
rnd=random.random()
maximum=8
minimum=3

rnd_in_rang=int(rnd*(maximum-minimum)) + minimum


print(rnd_in_rang)