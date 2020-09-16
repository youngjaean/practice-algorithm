
def segment(x, arr):
    k = []
    maximum = 0
    y = arr[0: x]
    y = min(y)
    if x == len(arr):
        return min(arr)
    for i in range(x, len(arr)):
        if x + i < len(arr):
            y = arr[i: x + i]
            y = min(y)
            if maximum < y:
                maximum = y
    return maximum


# import heapq
# def segment(x, arr):
#     k = []
#     if x == len(arr):
#         return min(arr)
#     for i in range(len(arr)):
#         if x + i < len(arr):
#             y = arr[i: x + i]
#             heapq.heapify(y)
#             k.append(y[0])
#     max_h = [(-ele) for ele in k]
#     heapq.heapify(max_h)
#     return -(max_h[0])

print(segment(1,[5, 1, 2, 3, 1, 2]))

