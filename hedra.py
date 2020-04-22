k = int(input())

for i in range(k):
    head = int(input())
    patten = input()
    for s in patten:
        if head == 0:
            head = 0
            break
        if s == 'c':
            head += 1
        elif s == 'b':
            head -= 1



    print("Data Set", i + 1,":")
    print(head)

        