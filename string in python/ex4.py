str1 = "PyNaTive"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str1 = ''.join(lower+upper)
print("result: ",sorted_str1)