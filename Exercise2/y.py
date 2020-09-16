# class Address():

#     def __init__(self, list):
#             self.first_name = list[0]
#             self.last_name = list[1]
#             self.number = list[2]

#     def log_data(self):
#         data_display = self.first_name + " " + self.last_name + " - " + self.number
#         # print(data_add) 
#         return data_display


input_ = 'Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001'

class PhoneBook():

    def __init__(self, message):
        self.sep1 = message.split(sep=';')
        list1 = []
        for i in self.sep1:
            _ = i.split(sep=',')
            list1.append(_)
            # print(list1)
        return list1
    
    def log_data(self):
        dictOutput = {}
        listTemp = []
        for i in self.list1:
            if i[2] not in listTemp:
                dictOutput[i] = "insert success"
            elif i[2] in listTemp:
                dictOutput[i] = "duplicate phone number"
            listTemp.append(i[2])
        print(dictOutput)

    # def separate(string):
    #     x = input_.split(sep=';')
    #     listReady = []
    #     for i in x:
    #         y = i.split(sep=',')
    #         listReady.append(y)
    #     return listReady

PhoneBook(input_).log_data()