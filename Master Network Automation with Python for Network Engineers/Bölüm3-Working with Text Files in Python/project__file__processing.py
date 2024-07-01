# PROJECT: FILE PROCESSING

with open('devices.txt') as f:
    content = f.read().splitlines()
    print(content)
    devices = list()
    for line in content:
        devices.append(line.split(':'))
    print(devices)


"""
with open('devices.txt') as f:
    content = f.read().splitlines()
    print(content)
    devices = list()
    for line in content:
        devices.append(line.split(':'))
    print(devices)

Bu komutları tek tek detaylı bir şekilde açıklayalım:

1. Dosyayı Açma ve Okuma

with open('devices.txt') as f:
    content = f.read().splitlines()

Bu kısımda birkaç şey gerçekleşiyor:

1. with open('devices.txt') as f: Bu, devices.txt adlı dosyayı okumak için açar. with ifadesi, dosya işlemlerinde kaynak yönetimi sağlar ve dosyanın otomatik olarak kapatılmasını garanti eder. f değişkeni, dosya nesnesini temsil eder.

2. content = f.read().splitlines(): 
    - f.read(): Dosyanın içeriğini bir string olarak okur.
    - .splitlines(): Bu, dosyanın içeriğini satır satır ayırır ve her bir satırı bir liste elemanı olarak döner. Boş satırlar da dahil olmak üzere her satır bir liste elemanı olur.

2. İçeriği Yazdırma

print(content)

Bu komut, content değişkeninin içeriğini yazdırır. content bir liste olduğundan, dosyanın her satırını bir liste elemanı olarak ekrana yazdırır.

3. Cihazlar Listesini Oluşturma

devices = list()

Bu satır, devices adlı boş bir liste oluşturur. Bu liste, daha sonra dosyadaki her satırın belirli bir işleme tabi tutulmuş halini saklamak için kullanılacaktır.

4. Satırları Bölme ve Listeye Ekleme

for line in content:
    devices.append(line.split(':'))

Bu döngü, content listesindeki her bir satırı işler:

1. for line in content: content listesindeki her bir eleman (line) üzerinde döngü yapar.

2. line.split(':'): Her bir satırı (string) : karakterine göre böler ve bu, bir liste döner. Örneğin, "device1:info1" satırı ["device1", "info1"] listesine dönüşür.

3. devices.append(line.split(':')): Bölünmüş listeyi devices listesine ekler. Bu, devices listesinin her bir elemanının, content listesindeki bir satırın : karakterine göre bölünmüş hali olmasını sağlar.

5. devices Listesini Yazdırma

print(devices)

Bu komut, devices listesinin içeriğini yazdırır. devices listesi, content listesindeki her bir satırın : karakterine göre bölünmüş hallerinden oluşur.

Örnek Dosya ve Çıktılar

Varsayalım ki devices.txt dosyasının içeriği şu şekilde olsun:

device1:info1
device2:info2
device3:info3

Yukarıdaki kod şu adımları izler:

1. Dosya açılır ve content listesi şu şekilde olur:
   ['device1:info1', 'device2:info2', 'device3:info3']

2. content listesi ekrana yazdırılır.

3. Boş bir devices listesi oluşturulur.

4. Döngü, her bir satırı : karakterine göre böler ve devices listesine ekler:
   [['device1', 'info1'], ['device2', 'info2'], ['device3', 'info3']]

5. devices listesi ekrana yazdırılır.

Bu, dosyadaki her bir satırın iki parçaya bölündüğü ve sonuçların iki boyutlu bir liste olarak saklandığı bir süreçtir.
"""


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
with open('devices.txt') as f:
    content = f.read().splitlines()
    print(content)
    devices = list()
    for line in content[1:]:
        devices.append(line.split(':'))
    print(devices)

for device in devices:
    print(f'ping {device[1]}')

Bu komutları tek tek detaylı bir şekilde açıklayalım:

