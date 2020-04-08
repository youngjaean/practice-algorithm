n = int(input())
count = 1
stack = []
reslut = []

for i in range(1, n + 1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        reslut.append("+")
    if stack[-1] == data:
        stack.pop()
        reslut.append('-')
    else:
        print('NO')
        exit(0)


print('\n'.join(reslut))
    
