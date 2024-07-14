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

# Gönderilecek komutların tanımlanması
cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.com'

# Konfigürasyon komutlarının gönderilmesi
output = connection.send_config_set(cmd.split(';'))
print(output)

# Komut satırı isteminin alınması ve yazdırılması
print(connection.find_prompt())

# Yapılandırmanın kaydedilmesi
connection.send_command('write memory')

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
# 5. Gönderilecek Komutların Tanımlanması:
#    # Gönderilecek komutların tanımlanması
#    cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.com'
#    - Birden fazla konfigürasyon komutu tanımlanır ve her biri `;` ile ayrılır.
#
# 6. Konfigürasyon Komutlarının Gönderilmesi:
#    # Konfigürasyon komutlarının gönderilmesi
#    output = connection.send_config_set(cmd.split(';'))
#    print(output)
#    - `send_config_set` fonksiyonu kullanılarak konfigürasyon komutları gönderilir.
#    - `cmd.split(';')`: Komutları `;` karakterine göre ayırarak liste halinde gönderir.
#
# 7. Komut Satırı İsteminin Alınması ve Yazdırılması:
#    # Komut satırı isteminin alınması ve yazdırılması
#    print(connection.find_prompt())
#    - `find_prompt` fonksiyonu kullanılarak cihazın mevcut istemi (prompt) alınır ve yazdırılır.
#
# 8. Yapılandırmanın Kaydedilmesi:
#    # Yapılandırmanın kaydedilmesi
#    connection.send_command('write memory')
#    - `send_command` fonksiyonu kullanılarak yapılandırma kaydedilir.
#
# 9. Bağlantının Kapatılması:
#    # Bağlantının kapatılması
#    print('Closing connection')
#    connection.disconnect()
#    - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.
