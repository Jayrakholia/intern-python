def mul_and_sum(num1,num2):
    product= num1 * num2
    if product <=1000:
        return product
    else:
        return num1+num2

answer = mul_and_sum(30,7)
print("the answer is:",answer)

answer = mul_and_sum(300,7)
print("the answer is:",answer)


