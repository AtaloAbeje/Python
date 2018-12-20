class Student:
    sum_students = 0
    sum_age = 0
    sum_marks = 0

    def __init__(self, mark, age):
        self.mark = mark
        self.age = age
        Student.sum_students+=1            # summarize of students

        Student.sum_age += self.age        # summarize of age students
        Student.sum_marks += self.mark     # summarize of marks students

    @classmethod
    def avg_marks(class_level):
        print("avg marks students: {}".format(class_level.sum_marks / class_level.sum_students))

    @classmethod
    def avg_age(class_level):
        print("avg age students: {}".format(class_level.sum_age / class_level.sum_students))

# main()
s1 = Student(80 ,22) # list of students
s2 = Student(85, 23)
s3 = Student(90, 24)
s4 = Student(95, 25)

print("sum students:",Student.sum_students)
print("sum age students:",Student.sum_age)
print("sum marks students:",Student.sum_marks)
print("------------------------")
Student.avg_age()
Student.avg_marks()

'''
_________Output_________
sum students: 4
sum age students: 94
sum marks students: 350
------------------------
avg age students: 23.5
avg marks students: 87.5
'''
# task.03 Python - Atalo Abeje