students = [ ('alice', 100, 80), ('tae', 100, 95), ('eliza', 100, 70)]



#sort by the first entry in each tuple
print(sorted(students))
# --> [('alice', 100, 80), ('eliza', 100, 70), ('tae', 100, 95)]



# sort by the differnce between "second entry" and "third entry"
print(sorted(students, key=lambda student:student[1]-student[2])) 
# --> [('tae', 100, 95), ('alice', 100, 80), ('eliza', 100, 70)]
