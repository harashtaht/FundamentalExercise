# SOAL 1

number = input("In: ")
number = int(number)

l = []
# number = 4
for i in range(1, number+1, 1):
    var1 = [i]*i
    l.append(var1)
print(l)

bar1 = []
for loop in range(len(l)): #range(0,4,1) #0,1,2,3
    for loop2 in range(0, loop+1):
        bar1.append(l[loop][loop2])
for loop in range(-2, -len(l)-1, -1): #0,-1,-2,-3
    for loop2 in range(len(l[loop])):
        bar1.append(l[loop][loop2])

j = 0
while j < number:
    z = ''
    for i in bar1:
        if i == j or i <j:
            z += '#'
        elif i != j:
            z += str(i)
    j += 1
    print(z)

# SOAL 2

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

wordIn = input('In: ')
list_ = wordIn.split(' ')
list_1 = []

for i in list_:
    try:
        list_1.append(alphabetify(*num_str(i))) 
    except:
        list_1.append(i)

# SOAL 3

wordIn_ = input('In: ')
list_ = wordIn_.lower().split(' ')
list_1 = []

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

list_2 = numFind(list_)

list_Kalimat = []

num = 0
num_ = 0
for i in range(len(list_2)):
    if type(list_2[i]) == int and type(list_2[i+1]) != str:
        if (list_2[i]%10 !=0):
            num_ += list_2[i]

        elif (list_2[i]%10 ==0):
            num_ *= list_2[i]
            num = num+num_            
            num_ *= 0

    elif type(list_2[i]) == int and type(list_2[i+1]) == str:
        num += list_2[i]

    elif type(list_2[i-1]) == int and type(list_2[i] == str):
        list_Kalimat.append(num)
        list_Kalimat.append(list_2[i])
    
    elif type(list_2[i]) == str:
        list_Kalimat.append(list_2[i])

def makingSentence(list_Kalimat):
    result = ''
    for i in list_Kalimat:
        if type(i) == str:
            result += i + ' '

        elif type(i) == int:
            result += str(i) + ' '
    
    return print(result.capitalize())

makingSentence(list_Kalimat)