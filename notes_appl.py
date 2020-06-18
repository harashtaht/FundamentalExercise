day_count = 0

present= int(input("Attendance? (0/1)"))
rate = 800
hour = int(input("Working hours:"))

salary = 0
while day_count<=20:
    day_count +=1
    if present == 1:
        salary += rate*hour
    elif present == 0:
        salary += 0
    else:
        print("error")
    print(f"DAY {day_count} SALARY {salary}")