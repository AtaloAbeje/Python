#open file 
# r - read mode
# w - write mode
# a - append mode (append to the end of the file)
# r+ - read and write

# create a new file (if file does not exist) in append mode
my_opened_file = open("myfile.txt", "a")
# add a new line in the file
my_opened_file.write("\ntest me") 
my_opened_file.close()


# create a new file (if file does not exist) in write mode
my_new_file = open("my_new_file", "w")
# add contents to new file, if file exists it will overwrite its contents
my_new_file.write("my new content")
my_new_file.close()