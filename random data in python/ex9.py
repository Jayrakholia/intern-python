import random

dice=[1,2,3,4,5,6]
print("random")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))