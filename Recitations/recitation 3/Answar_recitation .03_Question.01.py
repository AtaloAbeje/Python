def reverse_num(num):
        tmp = 0
        while num > 0:
                ezer = num % 10
                tmp = (tmp * 10) + ezer
                num = num // 10
        return tmp

def is_palindrom_num(num, rev):
        if (rev == num):
                print("is palindrom number!")
        else:
                print("is NOT palindrom number!")

num = int(input("Enter number for revers: "))
rev = reverse_num(num)
print("revers number:",rev)
is_palindrom_num(num, rev)

# pec.03 Answar 1 # Atalo Abeje