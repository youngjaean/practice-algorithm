test_case = int(input())

for _ in range(test_case):
    letf_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if letf_stack:
                letf_stack.pop()
        elif i == '<':
            if letf_stack:
                right_stack.append(letf_stack.pop())
        elif i == '>':
            if right_stack:
                letf_stack.append(right_stack.pop())

        else:
            letf_stack.append(i)
    
    letf_stack.extend(reversed(right_stack))
    print(''.join(letf_stack))

