



with open('devices.txt') as f:
    content = f.read().splitlines()
    print(content)
    devices = list()
    for line in content[1:]:
        devices.append(line.split(':'))
    print(devices)


for device in devices:
    print(f'ping {device[1]}')





"""

Bu kod, "devices.txt" adlı bir dosyadan cihaz bilgilerini okur ve her cihaz için "ping" komutunu oluşturur. 
İşte bu kodun nasıl çalıştığını adım adım açıklayalım:

"""


"""
    1- Dosyayı Açma ve İçeriğini Okuma:
"""

# with open('devices.txt') as f:
#     content = f.read().splitlines()
#     print(content)

"""

 -with- open('devices.txt') as f:: "devices.txt" adlı dosyayı açar ve f olarak adlandırılan bir dosya nesnesi oluşturur.

 - content = f.read().splitlines(): -  Dosyanın tüm içeriğini okur ve satır satır bir listeye (content) böler. 
Her bir satır bu listenin bir elemanı olur.

 - print(content): - Okunan satırları yazdırır. Bu adım, dosya içeriğini kontrol etmek için kullanılır.

"""



"""
    2- Cihaz Bilgilerini Listede Toplama:
"""

# devices = list()
# for line in content[1:]:
#     devices.append(line.split(':'))
# print(devices)



"""

- devices -  = list(): Boş bir liste (devices) oluşturur.

- for line in content[1:]: - Dosya içeriğinin ilk satırını (genellikle başlık satırı) atlayarak, ikinci satırdan itibaren her bir satır için döngüye girer.

- devices.append(line.split(':')): - Her bir satırı ':' karakterine göre böler ve sonucu devices listesine ekler. Bu, her cihazın bilgisini bir liste olarak saklar.

- print(devices): - Cihaz bilgilerini içeren listeyi yazdırır.


"""


"""
    3-Ping Komutlarını Oluşturma ve Yazdırma:
"""


# for device in devices:
#     print(f'ping {device[1]}')

"""

for device in devices:: devices listesindeki her bir cihaz için döngüye girer.
print(f'ping {device[1]}'): Her cihazın IP adresine (listenin ikinci elemanı) göre bir "ping" komutu oluşturur ve yazdırır. 
f'ping {device[1]}' ifadesi, Python'da formatlı bir string (f-string) kullanarak ping komutunu oluşturur.

"""



"""

Özetle, bu kod:

devices.txt dosyasını açar ve satır satır okur.
Dosya içeriğini ':' karakterine göre böler ve her bir cihazın bilgilerini bir listeye toplar.
Her cihaz için bir ping komutu oluşturur ve bu komutları yazdırır.

"""