def func(string, num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    copy_char = ""

    for char in string:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = int ((position + num) % 26)
            new_char = alphabet[new_position]
            print(char, "-->", new_char)
            copy_char = copy_char + new_char
        else:
            copy_char = copy_char + char
            print(char, "Not replaced")

    return copy_char

# main()
string = input("Enter string to encode: ")
num = int(input("Enter number for shifting: "))

result = func(string, num) 
print("ur new string is:\n",result)


print("----------break-code-caesar----------")
ciphertex = func(string, num)   #return ciphertex from function first

def caeser_break(ciphertex):
    for i in range(1,26): #
        maybe=func(ciphertex, i)
        print(i,".",maybe)

# main()
caeser_break(ciphertex) # send ciphertex to new function

# break caesar code - Atalo Abeje