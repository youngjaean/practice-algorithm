def splitIntoTwo(arr):
    count = 0
    left = 0
    right = sum(arr[0:])
    for i in range(len(arr) - 1):
        left += arr[i]
        right -= arr[i]
        if left > right:
            count +=1 
    return count


print(splitIntoTwo([10, 4, -8, 7]))