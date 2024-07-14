# from netmiko import ConnectHandler
#
#
# with open('devices.txt') as f:
#     devices = f.read().splitlines()
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
#         }
#
#     connection = ConnectHandler(**cisco_device)
#     print('Entering the enable mode...')
#     connection.enable()
#
#
#
#     output = connection.send_command('sh run')
#     # print(output)
#
#     promt = connection.find_prompt()
#
#     hostname = promt[0:-1]
#
#     from datetime import datetime
#
#     now = datetime.now()
#     year = now.year
#     month = now.month
#     day = now.day
#
#
#     filename = f'{hostname}-{year}-{month}-{day}-backup.txt'
#
#
#     with open(filename, 'w') as backup:
#         backup.write(output)
#         print(f'Backup of {hostname} completed successfully')
#         print('#' * 40)
#
#     print('Closing connection')
#     connection.disconnect()





    # netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
from netmiko import ConnectHandler

# 'devices.txt' dosyasının açılması ve IP adreslerinin okunması
with open('devices.txt') as f:
    devices = f.read().splitlines()  # Dosyadaki IP adreslerini satır satır okuma

    # Her bir IP adresi için cihaz bilgilerini tanımlama ve işlemleri gerçekleştirme
    for ip in devices:
        # Cihaz bilgileri sözlüğünün oluşturulması
        cisco_device = {
            'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
            'host': ip,  # Cihazın IP adresi
            'username': 'admin',  # SSH bağlantısı için kullanıcı adı
            'password': 'admin',  # SSH bağlantısı için şifre
            'port': '22',  # SSH bağlantısı için port (genellikle 22)
            'secret': 'cisco',  # Enable moduna geçiş için şifre
            'verbose': True  # Bağlantı sırasında ayrıntılı çıktı sağlama
        }

        # Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
        connection = ConnectHandler(**cisco_device)

        # Enable moduna geçiş
        print('Entering the enable mode...')
        connection.enable()

        # 'show run' komutunun gönderilmesi ve çıktının alınması
        output = connection.send_command('sh run')
        # print(output)

        # Komut isteminin (prompt) bulunması
        prompt = connection.find_prompt()

        # Hostname'in prompt'tan çıkarılması
        hostname = prompt[0:-1]  # Prompt'un son karakterini (genellikle #) çıkararak hostname'i alır

        from datetime import datetime

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        # Yedekleme dosyasının adının oluşturulması
        filename = f'{hostname}-{year}-{month}-{day}-backup.txt'

        # Çıktının dosyaya yazılması
        with open(filename, 'w') as backup:
            backup.write(output)
            print(f'Backup of {hostname} completed successfully')
            print('#' * 40)

        # Bağlantının kapatılması
        print('Closing connection')
        connection.disconnect()

    # Detaylı Açıklamalar:
    # 1. Gerekli Kütüphanenin İçe Aktarılması:
    #    # netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
    #    from netmiko import ConnectHandler
    #    - `netmiko`: Ağ cihazlarıyla SSH bağlantısı kurmayı ve komut göndermeyi kolaylaştıran bir kütüphane.
    #    - `ConnectHandler`: Netmiko'nun ağ cihazlarına bağlanmak için kullandığı sınıf.
    #
    # 2. Cihaz IP Adreslerinin Okunması:
    #    # 'devices.txt' dosyasının açılması ve IP adreslerinin okunması
    #    with open('devices.txt') as f:
    #        devices = f.read().splitlines()  # Dosyadaki IP adreslerini satır satır okuma
    #    - 'devices.txt': Cihaz IP adreslerini içeren dosya.
    #    - `splitlines()`: Dosya içeriğini satır satır okuyarak liste haline getirir.
    #
    # 3. Cihaz Bilgilerinin Tanımlanması:
    #    # Her bir IP adresi için cihaz bilgilerini tanımlama ve işlemleri gerçekleştirme
    #    for ip in devices:
    #        # Cihaz bilgileri sözlüğünün oluşturulması
    #        cisco_device = {
    #            'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
    #            'host': ip,                  # Cihazın IP adresi
    #            'username': 'admin',         # SSH bağlantısı için kullanıcı adı
    #            'password': 'admin',         # SSH bağlantısı için şifre
    #            'port': '22',                # SSH bağlantısı için port (genellikle 22)
    #            'secret': 'cisco',           # Enable moduna geçiş için şifre
    #            'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
    #        }
    #
    # 4. SSH Bağlantısının Kurulması:
    #        # Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
    #        connection = ConnectHandler(**cisco_device)
    #        - `ConnectHandler` sınıfı kullanılarak SSH bağlantısı kurulur.
    #        - `**cisco_device`: Sözlükteki anahtar-değer çiftleri fonksiyona argüman olarak geçirilir.
    #
    # 5. Enable Moduna Geçiş:
    #        # Enable moduna geçiş
    #        print('Entering the enable mode...')
    #        connection.enable()
    #        - `enable` fonksiyonu kullanılarak cihazın yetkili moduna (enable mode) geçilir.
    #
    # 6. 'show run' Komutunun Gönderilmesi:
    #        # 'show run' komutunun gönderilmesi ve çıktının alınması
    #        output = connection.send_command('sh run')
    #        # print(output)
    #        - `send_command` fonksiyonu ile 'sh run' komutu cihaza gönderilir ve çıktısı alınır.
    #
    # 7. Komut İsteminin (Prompt) Bulunması:
    #        # Komut isteminin (prompt) bulunması
    #        prompt = connection.find_prompt()
    #        - `find_prompt` fonksiyonu ile cihazın mevcut komut istemi (prompt) bulunur.
    #
    # 8. Hostname'in Çıkarılması:
    #        # Hostname'in prompt'tan çıkarılması
    #        hostname = prompt[0:-1]  # Prompt'un son karakterini (genellikle #) çıkararak hostname'i alır
    #        - Prompt'tan hostname'i çıkarır. Genellikle prompt son karakter olarak '#' içerir.
    #
    # 9. Yedekleme Dosyasının Adının Oluşturulması:
    #        # Yedekleme dosyasının adının oluşturulması
    #        filename = f'{hostname}-backup.txt'
    #        - Hostname'e dayalı olarak yedekleme dosyasının adı oluşturulur.
    #
    # 10. Çıktının Dosyaya Yazılması:
    #        # Çıktının dosyaya yazılması
    #        with open(filename, 'w') as backup:
    #            backup.write(output)
    #            print(f'Backup of {hostname} completed successfully')
    #            print('#' * 40)
    #        - Dosya yazma modunda açılır ve 'show run' komutunun çıktısı dosyaya yazılır.
    #
    # 11. Bağlantının Kapatılması:
    #        # Bağlantının kapatılması
    #        print('Closing connection')
    #        connection.disconnect()
    #        - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.


