
def func1():
    pass

print(type(10))             # --> <class 'int'>
print(type('a'))            # --> <class 'str'>
print(type("Hi there"))     # --> <class 'str'>
print(type([1,2,3]))        # --> <class 'list'>
print(type({"name":"Bob"})) # --> <class 'dict'>
print(type(True))           # --> <class 'bool'>
print(type(3.4))            # --> <class 'float'>
print(type(None))           # --> <class 'NoneType'>
print(type(func1()))        # --> <class 'NoneType'>
print(type(func1))          # --> <class 'function'>