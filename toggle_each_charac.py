def toggled_charac(s):
    toggled = ""
    for char in s:
        if char.islower():
            toggled = toggled + char.upper()
        elif char.isupper():
            toggled = toggled + char.lower()
        else:
            toggled = toggled + char
    return toggled

user = input("Enter the String : ")
print(toggled_charac(user))
