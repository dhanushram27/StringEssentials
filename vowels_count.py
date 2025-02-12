def check_vowels_count(s):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            count = count + 1
    return count
    
name = input("Enter The String : ")
print(check_vowels_count(name))
