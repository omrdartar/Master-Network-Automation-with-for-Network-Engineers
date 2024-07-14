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

# Komut satırı istemcisinin bulunması
promt = connection.find_prompt()
print(promt)

# Eğer komut satırı istemcisinde '>' karakteri varsa, enable moduna geçiş yapılması
if '>' in promt:
    connection.enable()

# 'show run' komutunun gönderilmesi ve çıktısının alınması
output = connection.send_command('sh run')
print(output)

# Eğer konfigürasyon modunda değilse, konfigürasyon moduna geçiş yapılması
if not connection.check_config_mode():
    connection.config_mode()

# Yeni bir kullanıcı oluşturma komutunun gönderilmesi
connection.send_command('username admin2 secret cisco')

# Konfigürasyon modundan çıkış yapılması
connection.exit_config_mode()

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
# 4. Komut Satırı İstemcisinin Bulunması:
#    # Komut satırı istemcisinin bulunması
#    promt = connection.find_prompt()
#    print(promt)
#    - `find_prompt` fonksiyonu, mevcut komut satırı istemcisini (prompt) bulur ve döndürür.
#
# 5. Enable Moduna Geçiş:
#    # Eğer komut satırı istemcisinde '>' karakteri varsa, enable moduna geçiş yapılması
#    if '>' in promt:
#        connection.enable()
#    - Eğer mevcut istemci `>` karakteri içeriyorsa (genellikle kullanıcı modunda), `enable` fonksiyonu kullanılarak enable moduna geçilir.
#
# 6. 'show run' Komutunun Gönderilmesi ve Çıktısının Alınması:
#    # 'show run' komutunun gönderilmesi ve çıktısının alınması
#    output = connection.send_command('sh run')
#    print(output)
#    - `send_command` fonksiyonu kullanılarak `show run` komutu gönderilir ve komutun çıktısı alınır.
#
# 7. Konfigürasyon Moduna Geçiş:
#    # Eğer konfigürasyon modunda değilse, konfigürasyon moduna geçiş yapılması
#    if not connection.check_config_mode():
#        connection.config_mode()
#    - Eğer cihaz konfigürasyon modunda değilse (`check_config_mode` ile kontrol edilir), `config_mode` fonksiyonu kullanılarak konfigürasyon moduna geçilir.
#
# 8. Yeni Bir Kullanıcı Oluşturma:
#    # Yeni bir kullanıcı oluşturma komutunun gönderilmesi
#    connection.send_command('username admin2 secret cisco')
#    - `send_command` fonksiyonu kullanılarak yeni bir kullanıcı oluşturma komutu gönderilir.
#
# 9. Konfigürasyon Modundan Çıkış:
#    # Konfigürasyon modundan çıkış yapılması
#    connection.exit_config_mode()
#    - `exit_config_mode` fonksiyonu kullanılarak konfigürasyon modundan çıkılır.
#
# 10. Bağlantının Kapatılması:
#     # Bağlantının kapatılması
#     print('Closing connection')
#     connection.disconnect()
#     - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.
