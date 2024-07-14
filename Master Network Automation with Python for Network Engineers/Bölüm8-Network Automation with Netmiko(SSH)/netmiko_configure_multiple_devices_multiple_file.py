# from netmiko import ConnectHandler
#
#
# with open('devices.txt') as f:
#     devices = f.read().splitlines()
#
# device_list = list()
#
#
# for ip in devices:
#
#     cisco_device = {
#         'device_type': 'cisco_ios',
#         'host': ip,
#         'username': 'admin',
#         'password': 'admin',
#         'port': '22',
#         'secret': 'cisco',
#         'verbose': True
#          }
#     device_list.append(cisco_device)
#
#
#
#
# for device in device_list:
#
#     connection = ConnectHandler(**device)
#
#     print('Entering the enable mode...')
#     connection.enable()
#
#
#     file = input(f'Enter a configuration file(use a vaild path) for {device["host"]}:')
#
#
#     print(f'Running commands from file: {file} on device: {device["host"]}')
#
#     output = connection.send_config_from_file(file)
#
#     print(output)
#
#     print(f'Closing connection to {cisco_device["host"]}')
#     connection.disconnect()
#
#     print('#' * 30)



################################################################################################################
################################################################################################################
################################################################################################################


# netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
from netmiko import ConnectHandler

# 'devices.txt' dosyasının açılması ve içeriğinin okunması
with open('devices.txt') as f:
    devices = f.read().splitlines()  # Dosyadaki IP adreslerini satır satır okuma

# Cihaz listesi için bir liste oluşturma
device_list = list()

# Her bir IP adresi için cihaz bilgilerini tanımlama ve listeye ekleme
for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
        'host': ip,  # Cihazın IP adresi
        'username': 'admin',  # SSH bağlantısı için kullanıcı adı
        'password': 'admin',  # SSH bağlantısı için şifre
        'port': '22',  # SSH bağlantısı için port (genellikle 22)
        'secret': 'cisco',  # Enable moduna geçiş için şifre
        'verbose': True  # Bağlantı sırasında ayrıntılı çıktı sağlama
    }
    device_list.append(cisco_device)  # Cihaz bilgilerini listeye ekleme

# Her bir cihaz için bağlantı kurma ve komutları gönderme
for device in device_list:
    # Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
    connection = ConnectHandler(**device)

    # Enable moduna geçiş
    print('Entering the enable mode...')
    connection.enable()

    # Kullanıcıdan konfigürasyon dosyası yolunu isteme
    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}:')

    # Dosyadan komutların gönderilmesi
    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    # Bağlantının kapatılması
    print(f'Closing connection to {device["host"]}')
    connection.disconnect()

    # İşlemin tamamlandığını belirten ayırıcı çizgi
    print('#' * 30)






################################################################################################################
################################################################################################################
################################################################################################################


# Detaylı Açıklamalar:
# 1. Gerekli Kütüphanenin İçe Aktarılması:
#    # netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
#    from netmiko import ConnectHandler
#    - `netmiko`: Ağ cihazlarıyla SSH bağlantısı kurmayı ve komut göndermeyi kolaylaştıran bir kütüphane.
#    - `ConnectHandler`: Netmiko'nun ağ cihazlarına bağlanmak için kullandığı sınıf.
#
# 2. Cihaz IP Adreslerinin Okunması:
#    # 'devices.txt' dosyasının açılması ve içeriğinin okunması
#    with open('devices.txt') as f:
#        devices = f.read().splitlines()  # Dosyadaki IP adreslerini satır satır okuma
#    - 'devices.txt': Cihaz IP adreslerini içeren dosya.
#    - `splitlines()`: Dosya içeriğini satır satır okuyarak liste haline getirir.
#
# 3. Cihaz Listesinin Oluşturulması:
#    # Cihaz listesi için bir liste oluşturma
#    device_list = list()
#    - Boş bir liste oluşturulur, bu listeye cihaz bilgileri eklenecektir.
#
# 4. Cihaz Bilgilerinin Tanımlanması ve Listeye Eklenmesi:
#    # Her bir IP adresi için cihaz bilgilerini tanımlama ve listeye ekleme
#    for ip in devices:
#        cisco_device = {
#            'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
#            'host': ip,                  # Cihazın IP adresi
#            'username': 'admin',         # SSH bağlantısı için kullanıcı adı
#            'password': 'admin',         # SSH bağlantısı için şifre
#            'port': '22',                # SSH bağlantısı için port (genellikle 22)
#            'secret': 'cisco',           # Enable moduna geçiş için şifre
#            'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
#        }
#        device_list.append(cisco_device)  # Cihaz bilgilerini listeye ekleme
#    - Her IP adresi için bir cihaz sözlüğü oluşturulur ve bu sözlük `device_list` listesine eklenir.
#
# 5. Cihazlara Bağlantı Kurma ve Komut Gönderme:
#    # Her bir cihaz için bağlantı kurma ve komutları gönderme
#    for device in device_list:
#        # Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
#        connection = ConnectHandler(**device)
#        - `ConnectHandler` sınıfı kullanılarak SSH bağlantısı kurulur.
#        - `**device`: Sözlükteki anahtar-değer çiftleri fonksiyona argüman olarak geçirilir.
#
#        # Enable moduna geçiş
#        print('Entering the enable mode...')
#        connection.enable()
#        - `enable` fonksiyonu kullanılarak cihazın yetkili moduna (enable mode) geçilir.
#
#        # Kullanıcıdan konfigürasyon dosyası yolunu isteme
#        file = input(f'Enter a configuration file (use a valid path) for {device["host"]}:')
#        - `input` fonksiyonu kullanılarak kullanıcıdan konfigürasyon dosyasının yolunu isteme.
#
#        # Dosyadan komutların gönderilmesi
#        print(f'Running commands from file: {file} on device: {device["host"]}')
#        output = connection.send_config_from_file(file)
#        print(output)
#        - `send_config_from_file` fonksiyonu kullanılarak belirtilen dosyadaki komutlar cihaza gönderilir.
#
#        # Bağlantının kapatılması
#        print(f'Closing connection to {device["host"]}')
#        connection.disconnect()
#        - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.
#
#        # İşlemin tamamlandığını belirten ayırıcı çizgi
#        print('#' * 30)



################################################################################################################
################################################################################################################
################################################################################################################