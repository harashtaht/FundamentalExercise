f = open("input.in.txt", "r")
# fill = f.readline()

T = []

for i in f:
    T.append(int(i))

ABK_ = T[1:]
# ABK_.append(T[1:])
T = T[0]


print(T)
print(type(T))
print(ABK_)
# print(T) #list of input
# print(type(T[0])) #int
# print(len(T)) #301
    

# print(f.read())
# T = int(input())
# # print(T)
# # print(type(T))

# if 1<=T<=100:
