num = 76542
rev_num=0
print("number",num)

while num>0:
    digit=num%10
    rev_num=(rev_num*10)+digit
    num=num//10
print("reverse num: ",rev_num)