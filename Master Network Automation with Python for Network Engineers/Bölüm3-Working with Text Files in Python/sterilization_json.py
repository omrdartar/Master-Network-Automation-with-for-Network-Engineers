import json

# Arkadaş bilgilerini içeren bir dictionary tanımlama
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

# JSON formatında yazma işlemi için 'friends.json' adlı dosyayı açma ('w' modunda)
with open('friends.json', 'w') as f:
    # JSON verisini 'friends.json' dosyasına yazma
    json.dump(friends, f, indent=4)
    # indent=4 parametresiyle JSON verisi okunabilir bir formatta yazılır.

# JSON verisini okunabilir bir string formatına dönüştürme
json_string = json.dumps(friends, indent=4)

# JSON verisini ekrana yazdırma
print(json_string)
# JSON verisi, okunabilir bir şekilde ekrana yazdırılır.
