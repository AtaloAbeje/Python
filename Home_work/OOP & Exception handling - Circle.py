import math
class Circel(Exception):

    def __init__(self, radius):
        Exception.__init__(self)
        self.radius = radius
try:
    radius = int(input("Enter radius of circel: "))
    if radius < 0:
        raise Circel(radius)

except Circel:
    print("non valid input - because input is less than 0 number")

else:
    print("Circle has created!!\nArea circle: " + str(math.pi * pow(radius, 2)))
    print("Scope circle: " + str(2 * math.pi * radius))

print("End of app")