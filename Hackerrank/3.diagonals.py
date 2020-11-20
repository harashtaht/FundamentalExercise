# Part 1

#input 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

n = int(input())

toCount = []
for i in range(n):
    i = input()
    ls = []
    for x in i.split():
        ls.append(int(x))
    toCount.append(ls)

def diagonalDifference(list):
    d1 = sum(list[x][x] for x in range(n))
    d2 = sum(list[x][n-1-x] for x in range(n))
    result = abs(d1-d2)
    return result

print(diagonalDifference(toCount))