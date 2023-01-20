import secrets

secretsGenerator = secrets.SystemRandom()
print("generate")
otp = secretsGenerator.randrange(100000, 999999)
print(otp)