1. Dosyayı Açma ve Okuma

with open('devices.txt') as f:
    content = f.read().splitlines()

Bu kısımda birkaç şey gerçekleşiyor:

1. with open('devices.txt') as f: Bu, devices.txt adlı dosyayı okumak için açar. with ifadesi, dosya işlemlerinde kaynak yönetimi sağlar ve dosyanın otomatik olarak kapatılmasını garanti eder. f değişkeni, dosya nesnesini temsil eder.

2. content = f.read().splitlines(): 
    - f.read(): Dosyanın içeriğini bir string olarak okur.
    - .splitlines(): Bu, dosyanın içeriğini satır satır ayırır ve her bir satırı bir liste elemanı olarak döner. Boş satırlar da dahil olmak üzere her satır bir liste elemanı olur.

2. İçeriği Yazdırma

print(content)

Bu komut, content değişkeninin içeriğini yazdırır. content bir liste olduğundan, dosyanın her satırını bir liste elemanı olarak ekrana yazdırır.

3. Cihazlar Listesini Oluşturma ve Satırları Bölme

devices = list()

Bu satır, devices adlı boş bir liste oluşturur. Bu liste, daha sonra dosyadaki her satırın belirli bir işleme tabi tutulmuş halini saklamak için kullanılacaktır.

for line in content[1:]:
    devices.append(line.split(':'))

Bu döngü, content listesindeki her bir satırı işler:

1. for line in content[1:]: content listesindeki ilk satırı atlayarak her bir eleman (line) üzerinde döngü yapar.
2. line.split(':'): Her bir satırı (string) : karakterine göre böler ve bu, bir liste döner. Örneğin, "device1:info1" satırı ["device1", "info1"] listesine dönüşür.
3. devices.append(line.split(':')): Bölünmüş listeyi devices listesine ekler. Bu, devices listesinin her bir elemanının, content listesindeki bir satırın : karakterine göre bölünmüş hali olmasını sağlar.

4. devices Listesini Yazdırma

print(devices)

Bu komut, devices listesinin içeriğini yazdırır. devices listesi, content listesindeki her bir satırın : karakterine göre bölünmüş hallerinden oluşur.

5. Ping Komutlarını Oluşturma ve Yazdırma

for device in devices:
    print(f'ping {device[1]}')

Bu döngü, devices listesindeki her bir cihaz için bir ping komutu oluşturur ve yazdırır:

1. for device in devices: devices listesindeki her bir eleman (device) üzerinde döngü yapar.
2. print(f'ping {device[1]}'): Her bir cihazın ikinci elemanını (IP adresi veya hostname) kullanarak bir ping komutu oluşturur ve ekrana yazdırır. f-string kullanılarak dinamik bir şekilde ping komutları oluşturulur.

Örnek Dosya ve Çıktılar

Varsayalım ki devices.txt dosyasının içeriği şu şekilde olsun:

header
device1:192.168.1.1
device2:192.168.1.2
device3:192.168.1.3

Yukarıdaki kod şu adımları izler:

1. Dosya açılır ve content listesi şu şekilde olur:
   ['header', 'device1:192.168.1.1', 'device2:192.168.1.2', 'device3:192.168.1.3']

2. content listesi ekrana yazdırılır.

3. Boş bir devices listesi oluşturulur.

4. Döngü, ilk satırı atlayarak her bir satırı : karakterine göre böler ve devices listesine ekler:
   [['device1', '192.168.1.1'], ['device2', '192.168.1.2'], ['device3', '192.168.1.3']]

5. devices listesi ekrana yazdırılır.

6. Ping komutları oluşturulur ve ekrana yazdırılır:
   ping 192.168.1.1
   ping 192.168.1.2
   ping 192.168.1.3

Bu, dosyadaki her bir satırın iki parçaya bölündüğü, bir listeye eklendiği ve her bir cihaz için bir ping komutunun oluşturulduğu bir süreçtir.
"""























