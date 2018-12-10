def func(lst1, lst2,lst3,size1, size2):
    j=0
    if size1 != size2:
        return False
    else:
        for i in range(size1):
            for j in range(size2):
                if lst1[i] == lst2[j]:
                    lst3.append(j)
        return lst3

lst1 = [4,2,8,3]
lst2 = [2,4,3,8]
lst3 = []

size1 = len(lst1)
size2 = len(lst2)

res = func(lst1, lst2, lst3, size1, size2)
print(res)

# pec.03 Answar 4 # Atalo Abeje