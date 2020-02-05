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
numdiv = list(map(int, numstr)) # [1,5,2,3,4] #type = integers

# print(numstr.split())
# print(list(map(int, numstr)))

dictNum = {}
numLoop = len(numstr)-1
for digits in numdiv:
    dictNum[digits] = 10**numLoop
    numLoop -=1

belas = []
lainnya = []

# print(dictNum)

for i in dictNum:
    # print(i, dictNum[i], i*dictNum[i])
    cond1 = (dictNum[i] == 10000 or dictNum[i] == 10) and (i == 1)
    if cond1 == True:
        belas.append(i)
    # elif:
    #     continue 
    else:
        lainnya.append(i)


def alfabetanum(dict):
    output = []
    dictAlfa = {
        1: 'satu', 2: 'dua', 3: 'tiga', 4: 'empat', 5: 'lima', 
        6: 'enam', 7: 'tujuh', 8: 'delapan', 9: 'sembilan', 
        10**6 : 'juta', 10**5: 'ratus ribu', 10**4: 'puluh ribu',
        10**3 : 'ribu', 10**2: 'ratus', 10: 'puluh'}
    for i in dict:
        output.append(dictAlfa[i])
        output.append(dictAlfa[dictAlfa[i]])

# for i in dictNum:
#     print(i)

output= []
dictAlfa = {
    1: 'satu', 2: 'dua', 3: 'tiga', 4: 'empat', 5: 'lima', 
    6: 'enam', 7: 'tujuh', 8: 'delapan', 9: 'sembilan', 
    10**6 : 'juta', 10**5: 'ratus ribu', 10**4: 'puluh ribu',
    10**3 : 'ribu', 10**2: 'ratus', 10: 'puluh'}
for i in dictNum:
    output.append(dictAlfa[i])
    output.append(dictAlfa[dictNum[i]])

# print(output)
# ['satu', 'puluh ribu', 'lima', 'ribu', 'dua', 'ratus', 'tiga', 'puluh', 'empat', 'satu']
# dibagi per 3 angka


# print(list(enumerate(dictNum)))

# for index, (key, value) in enumerate(dictNum.items()):
#     # print(index, key, value)
#     cond1 = (dictNum[key] == 10000 or dictNum[key] == 10) and (key == 1)
#     if cond1 == True:
#         idx = index+1
#         belas.append(key)
        
#         # print(index, key, value)
#     # elif 
#     else:
#         lainnya.append(key)

# print(belas)
# print(lainnya)

# transformNum = []

# for i in range(len(str(num)), 0, -1):
#     num0 = 0
#     num0 += num%10**i #[15234, 5234, 234, 34, 4]
#     # print(10**i)
#     # numAdd = num%10**i
#     transformNum.append(num0)


# print('transformNum : ', transformNum)

##### cara Mila
import re

def alphabetify(num):
    number = ['', ' satu', ' dua', ' tiga', ' empat', ' lima', ' enam', ' tujuh', ' delapan', ' sembilan', ' sepuluh', ' sebelas']
    result =""
    n = int(num)
    if n >= 0 and n <= 11:
        result = result + number[n]
    elif n < 20:
        result = alphabetify(n % 10) + " belas"
    elif n < 100:
        result = alphabetify(n / 10) + " puluh" + alphabetify(n % 10)
    elif n < 200:
        result = " Seratus" + alphabetify(n - 100)
    elif n < 1000:
        result = alphabetify(n / 100) + " ratus" + alphabetify(n %100)
    elif n < 2000:
        result = " Seribu" + alphabetify(n-1000)
    elif n < 1000000:
        result = alphabetify(n / 1000) + " ribu" + alphabetify(n % 1000)
    elif n < 1000000000:
        result = alphabetify(n/1000000) + " juta" + alphabetify(n % 1000000)
    else:
        result = alphabetify(n / 1000000000) + " milyar" + alphabetify(n % 1000000000)
    return result

def num_str(str): 
    array = re.findall(r'[0-9]+', str) 
    return array 

# wordIn = input('In: ')
wordIn = 'Saya membeli 2319 bungkus roti'
list_ = wordIn.split(' ')
list_1 = []

# for i in list_:
#     try:
#         list_1.append(alphabetify(*num_str(i))) 
#     except:
#         list_1.append(i)

# print(num_str('Saya membeli 2319 bungkus roti'))

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