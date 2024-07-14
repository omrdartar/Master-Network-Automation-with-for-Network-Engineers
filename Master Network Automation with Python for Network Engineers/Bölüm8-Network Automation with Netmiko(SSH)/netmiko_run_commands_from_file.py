# netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
from netmiko import ConnectHandler

# Cisco cihazına ait bağlantı bilgilerinin tanımlanması
cisco_device = {
    'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
    'host': '192.168.146.10',    # Cihazın IP adresi
    'username': 'admin',         # SSH bağlantısı için kullanıcı adı
    'password': 'admin',         # SSH bağlantısı için şifre
    'port': '22',                # SSH bağlantısı için port (genellikle 22)
    'secret': 'cisco',           # Enable moduna geçiş için şifre
    'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
}

# Tanımlanan bağlantı bilgileri ile SSH bağlantısı kurulması
connection = ConnectHandler(**cisco_device)

# Enable moduna geçiş
print('Entering the enable mode...')
connection.enable()

# Dosyadan komutların gönderilmesi
print('Sending commands from file...')
output = connection.send_config_from_file('ospf.txt')
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
#        'username': 'admin',         # SSH bağlantısı için kullanıcı adı
#        'password': 'admin',         # SSH bağlantısı için şifre
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
# 4. Enable Moduna Geçiş:
#    # Enable moduna geçiş
#    print('Entering the enable mode...')
#    connection.enable()
#    - `enable` fonksiyonu kullanılarak cihazın yetkili moduna (enable mode) geçilir.
#
# 5. Dosyadan Komutların Gönderilmesi:
#    # Dosyadan komutların gönderilmesi
#    print('Sending commands from file...')
#    output = connection.send_config_from_file('ospf.txt')
#    print(output)
#    - `send_config_from_file` fonksiyonu kullanılarak bir dosyadaki konfigürasyon komutları gönderilir.
#    - 'ospf.txt': Gönderilecek komutları içeren dosyanın adı.
#
# 6. Bağlantının Kapatılması:
#    # Bağlantının kapatılması
#    print('Closing connection')
#    connection.disconnect()
#    - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.
