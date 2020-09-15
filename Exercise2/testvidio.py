### Number 1 ###

# Example
# displayMulti("Jakarta", 2) --> JakJak
# displayMulti("Jakarta", 3) --> JakJakJak
# displayMulti("BBM", 2) --> BBMBBM
# displayMulti("Or", 3) --> rOrOrO

# def displayMulti(string, num):
#     output = ""
#     if len(string) >= 3:
#         output += (string[:3]*num)
#     else:
#         output += (string[::-1]*num)
#     print(output)

# displayMulti("Jakarta", 2)
# displayMulti("Jakarta", 3)
# displayMulti("BBM", 2)
# displayMulti("Or", 3)


### Number 2 ###
# '''
# Input:
# Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001

# Output:
# === Output START ===
# Log:
# Charlie Zoe – 08123123123 : insert success
# Andre Xavier – 08111222333 : insert success
# Charlie Xyz – 08123123123 : duplicate phone number
# Jean Summers – 08001001001 : insert success
# '''

inp = "Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001"

addressbook = []
for i in inp.split(sep=";"):
    _ = ()
    # print(i)
    # _.append(i)
    # addressbook.append(_)
    addressbook.append(i)

# print(addressbook)

# for i in addressbook:
#     # print(type(i.split(sep=",")))
#     print(i.split(sep=","))


# print(addressbook[0]) #['Charlie,Zoe,08123123123']
# print(len(addressbook)) #4

# for i in addressbook[0].split(sep=","):
#     print(i)

# for i in addressbook[0]:
#     # print(type(i))
#     print(i)

# Cari threshold untuk check nomor sudah di input (duplikat)


# Class untuk display Log
# insert success/duplicate phone number not done

list = ["Charlie,Zoe,08123123123"]

class Address():

    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    def show_input(self):
        data_add = self.first_name + " " + self.last_name + " - " + self.number
        print(data_add)

    def check_duplicate(self):
        return None

# Address('Charlie', 'Zoe', '08123123123').show_input()

inp = "Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001"

list = []
for i in inp.split(sep=';'):
    mylist = []
    mylist.append(i)
    mytuple = tuple(mylist)
    list.append((mytuple))
# print(list)
# [('Charlie,Zoe,08123123123',), ('Andre,Xavier,08111222333',), ('Charlie,Xyz,08123123123',), ('Jean,Summers,08001001001',)]()tuplenew = {}
