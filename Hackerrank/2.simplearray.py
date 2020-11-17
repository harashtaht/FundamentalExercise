# ## Part 1 ##

# b = input()
# b = int(b)

# if (b<0) or (b > 1000):
#     print("Constraints must be more than 0 or less than equal of 1000. Please enter another number.\n")
#     b = input()
# else:
#     a = input()

# ls = []
# for i in a.split():
#     ls.append(int(i))

# results = 0
# for i in ls:
#     results += i

# print(results)

# Part 2

# def appendList(x):
#     ls = []
#     for i in x.split():
#         ls.append(int(i))
#     return ls

# a = input()
# b = input()
# a = appendList(a)
# b = appendList(b)

# def compareTriplets(a,b):
#     num_a = 0
#     num_b = 0
#     for i in range(len(a)):
#         if a[i] > b[i]:
#             num_a += 1
#         elif b[i] > a[i]:
#             num_b += 1
#         else:
#             num_a += 0
#             num_b += 0
#     str = f'{num_a} {num_b}'
#     return str

# results = compareTriplets(a,b)
# print(results)

# Part 3
x = "1000000001 1000000002 1000000003 1000000004 1000000005" #input2
y = int("5") #input1

def appendList(x):
    ls = []
    for i in x.split():
        ls.append(int(i))
    return ls

listNum = appendList(x)

num = 0
for i in range(y):
    num += listNum[i]
print(num)

#Tinggal buat function