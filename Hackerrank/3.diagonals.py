# Part 1

#input 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

n = int(input())

toCount = [list(int(x) for x in input().split()) for i in range(n)]

def diagonalDifference(list):
    d1 = sum(list[x][x] for x in range(n))
    d2 = sum(list[x][n-1-x] for x in range(n))
    result = abs(d1-d2)
    return result

print(diagonalDifference(toCount))

# Part 2: ratio of integers

# n = int(input())

# arr = input()
# arr1 = [list(int(x) for x in arr.split())]
# # list = []
# # arr1 = [list.append(i) for i in arr.split()]
# print(arr1)