number = str(input('Enter a number: '))
 
if number == number[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")