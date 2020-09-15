# input_ = input()
input_ = 'Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001'

# Separate string into 4 strings, separated by ";" into List
x = input_.split(sep=';')
# print(x)
# ['Charlie,Zoe,081028302131', 'Andre,Xavier,09810382013812', 'Charlie,Xyz,081818182', 'Jean,Summer,292929292']

# Separate into tuples for Class()
# 4 Tuples inside a List
listReady = []
for i in x:
    y = i.split(sep=',')
    listReady.append(y)
# print(listReady)
# [['Charlie', 'Zoe', '08123123123'], ['Andre', 'Xavier', '08111222333'], ['Charlie', 'Xyz', '08123123123'], ['Jean', 'Summers', '08001001001']]

class Address():

    def __init__(self, list):
            self.first_name = list[0]
            self.last_name = list[1]
            self.number = list[2]

    def log_data(self):
        data_display = self.first_name + " " + self.last_name + " - " + self.number
        # print(data_add) 
        return data_display

dictOutput = {}
listTemp = []
for i in listReady:
    if i[2] not in listTemp:
        dictOutput[Address(i).log_data()] = "insert success"
    elif i[2] in listTemp:
        dictOutput[Address(i).log_data()] = "duplicate phone number"
    listTemp.append(i[2])

print(dictOutput)
