def find_All(str1):
    char_count = 0
    digit_count=0
    symbol_count=0
    for char in str1:
        if char.isalpha():
            char_count+=1
        elif char.isdigit():
            digit_count+=1
        else:
            symbol_count+=1
    print("char =",char_count,"digits =",digit_count,"symbols =",symbol_count)
str1="P@#yn26at^&i5ve"
print("total count of char,digits,symbols \n")
find_All(str1)