num = 5
fact = 1
if num <0:
    print("doesn't exist")
elif num==0:
    print("fact is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)