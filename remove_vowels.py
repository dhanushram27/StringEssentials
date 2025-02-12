def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ""
    for char in s:
        if char not in vowels:
            result = result + char
    return result
    
name = input("Enter The String : ")
print(remove_vowels(name))
