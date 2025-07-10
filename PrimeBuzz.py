#This code is completed
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

num = int(input("Enter the value = "))
num = num+1

for i in range(1, num):
    if is_prime(i):
        print("Prime")
    elif i % 4 == 0:
        print("Quad")
    else:
        print(i)