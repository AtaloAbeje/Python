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


string = input("Enter string to encode: ")
num = int(input("Enter number for shifting: "))

result = func(string, num) 
print(result)

# String encryption using cipher Caesar