import math
class Square(Exception):

    def __init__(self, rib):
        Exception.__init__(self)
        self.rib = rib
try:
    rib = int(input("Enter rib squarel: "))
    if rib < 0:
        raise Square(rib)
except Square:
    print("non valid input - because input is less than 0 number")

else:
    print("Square has created!!\nArea Square: " + str(pow(rib, 2)))
    print("Scope Square: " + str(rib * 4))

print("End of app")