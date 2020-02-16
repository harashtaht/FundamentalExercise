# No 4 - Python

def divisible(dictNum):
    results = 0
    cond1 = (1<=dictNum["A"]<=dictNum["B"]<10000)
    cond2 = (1<=dictNum["K"]<10000)
    if cond1 == True and cond2 == True:
        for i in range(dictNum["A"], dictNum["B"]+1):
            if i%dictNum["K"] == 0:
                results+=1
            else:
                results+=0
        return results
    else:
        return 0

# def divisible(dictNum):
#     results = 0
#     cond1 = (1<=dictNum["A"]<=dictNum["B"]<10000)
#     cond2 = (1<=dictNum["K"]<10000)
#     if cond1 == True and cond2 == True:
#         for i in range(dictNum["A"], dictNum["B"]+1):
#             if i%dictNum["K"].is_integer():
#                 results+=1
#             else:
#                 results+=0
#         return results
#     else:
#         return 0

test_A = input()
num_T = int(test_A)

cond_init = (1<=num_T<=100)

if cond_init==True:
    dictOutput = {}
    for i in range(1, num_T+1):
        dictNum = {}
        dictNum["A"] = int(input())
        dictNum["B"] = int(input())
        dictNum["K"] = int(input())
        dictOutput[i] = divisible(dictNum)
else:
    breakpoint

for i in range(1, len(dictOutput)+1):
    print(f'Case {i}: {dictOutput[i]}')

