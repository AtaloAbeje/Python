#type does not account for inheritance
#isinstance accounts for inheritance

"""
isinstance - is a function that gets 2 parameters:
    1) an object
    2) a class
The function returns:
    - True - if the object is instance of this class or a sub-class
    - False - if the object is not an instance of this class or a sub-class
"""
class Car:
    pass

class MiniCar(Car):
    pass

class Truck():
    pass

c1 = Car()
c2 = Car()
m = MiniCar()
t = Truck()
print(type(c1))                     # --> <class '__main__.Car'>
print(type(t))                      # --> <class '__main__.Truck'>
print(type(m))                      # --> <class '__main__.MiniCar'>
print(type(c1) == type(t))          # --> False
print(type(c1) == type(c2))         # --> True
print(type(c1) == type(m))          # --> False

print(isinstance(c1, Car))          # --> True
print(isinstance(m, Car))           # --> True
print(isinstance(t, Car))           # --> False


