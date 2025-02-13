string = input("Enter The string : ")
case = string.lower()
rev = case[::-1]

if case == rev:
    print("It's Palindrome")
else:
    print("It's Not an Palindrome")
