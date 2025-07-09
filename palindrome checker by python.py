string = input("Enter the word you want to check: ")
s = string[::-1]
if string == s:
    print("This word is a Palindrome!")
else:
    print("This is not Palindrome!")

print("Solution:")
print("Your word: ",string)
print("Reversed: ",s)
input("Press enter to close....")