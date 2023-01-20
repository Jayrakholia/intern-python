n=5
start = 2
sum_seq = 0

for i in range(0,n):
    print(start,end="+")
    start=start*10+2
    sum_seq += start

print("=",sum_seq)