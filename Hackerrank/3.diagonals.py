# Part 1

input_a = int(input())
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

num1 = 0
for j in range(len(toCount)):
    num1 += toCount[j][j]

num2 = 0
for j in range(len(toCount)):
    num2 += toCount[j][input_a-1-j]

print(abs(num1-num2))