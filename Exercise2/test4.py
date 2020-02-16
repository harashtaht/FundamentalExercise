f = open("input.in.txt", "r")
# fill = f.readline()

T = []

for i in f:
    T.append(int(i))

# ABK_ = T[1:]
# # ABK_.append(T[1:])
# T = T[0]

for number in T:
    if T[0]>=1 and T[0]<=100:
        # ABK_ = T[1:]
        T = T[0]
        continue
    else:
        break

print(T)

# print(T) #list of input
# print(type(T[0])) #int
# print(len(T)) #301
    

# print(f.read())
# T = int(input())
# # print(T)
# # print(type(T))

# if 1<=T<=100:
