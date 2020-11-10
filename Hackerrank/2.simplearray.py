## Part 1 ##

b = input()
b = int(b)

if (b<0) or (b > 1000):
    print("Constraints must be more than 0 or less than equal of 1000. Please enter another number.\n")
    b = input()
else:
    a = input()

ls = []
for i in a.split():
    ls.append(int(i))

results = 0
for i in ls:
    results += i

print(results)
