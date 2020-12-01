# Part 1: catAndMouse

#in: 2 5 4 out: cat B
#in: 1 2 3 out: cat B
#in: 1 3 2 out: mouse C

def catAndMouse(str):
    nums = [int(x) for x in str.split()]
    numA = nums[0]
    numB = nums[1]
    numC = nums[-1]

    if (numC>numA) and (numC>numB):
        if abs(numC-numA) < abs(numC-numB):
            print("Cat A")
        elif abs(numC-numA) > abs(numC-numB):
            print("Cat B")
        elif abs(numC-numA) == abs(numC-numB):
            print("Mouse C")
    elif (numC<numA) or (numC<numB):
        if abs(numC-numA) < abs(numC-numB):
            print("Cat A")
        elif abs(numC-numA) > abs(numC-numB):
            print("Cat B")
        elif abs(numC-numA) == abs(numC-numB):
            print("Mouse C")
    elif (numC==numA) or (numC==numB):
        if abs(numC-numA) < abs(numC-numB):
            print("Cat A")
        elif abs(numC-numA) > abs(numC-numB):
            print("Cat B")
        elif abs(numC-numA) == abs(numC-numB):
            print("Mouse C")

q = int(input())
ls = []
for i in range(q):
    ls.append(input())

for i in ls:
    catAndMouse(i)