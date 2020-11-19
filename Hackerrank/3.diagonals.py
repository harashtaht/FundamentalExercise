# Part 1

# input_a = 3
input1 = "11 2 4"
input2 = "4 5 6"
input3 = "10 8 -12"

def appendList(x):
    ls = []
    for i in x.split():
        ls.append(int(i))
    return ls

# print(appendList(input1))
# print(appendList(input2))
# print(appendList(input3))

arr1 = appendList(input1)
arr2 = appendList(input2)
arr3 = appendList(input3)

toCount = []
toCount.append(arr1)
toCount.append(arr2)
toCount.append(arr3)
print(toCount)

#range() arr[0][0] + arr[1][1] + arr[2][2]
# arr[0][-1] + arr[0][-2] + arr[0][-3]  / arr[0][2] + arr[0][1] + arr[0][0]