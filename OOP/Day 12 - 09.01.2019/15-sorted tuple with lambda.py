students = [ ('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]




#sort by the first entry in each tuple (this is default sorting)
print(sorted(students))
# --> [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]


#sort by the first entry in each tuple i.e. sort by student name
print(sorted(students, key=lambda student:student[0]))  
# --> [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]


#sort by the second entry in each tuple i.e. sort by student grade
print(sorted(students, key=lambda student:student[1]))  
# --> [('eliza', 'A', 16), ('alice', 'B', 12), ('tae', 'C', 15)]

#sort by the third entry in each tuple i.e. sort by student marks
print(sorted(students, key=lambda student:student[2]))  
# --> [('alice', 'B', 12), ('tae', 'C', 15), ('eliza', 'A', 16)]