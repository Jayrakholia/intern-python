sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("origial list ",sample_list)

sample_list = list(set(sample_list))
print("final list: ",sample_list)

t = tuple(sample_list)
print("tuple ",t)

print("minimum number is: ",min(t))
print("maximum number is: ",max(t))
