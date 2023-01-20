sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

ans = dict()

for k in keys:
    ans.update({k: sample_dict[k]})
print(ans)