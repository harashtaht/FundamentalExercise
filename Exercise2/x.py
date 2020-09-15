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
    # listReady.append(tuple(y))
    listReady.append(y)
# print(listReady)
# ('Charlie', 'Zoe', '08123123123'), ('Andre', 'Xavier', '08111222333'), ('Charlie', 'Xyz', '08123123123'), ('Jean', 'Summers', '08001001001')]

# print(listReady[0][0])


class Address():

    def __init__(self, list):
            self.first_name = list[0]
            self.last_name = list[1]
            self.number = list[2]

    def show_input(self):
        data_add = self.first_name + " " + self.last_name + " - " + self.number
        print(data_add)

    
# Address(['Charlie', 'Zoe', '0812312312']).show_input()

for i in listReady:
    Address(i).show_input()


# class Address():

#     def __init__(self, first_name, last_name, number):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.number = number

#     def show_input(self):
#         data_add = self.first_name + " " + self.last_name + " - " + self.number
#         print(data_add)

#     def check_duplicate(self):
#         return None

# # Address('Charlie', 'Zoe', '08123123123').show_input()

# # for i in listReady:
# #     Address(i).show_input()
# #     # print(i)

# for i in x:
#     print(i.split(sep=','))
