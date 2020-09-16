document = input()
word = input()
count = 0
index = 0
while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        count += 1
        index += len(word)
    else:
        index += 1



print(count)        