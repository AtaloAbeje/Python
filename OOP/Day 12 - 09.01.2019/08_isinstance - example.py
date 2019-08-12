class Person:
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Animal:
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass


in_this_room=[Student(), Student(), Teacher(), Cat(), Dog(), Dog()]

people_in_this_room=0
animals_in_this_room=0

for x in range(0,len(in_this_room)):
    if isinstance(in_this_room[x],Person):
        people_in_this_room+=1
    elif isinstance(in_this_room[x],Animal):
        animals_in_this_room+=1

print("people_in_this_room",people_in_this_room)
print("animals_in_this_room",animals_in_this_room)


"""
OUTPUT:
______________________
people_in_this_room 3
animals_in_this_room 3
"""