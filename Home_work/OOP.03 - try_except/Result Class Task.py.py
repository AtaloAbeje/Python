import random

class Person(Exception):
    def __init__(self, name = "", age = "", eye_color = ""):
        Exception.__init__(self)
        self.name = name
        self.age = age
        self.eye_color = eye_color

    def set_name(self, name):
        try:
            pass
            if len(name) < 3:
                raise Person(len(name), 3)

            if len(name) > 9:
                raise Person(len(name), 9)

        except Person as my_ex_name:
            if len(name) < 3:
                print("non-valid name! Short input - your input is less than 3 chars: ", my_ex_name.name)
            if len(name) > 9:
                print("non-valid name! Long input - your input is more than 9 chars: ", my_ex_name.name)   
        else:
            print("valid name: ", name)

    def set_age(self, age):
        try:
            if age < 0:
                raise Person(age)
            if age > 120:
                raise Person(age)

        except Person as my_ex_age:
            print("non-valid age", my_ex_age.age)
            
        else:
            print("valid age: ", age)

    def set_eye_color(self, eye_color):
        try:
            if eye_color not in ["green", "brown", "blue"]:
                raise Person(eye_color)

        except Person as my_ex_eye_color:
            print("non-valid color!", my_ex_eye_color)
        else:
            print("valid eye color: ", eye_color)

# main()-----------------------
names = ["Tom", "li" , "Bob" , "Alice" , "Clarc" , "Adam" , "Sean"]
colors = ["green", "blue" , "yellow" , "black" ]

for i in range(0, 5):
    Person().set_name(random.choice(names))         # send to the function set_name random name
    Person().set_age(random.randint(-20, 200))      #  send random number to the function set_age
    Person().set_eye_color(random.choice(colors))   # send random color to the function set_eye_color
    print("-------------------")
    
'''
__________________________OUTPUT:____________________________
valid name:  Clarc
valid age:  40
valid eye color:  green
-------------------
valid name:  Sean
valid age:  116
valid eye color:  green
-------------------
non-valid name! Short input - your input is less than 3 chars:  2
valid age:  67
non-valid color!
-------------------
''' 
