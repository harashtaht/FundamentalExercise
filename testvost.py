# SOAL 1

# number = input("In: ")
# number = int(number)

# l = []
# # number = 4
# for i in range(1, number+1, 1):
#     var1 = [i]*i
#     l.append(var1)
# print(l)

# bar1 = []
# for loop in range(len(l)): #range(0,4,1) #0,1,2,3
#     for loop2 in range(0, loop+1):
#         bar1.append(l[loop][loop2])
# for loop in range(-2, -len(l)-1, -1): #0,-1,-2,-3
#     for loop2 in range(len(l[loop])):
#         bar1.append(l[loop][loop2])

# j = 0
# while j < number:
#     z = ''
#     for i in bar1:
#         if i == j or i <j:
#             z += '#'
#         elif i != j:
#             z += str(i)
#     j += 1
#     print(z)

# SOAL 2

# sentence2 = input('In: ')
kalimat = 'Saya beli 23 bungkus roti'

lsangka = []
lskal = []

for i in kalimat.split():
    if i.isdigit() == True:
        lsangka.append(int(i))
        lskal.append('temp1')
    else:
        lskal.append(i)

# print('lsangka', lsangka)
# print('lskalimat', lskal)


#### Testing --> Buat Function

# print(237/10) #23.7
# print(237%100) #37
num = 15234
numstr = str(num) # '15234'
numdiv = list(map(int, numstr)) # [1,5,2,3,4]

# print(numstr.split())
# print(list(map(int, numstr)))

dictNum = {}
numLoop = len(numstr)-1
for digits, unit in zip(numstr, numdiv):
    
    # newNum = num%(10**numLoop)
    # print(numLoop, newNum, numdiv)
    pangkat = 10**numLoop
    numLoop -= 1
    # dictNum[]
    



# transformNum = []

# for i in range(len(str(num)), 0, -1):
#     num0 = 0
#     num0 += num%10**i #[15234, 5234, 234, 34, 4]
#     # print(10**i)
#     # numAdd = num%10**i
#     transformNum.append(num0)


# print('transformNum : ', transformNum)

#capitalize

# print(15234//10)
# print(15234/10)
# print(15234%1000)

# SOAL 3
# numIn = input('In: ')
# numIn = numIn.lower()
# numIn = 'dua puluh tiga'
# numLs = numIn.split()
# # print(numLs)

# ### Reference for converting
# angkaNum = [i for i in range(1, 10)]
# angkaBet = ['satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
# dictAng = dict(zip(angkaBet, angkaNum))
# print(dictAng) #{'satu': 1, 'dua': 2, 'tiga': 3, 'empat': 4, 'lima': 5, 'enam': 6, 'tujuh': 7, 'delapan': 8, 'sembilan': 9}


# convertingNum = []
# origin = []

# # for i in numIn.split():
# for i in numLs:
#     indexNum = []
#     if i in dictAng:
#         convertingNum.append(dictAng[i])
#         origin.append('index: '+str(numLs.index(i)))
#     else:
#         origin.append(i)
#         # indexNum.append(i.index())
# print('convertingNum', convertingNum) #convertingNum [2, 3]
# print('original Sentence', origin) # original Sentence ['index: 0', 'puluh', 'index: 2']

# def find_between(s, start, end):
#   return (s.split(start))[1].split(end)[0]

# # print(find_between(numIn, 'dua', 'tiga'))

# lsPul = []
# puluhNum = [10**i for i in range(0, 10)]
# puluhBet = ['se', 'puluh', 'ratus', 'ribu', 'puluh ribu', 'ratus ribu', 'juta', 'puluh juta', 'ratus juta']
# dictPul = dict(zip(puluhBet, puluhNum))

# print(dictPul)