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

# import re

# def alphabetify(num):
#     number = ['', ' satu', ' dua', ' tiga', ' empat', ' lima', ' enam', ' tujuh', ' delapan', ' sembilan', ' sepuluh', ' sebelas']
#     result =""
#     n = int(num)
#     if n >= 0 and n <= 11:
#         result = result + number[n]
#     elif n < 20:
#         result = alphabetify(n % 10) + " belas"
#     elif n < 100:
#         result = alphabetify(n / 10) + " puluh" + alphabetify(n % 10)
#     elif n < 200:
#         result = " Seratus" + alphabetify(n - 100)
#     elif n < 1000:
#         result = alphabetify(n / 100) + " ratus" + alphabetify(n %100)
#     elif n < 2000:
#         result = " Seribu" + alphabetify(n-1000)
#     elif n < 1000000:
#         result = alphabetify(n / 1000) + " ribu" + alphabetify(n % 1000)
#     elif n < 1000000000:
#         result = alphabetify(n/1000000) + " juta" + alphabetify(n % 1000000)
#     else:
#         result = alphabetify(n / 1000000000) + " milyar" + alphabetify(n % 1000000000)
#     return result

# def num_str(str): 
#     array = re.findall(r'[0-9]+', str) 
#     return array 

# wordIn = input('In: ')
# list_ = wordIn.split(' ')
# list_1 = []

# for i in list_:
#     try:
#         list_1.append(alphabetify(*num_str(i))) 
#     except:
#         list_1.append(i)

# SOAL 3

# in_ = input('In: ')
in_ = 'Saya beli dua puluh tiga bungkus roti'

# def numerify(str):
#     number = ['', ' satu', ' dua', ' tiga', ' empat', ' lima', ' enam', ' tujuh', ' delapan', ' sembilan', ' sepuluh', ' sebelas']
#     result =""
#     n = int(num)
#     if n >= 0 and n <= 11:
#         result = result + number[n]
#     elif n < 20:
#         result = alphabetify(n % 10) + " belas"
#     elif n < 100:
#         result = alphabetify(n / 10) + " puluh" + alphabetify(n % 10)
#     elif n < 200:
#         result = " Seratus" + alphabetify(n - 100)
#     elif n < 1000:
#         result = alphabetify(n / 100) + " ratus" + alphabetify(n %100)
#     elif n < 2000:
#         result = " Seribu" + alphabetify(n-1000)
#     elif n < 1000000:
#         result = alphabetify(n / 1000) + " ribu" + alphabetify(n % 1000)
#     elif n < 1000000000:
#         result = alphabetify(n/1000000) + " juta" + alphabetify(n % 1000000)
#     else:
#         result = alphabetify(n / 1000000000) + " milyar" + alphabetify(n % 1000000000)
#     return result

wordIn_ = 'Saya beli dua puluh tiga bungkus roti'
list_ = wordIn_.split(' ')
list_1 = []

# print(list_)

# def separateNum(list):
#     for i in list:

for i in list_:
    try:
        list_1.append(alphabetify(*num_str(i))) 
    except:
        list_1.append(i)



# wordIn = input('In: ')
# list_ = wordIn.split(' ')
# list_1 = []

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


# buat fungsi untuk split per spasi
# dictionary angka
# dikali 10^^ sesuai len(num)
