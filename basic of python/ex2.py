print("print current and previous number sum in a range(10)")
prev_num = 0

for i in range(0,10):
    sum_num = prev_num + i
    print("current number",i,"previous number", prev_num, "sum:", sum_num)
    prev_num = i