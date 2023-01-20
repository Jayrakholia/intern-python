import random

lottery_tickets_list = []
print("create 100 random ticket")

for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_tickets_list,2)
print("lucky 2 lottery ticket", winners)