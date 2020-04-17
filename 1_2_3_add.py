#https://www.acmicpc.net/problem/9095
def cal(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return cal(n - 1 ) + cal(n - 2) + cal(n - 3)
    


t = int(input())

for _ in range(t):
    n = int(input())
    print(cal(n))
