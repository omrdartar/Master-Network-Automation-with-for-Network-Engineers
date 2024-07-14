# from netmiko import ConnectHandler
# from datetime import datetime
# import time
# import threading
#
#
#
# start = time.time()
#
#
# def backup(device):
#     connection = ConnectHandler(**device)
#     print('Entering the enable mode...')
#     connection.enable()
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
#     filename = f'{hostname}-{year}-{month}-{day}-backup.txt'
#
#     with open(filename, 'w') as backup:
#         backup.write(output)
#         print(f'Backup of {hostname} completed successfully')
#         print('#' * 40)
#
#     print('Closing connection')
#
# with open('devices.txt') as f:
#     devices = f.read().splitlines()
#
#
# threads = list()
# for ip in devices:
#
#     device = {
#         'device_type': 'cisco_ios',
#         'host': ip,
#         'username': 'admin',
#         'password': 'admin',
#         'port': '22',
#         'secret': 'cisco',
#         'verbose': True
#         }
#     th = threading.Thread(target=backup, args=(device,))
#     threads.append(th)
#
#
#
# for th in threads:
#     th.start()
#
# for th in threads:
#     th.join()
#
#
#
# end = time.time()
#
# print(f'Total execution time:{end-start}')








##################################################################################################################
##################################################################################################################
##################################################################################################################




# netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
from netmiko import ConnectHandler
# datetime modülünden datetime sınıfının içe aktarılması (dosya isimlendirmede kullanmak için)
from datetime import datetime
# time modülünün içe aktarılması (toplam süreyi hesaplamak için)
import time
# threading modülünün içe aktarılması (çoklu iş parçacığı için)
import threading

# Başlangıç zamanının kaydedilmesi
start = time.time()

# Cihaz yedekleme fonksiyonu tanımlanması
def backup(device):
    # SSH bağlantısının kurulması
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')
    # Enable moduna geçiş
    connection.enable()

    # 'show run' komutunun gönderilmesi ve çıktının alınması
    output = connection.send_command('sh run')
    # print(output)

    # Komut isteminin (prompt) bulunması
    prompt = connection.find_prompt()
    # Hostname'in prompt'tan çıkarılması
    hostname = prompt[0:-1]

    # Dosya adının oluşturulması için tarih ve saat bilgisinin alınması
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # Dosya adının oluşturulması
    filename = f'{hostname}-{year}-{month}-{day}-backup.txt'

    # Çıktının dosyaya yazılması
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 40)

    # Bağlantının kapatılması
    print('Closing connection')
    connection.disconnect()

# Cihaz IP adreslerinin 'devices.txt' dosyasından okunması
with open('devices.txt') as f:
    devices = f.read().splitlines()

# İş parçacıkları listesi oluşturulması
threads = list()
# Her bir cihaz için iş parçacığı oluşturma
for ip in devices:
    # Cihaz bilgileri sözlüğünün oluşturulması
    device = {
        'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
        'host': ip,                  # Cihazın IP adresi
        'username': 'admin',         # SSH bağlantısı için kullanıcı adı
        'password': 'admin',         # SSH bağlantısı için şifre
        'port': '22',                # SSH bağlantısı için port (genellikle 22)
        'secret': 'cisco',           # Enable moduna geçiş için şifre
        'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
    }
    # Yedekleme fonksiyonunu çalıştıracak bir iş parçacığı (thread) oluşturulması
    th = threading.Thread(target=backup, args=(device,))
    # İş parçacığının listeye eklenmesi
    threads.append(th)

# İş parçacıklarının başlatılması
for th in threads:
    th.start()

# İş parçacıklarının tamamlanmasının beklenmesi
for th in threads:
    th.join()

# Bitiş zamanının kaydedilmesi
end = time.time()

# Toplam çalıştırma süresinin hesaplanması ve yazdırılması
print(f'Total execution time: {end-start}')


##################################################################################################################
##################################################################################################################
##################################################################################################################



