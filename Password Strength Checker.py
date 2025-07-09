password = input("Enter your password: ")
strength = 0
for char in password:
    if char == int:
        strength = strength+1
    elif char == '@' or '!' or '#' or '$' or '&' or '*':
        strength = strength+2
    elif char == '@' and '!':
        strength = strength+4
    elif char == '(' and ')':
        strength = strength+2
    elif len(password) >= 5:
        strength = strength+2
    elif len(password) < 5:
        strength = strength+1
print("Your password: ",password)
print("The strength of your password = ",strength)
if strength >= 30:
    print("Strong")
elif strength < 20:
    print("medium")
elif strength <= 10:
    print("Low")