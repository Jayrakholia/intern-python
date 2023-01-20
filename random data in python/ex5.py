import random
import string

def randomString(stirngLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters)for i in range(stirngLength))

print("random string",randomString(5))