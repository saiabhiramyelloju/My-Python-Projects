num = int(input("enter the value = "))

def is_palin(n):
    return str(n) == str(n)[::-1]

for i in range(1, num+1):
    output = ""

    if is_palin(i):
        output += "Palin"
    if i % 9 == 0:
        output += "Buzz"
    print(output or i)