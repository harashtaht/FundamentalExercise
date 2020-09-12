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

# inp = "Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001"


# for i in inp.split(sep=","):
#     print(i)

# print(type(inp))

a = "ak"
print(a)