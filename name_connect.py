#https://www.acmicpc.net/problem/17269

n, m = int(input()), int(input())

A, B = input().split()

alpa =[3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2 ,1, 1, 1, 2, 2, 1]

AB = ''

min_len = min(A, B)
for i in range(min_len):
    AB += A[i] + B[i]
AB = A[min_len] + B[min_len]

lst = [alpa[ord(i) - ord('A')] for i in AB]


for i in range(A+B-2):
    for j in range(A+B-1-i):
        lst[j] += lst[j+1]


print("{}".format(lst[0] % 10 * 10 + lst[1] % 10))