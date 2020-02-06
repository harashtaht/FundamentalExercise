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
list_ = wordIn_.lower().split(' ')
list_1 = []

# print(list_)
#['Saya', 'beli', 'dua', 'puluh', 'tiga', 'bungkus', 'roti']


def numFind(list_):
    numDict = {'satu':1, 'dua':2, 'tiga':3, 'empat':4, 'lima':5, 'enam':6, 'tujuh':7, 'delapan':8, 'sembilan':9, 'sepuluh':10, 'sebelas':11}
    for i in list_:
        try:
            list_1.append(numDict[i])
        except:
            list_1.append(i)
            
    list_2 = []
    puluhDict = {'puluh':10, 'ratus':10**2, 'ribu':10**3, 'puluh ribu':10**4, 'ratus ribu':10**5, 'juta':10**6, 'puluh juta':10**7, 'ratus juta':10**8, 'milyar':10**9}
    
    for j in list_1:
        try:
            list_2.append(puluhDict[j])
        except:
            list_2.append(j)
    return list_2

# print(numFind(list_))
list_2 = ['saya', 'beli', 2, 10, 3, 'bungkus', 'roti']

for i in range(len(list_2)):
    # list_Kalimat = []
    # list_Angka = []
    # print(list_2[i])
    num = 0
    if type(list_2[i]) == int:
        # print(list_2[i])
        
        if list_2[i]%10 != 0:
            num += list_2[i]

        elif list_2[i]%10 == 0:
            num *= list_2[i]
        
        else:
            print(f'num = {num}')
        # print(f'{i} == integer')
        # if list_2[i]
        # list_Angka.append(i)
    else:
        continue
        # print(i)
        # continue
        # list_Kalimat.append(i)

# print(2%10)
# print(10%10)
# print(1000%10)

# print(list_Angka)
# print(list_Kalimat)

# def numLetter(list_2):
#     for i in list_2:
