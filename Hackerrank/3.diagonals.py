# Part 1

#input 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# n = int(input())

# toCount = [list(int(x) for x in input().split()) for i in range(n)]

# def diagonalDifference(list):
#     d1 = sum(list[x][x] for x in range(n))
#     d2 = sum(list[x][n-1-x] for x in range(n))
#     result = abs(d1-d2)
#     return result

# print(diagonalDifference(toCount))

# Part 2: ratio of integers

# input : 5
# input2 : 1 1 0 -1 -1

# n = int(input())

# arr = list(map(int, input().split()))

# def plusMinus(list):
#     positive = 0
#     negative = 0
#     zeros = 0
#     for i in range(len(list)):
#         if list[i] > 0:
#             positive += 1
#         elif list[i] <0:
#             negative += 1
#         else:
#             zeros += 1
#     pos = positive/len(list)
#     neg = negative/len(list)
#     zer = zeros/len(list)
#     print(f'{pos:.6f}')
#     print(f'{neg:.6f}')
#     print(f'{zer:.6f}')

# plusMinus(arr)

# Part 3: Staircase

# n = int(input())

# for i in range(n):
#     num = ''
#     num += ' '*(n-i-1)
#     num += '#'*(i+1)
#     print(num)

# Part 4: Mini-Max Sum

# in: 1 3 5 7 9
# out: 16 24
# in : 1 2 3 4 5
# out : 10 14

# nums = [int(x) for x in input().split()]
# print(sum(nums)-max(nums), sum(nums)-min(nums))


# Part 5: Birthday Cake Candles

# in: 4
# in: 3 2 1 3
# out: 2

# n = int(input())
# candles = list(map(int, input().split()))
# print(candles.count(max(candles)))


# Part 6: Time Conversion

# in: 07:05:45PM
# out: 19:05:45

inp = input()

def timeConversion(inp):
    if (inp[-2:]=="PM") and int(inp[:2])!=12:
        out = str(int(inp[:2])+12)+inp[2:-2]
    elif (inp[-2:]=="PM") and int(inp[:2])==12:
        out = inp[:-2]
    elif (inp[-2:]=="AM") and int(inp[:2])==12:
        out = str(int(inp[:2])-12)+"0"+inp[2:-2]
    else:
        out = inp[:-2]
    print(out)

timeConversion(inp)

# test = ["07:05:45PM","07:05:45AM", "12:05:45PM", "12:05:45AM"]
# for i in test:
#     print(i, "  =   ", timeConversion(i))