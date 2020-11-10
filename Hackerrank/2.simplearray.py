## Part 1 ##

# a = (input())
a = '2 4 1 20 18'

# print(a)
# print(type(a))
ls = []
for i in a.split():
    ls.append(int(i))

results = 0
for i in ls:
    results += i
    print(results)

print(results)