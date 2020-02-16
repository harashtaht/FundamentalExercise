# A = int(input("A : "))
# B = int(input("B : "))
# K = int(input("K : "))

# cond1 = (1<=A<=B<10000)
# cond2 = (1<=K<10000)

# if cond1 == True and cond2 == True:
#     results = 0
#     for i in range(A, B+1, 1):
#         if i%K == 0:
#             results +=1
#             print('i = ', i, 'results =', results)
#         else:
#             continue

# print('results = ',results)

results = 0
for i in range(1,11,1):
    print(f'for number = {i} results= {i/3} type= {type(i/3)}')
    if (i/3).is_integer():
        results += 1
        print(i/3, (i/3).is_integer())
    else:
        results += 0

print(float(2.66))
# print(3%3)
# print(6%3)
print(9%3)


# A : 281
# B : 9155
# K : 91

# 364 1
# 455 2
# 546 3
# 637 4
# 728 5
# 819 6
# 910 7
# 1001 8

# print(364%91)
# print(455%91)
# print(546%91)
# print(637%91)
# print(728%91)
# print(819%91)
# print(910%91)
# print(1001%91)

# 6734 71
# 6825 72
# 6916 73
# 7007 74
# 7098 75
# 7189 76
# 7280 77
# 7371 78
# 7462 79
# 7553 80


# print(6734%91)
# print(6735%91)
# print(6736%91)
# print(6825%91)
# print(6916%91)
# print(7007%91)
# print(7098%91)
# print(7189%91)
# print(7280%91)
# print(7371%91)
# print(7462%91)
# print(7553%91)