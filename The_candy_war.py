#https://www.acmicpc.net/problem/9037

def check(N, candy):
    for i in range(N):
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1 # 다같으면 candy 길이가 1이됨

def teacher (N, candy):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx+1) % N] = candy[idx]
    
    for idx in range(N):
        candy[idx] += tmp_lst[idx] #오른쪽으로 분배 

    return candy

def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt) 

for i in range(int(input())):
    process()