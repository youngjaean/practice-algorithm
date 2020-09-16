
timstamp = [0, 1, 1, 2, 4, 5]
top = [5]

def requestsServed(timestamp, top):
    count = 0
    index = 0
    timestamp.sort()
    top.sort()
    while index < len(top):
        i = 0
        fir = timestamp[:5]

        while i < len(fir):
            if top[index] > timestamp[0]:
                count += 1
                timestamp.pop(0)
            i += 1
        index += 1
        
    if count == 0:
        return 1

    return count



