num = int(input("Enter the value = ")) # gets the number from user
num = num+1
for i in range(1,num):
    if i % 3 == 0 and i % 5 != 0 and i % 7 != 0:
        print("Foo")
    elif i % 5 == 0 and i % 3 != 0 and i % 7 != 0:
        print("Bar")
    elif i % 7 == 0 and i % 3 != 0 and i % 5 != 0:
        print("Qix")
    else:
        print(i)