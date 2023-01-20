import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("start")
with open("samplejson.json", "w")as write_file:
    json.dump(sampleJson,write_file,indent=4,sort_keys=True)

print("done")