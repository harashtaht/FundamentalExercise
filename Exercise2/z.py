def separate(string):
    x = input_.split(sep=';')
    listReady = []
    for i in x:
        y = i.split(sep=',')
        listReady.append(y)
        dictOutput = {}
        listTemp = []   
        for i in listReady:
            if i[2] not in listTemp:
                dictOutput[Address(i).log_data()] = "insert success"
            elif i[2] in listTemp:
                dictOutput[Address(i).log_data()] = "duplicate phone number"
            listTemp.append(i[2])
    for key, val in dictOutput.items():
                print(key, ':', val)
    print("Phone book:")
    listOutput = []
    for key, val in dictOutput.items():
        if val == "insert success":
            listOutput.append(key)
    for i in range(len(listOutput)):
        print(f"{i+1}. {listOutput[i]}")

class Address():

    def __init__(self, list):
            self.first_name = list[0]
            self.last_name = list[1]
            self.number = list[2]

    def log_data(self):
        data_display = self.first_name + " " + self.last_name + " - " + self.number
        # print(data_add) 
        return data_display

print("Input:")
# input_ = input()
input_ = 'Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001'
print(input_)
print("\n")
print('''Output:
=== Output START ===
Log:''')
separate(input_)
print("=== Output END ===")