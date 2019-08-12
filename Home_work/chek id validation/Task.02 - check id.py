arr = input("Enter ur id number: ")
arr = [int(i) for i in arr] #convert to intger
brr = [1,2,1,2,1,2,1,2,1]
newarr = [0,0,0,0,0,0,0,0,0]

while len(arr) < 9 or len(arr) > 9: #Checkig if the ID number is 9 digits
    arr = input("ur id number invalid, try again: ")

for i in range(len(arr)):
    newarr[i] = arr[i] * brr[i]

for i in range(len(newarr)):
    if newarr[i] > 9:    #Checkig if value with 2 digits 
        sum1 = int(newarr[i] % 10)
        sum2 = int(newarr[i] / 10)
        newarr[i] = sum1 + sum2

sum1=0
for i in range(len(newarr)):
    sum1 += newarr[i]

if sum1 % 10 == 0:
    print("ur id is good!!")
else:
    print("ur id number invalid!")
## task.02 python - Atalo Abeje 
