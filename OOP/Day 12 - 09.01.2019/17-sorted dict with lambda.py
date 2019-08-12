students = [{"name":"Alice","age": 100},{"name":"Bob","age": 20}]


print(students)
# --> [{'name': 'Alice', 'age': 100}, {'name': 'Bob', 'age': 20}]


# Note: by default "sorted" works by comparing 2 elements with  '<'
# So, "sorted"  returns TypeError when we try to run it on dict array
# because '<' not supported between instances of 'dict' and 'dict'

# The solution how to sort this dict array - is to add a lambda
# that runs the comparing 2 elements with  '<' - to a specific part in the dict

print(sorted(students, key=lambda student:student["age"])) 
# --> [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 100}]

print(sorted(students, key=lambda student:student["name"])) 
# --> [{'name': 'Alice', 'age': 100}, {'name': 'Bob', 'age': 20}]
