def check_vowel_consonant(char):
    char.lower()
    
    if char in ['a','e','i','o','u']:
        return "vowel"
    elif char.isalpha():
        return "Consonant"
    else:
        return "Invalid Input"

char = input("Enter The Character : ")

if len(char) == 1:
    print(check_vowel_consonant(char))
else:
    print("Please enter a Single Character")
