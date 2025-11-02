users = {
    "id": 1,
    "name": "Alexander Graham Bell",
    "username": "AGBell",
    "email": "alexandergrahambell@gmail.com",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(users)
print(type(users))
print("\nUbah dict ke json(ini hanya output bukan jadi file) (menggunakan json.dumps")
import json
result = json.dumps(users)
print(type(result))
print(result)

"""
Mengubah dictionary ke file.json menggunakan json.dump
"""
with open("result.json", "w") as file:
    json.dump(users, file)