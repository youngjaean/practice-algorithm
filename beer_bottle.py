n = int(input())


for k in range(n, 0, -1):
    if k > 1:
        print(f"""{k} bottles of beer on the wall, {k} bottles of beer.
Take one down and pass it around, {k - 1} bottles of beer on the wall.""")
    elif k == 1:
        print("""1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.""")
    print()
print(f"""No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {n} bottles of beer on the wall.""")
