#This code is not yet completed

num = int(input("Enter the value = "))
num = num+1

for i in range(1, num):
    if i % 1 == 0 and i % i == 0:
        print("Prime")
    elif i % 4 == 0:
        print("Quad")
    else:
        print(i)