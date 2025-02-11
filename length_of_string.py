def string_length(s):
    count = 0
    for i in s:
        count = count + 1
    return count

String = input("Enter the String : ")
length = string_length(String)
print("The Length of the String is : ", length)
