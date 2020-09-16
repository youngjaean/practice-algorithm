dice = sorted(list(map(int, input().split())))

if len(set(dice)) == 1:
    print(10000 + dice[0] * 1000)
elif len(set(dice)) == 2:
    print(1000 + dice[1] * 100)
else:
    print(dice[2] * 100)

