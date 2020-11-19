# Part 1

#input 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

n = int(input())
input1 = input()
input2 = input()
input3 = input()

def appendList(x):
    ls = []
    for i in x.split():
        ls.append(int(i))
    return ls

arr1 = appendList(input1)
arr2 = appendList(input2)
arr3 = appendList(input3)

toCount = []
toCount.append(arr1)
toCount.append(arr2)
toCount.append(arr3)

d1 = sum(toCount[x][x] for x in range(n))
d2 = sum(toCount[x][n-1-x] for x in range(n))

print(abs(d1-d2))