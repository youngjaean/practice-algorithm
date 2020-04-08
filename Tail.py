n = int(input())

first = 0
sec = 1
for _ in range(n):
    first, sec = sec, first + sec

print(sec % 15746 )

