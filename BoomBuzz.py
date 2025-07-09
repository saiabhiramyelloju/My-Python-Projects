num = int(input("Enter the value = "))
for i in range(1, num):
    if i % 7 == 0 and i % 11 != 0:
        print("Boom!")
    elif i % 11 == 0 and i % 7 != 0:
        print("Buzz!")
    elif i % 77 == 0:
        print("BoomBuzz!")
    else:
        print(i)