# Detaylı Açıklamalar:
# 1. Gerekli Kütüphanelerin İçe Aktarılması:
#    # netmiko kütüphanesinden ConnectHandler sınıfının içe aktarılması
#    from netmiko import ConnectHandler
#    # datetime modülünden datetime sınıfının içe aktarılması (dosya isimlendirmede kullanmak için)
#    from datetime import datetime
#    # time modülünün içe aktarılması (toplam süreyi hesaplamak için)
#    import time
#    # threading modülünün içe aktarılması (çoklu iş parçacığı için)
#    import threading
#    - `netmiko`: Ağ cihazlarıyla SSH bağlantısı kurmayı ve komut göndermeyi kolaylaştıran bir kütüphane.
#    - `ConnectHandler`: Netmiko'nun ağ cihazlarına bağlanmak için kullandığı sınıf.
#    - `datetime`: Tarih ve saat bilgisi almak için kullanılan modül.
#    - `time`: Zamanla ilgili fonksiyonlar sunan modül.
#    - `threading`: Paralel iş parçacıkları oluşturmayı sağlayan modül.
#
# 2. Başlangıç Zamanının Kaydedilmesi:
#    # Başlangıç zamanının kaydedilmesi
#    start = time.time()
#    - İşlemlerin başlangıç zamanını kaydeder.
#
# 3. Yedekleme Fonksiyonunun Tanımlanması:
#    # Cihaz yedekleme fonksiyonu tanımlanması
#    def backup(device):
#        - Her cihaz için yedekleme işlemini gerçekleştiren fonksiyon.
#
# 4. SSH Bağlantısının Kurulması:
#        # SSH bağlantısının kurulması
#        connection = ConnectHandler(**device)
#        print('Entering the enable mode...')
#        - `ConnectHandler` sınıfı kullanılarak SSH bağlantısı kurulur.
#
# 5. Enable Moduna Geçiş:
#        # Enable moduna geçiş
#        connection.enable()
#        - Cihazın yetkili moduna (enable mode) geçiş yapılır.
#
# 6. 'show run' Komutunun Gönderilmesi:
#        # 'show run' komutunun gönderilmesi ve çıktının alınması
#        output = connection.send_command('sh run')
#        - `send_command` fonksiyonu ile 'sh run' komutu cihaza gönderilir ve çıktısı alınır.
#
# 7. Hostname'in Çıkarılması:
#        # Komut isteminin (prompt) bulunması
#        prompt = connection.find_prompt()
#        # Hostname'in prompt'tan çıkarılması
#        hostname = prompt[0:-1]
#        - Prompt'tan hostname'i çıkarır. Genellikle prompt son karakter olarak '#' içerir.
#
# 8. Dosya Adının Oluşturulması:
#        # Dosya adının oluşturulması için tarih ve saat bilgisinin alınması
#        now = datetime.now()
#        year = now.year
#        month = now.month
#        day = now.day
#        # Dosya adının oluşturulması
#        filename = f'{hostname}-{year}-{month}-{day}-backup.txt'
#        - Hostname ve tarih bilgisine dayalı olarak yedekleme dosyasının adı oluşturulur.
#
# 9. Çıktının Dosyaya Yazılması:
#        # Çıktının dosyaya yazılması
#        with open(filename, 'w') as backup:
#            backup.write(output)
#            print(f'Backup of {hostname} completed successfully')
#            print('#' * 40)
#        - Dosya yazma modunda açılır ve 'show run' komutunun çıktısı dosyaya yazılır.
#
# 10. Bağlantının Kapatılması:
#        # Bağlantının kapatılması
#        print('Closing connection')
#        connection.disconnect()
#        - `disconnect` fonksiyonu kullanılarak SSH bağlantısı kapatılır.
#
# 11. Cihaz IP Adreslerinin Okunması:
#    # Cihaz IP adreslerinin 'devices.txt' dosyasından okunması
#    with open('devices.txt') as f:
#        devices = f.read().splitlines()
#    - 'devices.txt' dosyasındaki IP adresleri okunur ve listeye dönüştürülür.
#
# 12. İş Parçacıkları Listesinin Oluşturulması:
#    # İş parçacıkları listesi oluşturulması
#    threads = list()
#    - İş parçacıklarını saklamak için boş bir liste oluşturulur.
#
# 13. Her Bir Cihaz İçin İş Parçacığı Oluşturma:
#    # Her bir cihaz için iş parçacığı oluşturma
#    for ip in devices:
#        # Cihaz bilgileri sözlüğünün oluşturulması
#        device = {
#            'device_type': 'cisco_ios',  # Cihazın türü (Cisco IOS)
#            'host': ip,                  # Cihazın IP adresi
#            'username': 'admin',         # SSH bağlantısı için kullanıcı adı
#            'password': 'admin',         # SSH bağlantısı için şifre
#            'port': '22',                # SSH bağlantısı için port (genellikle 22)
#            'secret': 'cisco',           # Enable moduna geçiş için şifre
#            'verbose': True              # Bağlantı sırasında ayrıntılı çıktı sağlama
#        }
#        # Yedekleme fonksiyonunu çalıştıracak bir iş parçacığı (thread) oluşturulması
#        th = threading.Thread(target=backup, args=(device,))
#        # İş parçacığının listeye eklenmesi
#        threads.append(th)
#
# 14. İş Parçacıklarının Başlatılması:
#    for th in threads:
#        th.start()
#    - Her bir iş parçacığını başlatmak için threads listesindeki her bir iş parçacığı için `start()` methodu çağrılır. Bu adım, her iş parçacığının ayrı ayrı çalışmasını başlatır.
#
# 15. İş Parçacıklarının Tamamlanmasının Beklenmesi:
#    for th in threads:
#        th.join()
#    - Her iş parçacığının `join()` methodu ile tamamlanmasını bekler. Bu adım, tüm iş parçacıklarının bitirmesini sağlar ve programın devam etmesi için bekler.
#
# 16. Bitiş Zamanının Kaydedilmesi:
#    # Bitiş zamanının kaydedilmesi
#    end = time.time()
#    - İşlemlerin bitiş zamanını kaydeder.
#
# 17. Toplam Çalışma Süresinin Hesaplanması ve Yazdırılması:
#    # Toplam çalıştırma süresinin hesaplanması ve yazdırılması
#    print(f'Total execution time: {end-start}')
#    - Programın başlangıç ve bitiş zamanları arasındaki farkı hesaplayarak, toplam çalışma süresini hesaplar ve ekrana yazdırır.
#
# Bu adımlar, her bir Cisco IOS cihazı için aynı anda yedekleme işlemlerini gerçekleştirmek için çoklu iş parçacıkları kullanarak,
# işlemleri paralel hale getirir. Her bir iş parçacığı ayrı bir SSH bağlantısı oluşturur ve cihazdan 'show run' komutu ile yapılandırma bilgisini alarak,
# bunu bir dosyaya kaydeder. Son olarak, iş parçacıkları tamamlandığında toplam çalışma süresini raporlar.




##################################################################################################################
##################################################################################################################
##################################################################################################################