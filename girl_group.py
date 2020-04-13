#https://www.acmicpc.net/problem/16165

n, m  = map(int, input().split())
group_dict, mem_dict = {}, {}
for i in range(n):
    team_name, team_num = input(), int(input())
    group_dict[team_name] = []
    for j in range(team_num):
        value = input()
        group_dict[team_name].append(value)
        mem_dict[value] = team_name


for _ in range(m):
    name =  input()
    group_mem = int(input())
    if group_mem == 1:
        print(mem_dict[name])
    elif group_mem == 0:
        for mem in sorted(group_dict[name]):
            print(mem)