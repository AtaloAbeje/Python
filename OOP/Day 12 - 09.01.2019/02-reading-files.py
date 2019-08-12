#open file 
# r - read mode
# w - write mode
# a - append mode (append to the end of the file)
# r+ - read and write


# opens an exsiting file in read mode
# Note: if No such file or directory we get: FileNotFoundError
my_opened_file = open("myfile.txt", "r")


#is file readable (return boolean value)
print("readable:", my_opened_file.readable())

# get all the data from the file using read()
print("read:", my_opened_file.read())

#close the opened file
my_opened_file.close()
