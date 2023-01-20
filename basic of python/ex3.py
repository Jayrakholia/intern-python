str = input("enter string ")
print("orginal string:",str)

size=len(str)
print("even index char")
for i in range(0,size-1,2):
    print(str[i])