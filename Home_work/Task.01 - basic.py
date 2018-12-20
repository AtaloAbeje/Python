num = int (input("enter a number: "))
sum = 0
ahadot = 0
asarot = 0
meot = 0

if num >= 0 and num <= 999: #check if num between 0 and 999 (until 3 digits)
    if num >= 0 and num <= 9: # check if num between 0 - 9 // ahadot
        if num == 0: 
            print("zero")
        if num == 1:
            print("one")
        if num == 2:
            print("tow")
        if num == 3:
            print("three")
        if num == 4:
            print("four")
        if num == 5:
            print("five")
        if num == 6:
            print("six")
        if num == 7:
            print("seven")
        if num == 8:
            print("eight")      
        if num == 9:
            print("nine")

    elif num >= 10 and num <= 99:
        sum = int (num / 10 ) + int (num % 10)
        print(num, "is 2 digits number, sum is", sum)

    if num >= 100 and num <= 999:
        ahadot = int (num % 10)
        asarot = int ((num / 10) % 10)
        meot = int (num / 100)
        print(num, "is 3 digits number, mul is", (meot * asarot) * ahadot) #(2 * 3) * 4
else:
    print(num, "number has more than 3 digits")       
## task.01 python - Atalo Abeje