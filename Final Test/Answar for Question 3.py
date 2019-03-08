def get_index(arr, num):
    index = []
    first = -1
    second = -1
    i = 0

    while i < len(arr): # Search from the beginning of the array
        if arr[i] == num:
            first = i
            break
        i+=1
    
    i = len(arr)-1      # Search from the end of the array
    while i >= 0:
        if arr[i] == num:
            second = i
            break
        i-=1

    if first != -1:     # If the number is in the array, add the first index and second index of the number to a new list
        index.append(first)
        index.append(second)
    else:
        index.append(first)
        index.append(second)
   
    return index

# main()
arr = [5,7,7,8,5,6,10]
num = 5

print(get_index(arr, num))

''' OUTPUT:
arr = [5,7,7,8,8,6,10]
num = 4:
[-1, -1]
-----

arr = [5,7,7,8,5,6,10]
num = 5:
[0, 4]
'''

