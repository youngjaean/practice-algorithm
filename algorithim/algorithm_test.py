#https://www.acmicpc.net/problem/17389

# n = int(input())
# correct = input()
# score, k = 0, 0
# bonus = False

# for idx, OX in enumerate(correct):
#     if OX == 'O':
#         score += idx + 1
#         if bonus:
#             score += k
#             k += 1
#         else:
#             bonus = True
#             k += 1
#     else:
#         bonus = False
#         k = 0

N, S = int(input()), input()
score, bonus = 0 , 0

for idx, OX in enumerate(S):
    if OX == 'O':
        score += idx + 1 + bonus
        bonus += 1
    else:
        bonus = 0
print(score)

