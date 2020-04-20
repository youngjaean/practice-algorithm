
def dice():
    k = sorted(list(map(int, input().split())))
    if len(set(k)) == 1:
        return  50000 + (k[0]) * 5000
    elif len(set(k)) == 2:
        if k[1] == k[2]:
            return 10000 + (k[1]) * 1000
        else:
            return 2000 + (k[0]) * 500 + (k[3]) * 500
    
    for i in range(3):
        if k[i] == k[i+1]:
            return 1000 + (k[i]) * 100
    return max(k) * 100
    

print(max(dice() for i in range(int(input()))))