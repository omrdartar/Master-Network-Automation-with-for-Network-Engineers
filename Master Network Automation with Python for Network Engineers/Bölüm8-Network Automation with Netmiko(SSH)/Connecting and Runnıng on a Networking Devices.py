# from netmiko import Netmiko
#
#
#
# connection = Netmiko(host= '192.168.146.10', port = '22', username = 'admin1', password = 'admin1', device_type = 'cisco_ios')



# netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
from netmiko import ConnectHandler

# Cisco cihazına ait bağlantı bilgilerinin tanımlanması
cisco_device = {
    'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
    'host': '192.168.146.10',    # Cihazın IP adresi
    'username': 'admin1',        # SSH bağlantısı için kullanıcı adı
    'password': 'admin1',        # SSH bağlantısı için şifre
    'port': '22',                # SSH bağlantısı için port (genellikle 22)
    'secret': 'cisco',           # Enable moduna geçiş için şifre
    'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
}

# Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
connection = ConnectHandler(**cisco_device)

# 'show ip interface brief' komutunun gönderilmesi ve çıktısının alınması
output = connection.send_command('sh ip int brief')
print(output)

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
# 2. Cisco Cihazına Ait Bağlantı Bilgilerinin Tanımlanması:
#    # Cisco cihazına ait bağlantı bilgilerinin tanımlanması
#    cisco_device = {
#        'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
#        'host': '192.168.146.10',    # Cihazın IP adresi
#        'username': 'admin1',        # SSH bağlantısı için kullanıcı adı
#        'password': 'admin1',        # SSH bağlantısı için şifre
#        'port': '22',                # SSH bağlantısı için port (genellikle 22)
#        'secret': 'cisco',           # Enable moduna geçiş için şifre
#        'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
#    }
#    - Bu sözlük, cihaza nasıl bağlanılacağını belirten tüm gerekli bilgileri içerir.
#
# 3. SSH Bağlantısı Kurulması:
#    # Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
#    connection = ConnectHandler(**cisco_device)
#    - `ConnectHandler` sınıfı kullanılarak SSH bağlantısı kurulur.
#    - `**cisco_device`: Sözlükteki anahtar-değer çiftleri fonksiyona argüman olarak geçirilir.
#
# 4. 'show ip interface brief' Komutunun Gönderilmesi ve Çıktısının Alınması:
#    # 'show ip interface brief' komutunun gönderilmesi ve çıktısının alınması
#    output = connection.send_command('sh ip int brief')
#    print(output)
#    - `send_command` fonksiyonu kullanılarak `show ip interface brief` komutu gönderilir ve komutun çıktısı alınır.
#
# 5. Bağlantının Kapatılması:
#    # Bağlantının kapatılması
#    print('Closing connection')
#    connection.disconnect()
#    - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.
