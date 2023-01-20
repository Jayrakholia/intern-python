import json

class Vehicle:
    def __init__(self,name,engine,price):
        self.name=name
        self.engine=engine
        self.price=price

def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicleobj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',object_hook=vehicleDecoder)

print("type of decoded object from json data")
print(type(vehicleobj))
print("vehicle details")
print(vehicleobj.name,vehicleobj.engine,vehicleobj.price)