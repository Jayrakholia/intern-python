str1 = "PYnative29@#8496"
total=0
cnt=0
for char in str1:
    if char.isdigit():
        total+=int(char)
        cnt+=1
avg=total/cnt
print("sum: ",total, "average: ",avg)