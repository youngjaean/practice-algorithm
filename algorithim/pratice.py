# def qsort(data):
    # if len(data) <= 1:
    #     return data
    # pivot = data[0]

    # left = [item for item in data[1:] if pivot > item]
    # right = [item for item in data[1:] if pivot <= item]

    # return qsort(left) + [pivot] + qsort(right)

# def qsort(data):
#     if len(data) <= 1:
#         return data
#     pivot = data[0]

#     left = [item for item in  data[1:] if pivot > item ]
#     right = [item for item in data[1:] if pivot > item]

#     return qsort(left) + [pivot] + quit(right)


# def merge(left, right):
    # merged = list()
    # left_point, right_point = 0, 0
    
    # while len(left) > left_point and len(right) > right_point:
    #     if left[left_point] > right[right_point]:
    #         merged.append(right[right_point])
    #         right_point += 1
    #     else:
    #         merged.append(left[left_point])
    #         left_point += 1

    # while len(left) > left_point:
    #     merged.append(left[left_point])
    #     left_point += 1

    # while len(right) > right_point:
    #     merged.append(right[right_point])
    #     right_point += 1
    
    # return merged


# def mergesplit(data):
    # if len(data) <= 1:
    #     return data
    # medium = int(len(data) / 2)
    # left = mergesplit(data[:medium])
    # right = mergesplit(data[medium:])
    # return merge(left, right)


# def buble_sort(data):
    # for index in range(len(data) - 1):
    #     swap = False
    #     for index2 in range(len(data) - index - 1):
    #         if data[index2] > data[index2 + 1]:
    #             data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
    #             swap = True
    #     if swap == False:
    #         break
    # return data




def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]

    left = [item for item in  data[1:] if pivot > item ]
    right = [item for item in data[1:] if pivot > item]
    return qsort(left) + [pivot] + quit(right)


def bublesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data


def inser_sotr(data):
    for stand in range(len(data)):
        key = data[stand]
        for index in range(stand, 0, -1):
            if key < data[index - 1]:
                data[index - 1], data[index]  = data[index], data[index - 1]
    
    return data
            

def selectsort(data):
    for stand in range(len(data)):
        selce = stand
        for index in range(stand + 1, len(data)):
            if data[stand] > data[index]:
                stand = index
        
        data[stand], data[index] = data[index], data[stand]

    return data

def dfs(v):
    print(v, end=' ')
    visted[v] = True
    for e in adj[v]:
        if not visted[e]:
            dfs(e)
from collections import deque
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not visted[v]:
            visted[v] = True
            print(v, end = ' ')
            for e in adj[v]:
                if not visted[e]:
                    q.append(e)


        
n, m, v = map(int, input().split)
adj = [[] for _ in range(n + 1)]
visted = [False] * (n + 1)
import random

data_list = random.sample(range(100), 10)
print(inser_sotr(data_list))




# import sys

# n = int(sys.stdin.readline())

# array = [0] * 10001

# for _ in range(n):
#     data = int(sys.stdin.readline())
#     array[data] += 1


# for i in range(10001):
#     if array[i] != 0:
#         for j in range(array[i]):
#             print(i)


            
    

