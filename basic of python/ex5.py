def FLS(numlist):
    print("list:",numlist)

    first_num = numlist[0]
    last_num = numlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10,20,30,40,10]
print("answer is: ",FLS(numbers_x))

numbers_y = [75,65,35,75,30]
print("answer is: ",FLS(numbers_y))

