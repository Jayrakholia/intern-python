def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0

ans= addition(10)
print(ans)