def outer(a,b):
    def add(a,b):
        return a+b

    addition = add(a,b)
    return addition+5

result = outer(5,10)
print(result)