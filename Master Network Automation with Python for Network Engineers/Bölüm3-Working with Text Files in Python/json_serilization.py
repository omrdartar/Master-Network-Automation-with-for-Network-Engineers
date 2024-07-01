#################################
## Data Serialization and Deserialization with JSON
#################################

import json

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

# Serializing the dictionary to a text file called `friends.json`
with open('friends.json', 'wt') as f:
    json.dump(friends, f, indent=4)
    # `friends` sözlüğünü JSON formatına dönüştürüp (`serialize` edip) 'friends.json' dosyasına yazma.
    # indent=4 parametresi, JSON verisinin okunabilir bir formatta yazılmasını sağlar.

# Serializing the dictionary to a JSON encoded string
json_string = json.dumps(friends, indent=4)
print(json_string)
# `friends` sözlüğünü JSON formatına dönüştürüp (`serialize` edip) bir string olarak `json_string` değişkenine atama.
# indent=4 parametresi, JSON verisinin okunabilir bir formatta olmasını sağlar.
# `json_string` değişkenini ekrana yazdırma.

# Deserializing from file into a Python Object
with open('friends.json') as f:
    obj = json.load(f)
    # 'friends.json' dosyasını açma ve içeriğini JSON formatından Python nesnesine (`obj`) dönüştürme (`deserialize`).

    print(type(obj))  # => dict
    # `obj` değişkeninin türünü yazdırma. Bu örnekte `obj` bir dictionary (sözlük) olacak.

    print(obj)
    # `obj` değişkeninin içeriğini ekrana yazdırma. `obj`, `friends` sözlüğünün orijinal hali olacak.

# Loading a JSON encoded string into a Python Object
json_string = """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""
# JSON formatında kodlanmış bir string tanımlama.

obj = json.loads(json_string)
# JSON formatındaki `json_string` değişkenini Python nesnesine (`obj`) dönüştürme (`deserialize`).

print(type(obj))  # => dict
# `obj` değişkeninin türünü yazdırma. Bu örnekte `obj` bir dictionary (sözlük) olacak.

print(obj)
# `obj` değişkeninin içeriğini ekrana yazdırma. `obj`, `friends` sözlüğünün orijinal hali olacak.
