num = int(input("Enter the value = "))
num = num+1

for i in range(1,num):
    if i % 2 == 0:
        print("Even")
    elif i % 1 == 0 and i % 5 != 0:
        print("Odd")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)