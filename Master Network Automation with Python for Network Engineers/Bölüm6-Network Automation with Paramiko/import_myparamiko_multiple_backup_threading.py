# Gerekli kütüphanelerin içe aktarılması
import time
import myparamiko
import threading


# Yedekleme fonksiyonu
# Bu fonksiyon, verilen router bilgileri ile SSH bağlantısı kurar, yapılandırma bilgisini alır ve dosyaya yazar.
def backup(router):
    # Router'a bağlantı kurulması
    client = myparamiko.connect(
        **router)  # myparamiko kütüphanesindeki connect fonksiyonu kullanılarak SSH bağlantısı kurulur.

    # Shell elde edilmesi
    shell = myparamiko.get_shell(client)  # SSH bağlantısından interaktif shell (komut satırı) elde edilir.

    # Terminal uzunluğunun ayarlanması
    myparamiko.send_command(shell, 'terminal len 0')  # Terminal çıktısının uzunluğunu sınırsız yap

    # Yapılandırma çıktısının alınması
    myparamiko.send_command(shell, 'show run')  # Router yapılandırmasını göster

    # Bekleme süresi
    time.sleep(3)  # 3 saniye bekle, komutun tamamlanmasını sağla

    # Komut çıktısının alınması
    output = myparamiko.show(shell)  # Komutun çıktısı alınır

    # Çıktının işlenmesi
    output_list = output.splitlines()  # Çıktıyı satır satır ayır
    output = '\n'.join(output_list)  # Satırları yeniden birleştir

    from datetime import datetime

    # Tarih ve saat bilgisinin alınması
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    # Dosya adının oluşturulması
    file_name = f"{router['server_ip']}_{year}-{month}-{day}.txt"  # Dosya adı, router'ın IP adresi ve tarih bilgisiyle oluşturulur.

    # Çıktının dosyaya yazılması
    with open(file_name, 'w') as f:  # Dosya yazma modunda açılır.
        f.write(output)  # İşlenmiş çıktıyı dosyaya yaz

    # Bağlantının kapatılması
    myparamiko.close(client)  # SSH bağlantısını kapat


# Router bilgilerinin tanımlanması
router1 = {
    'server_ip': '192.168.146.10',  # Router'ın IP adresi
    'server_port': '22',  # SSH portu (genellikle 22)
    'user': 'admin',  # Kullanıcı adı
    'passwd': 'admin'  # Şifre
}

router2 = {
    'server_ip': '192.168.146.20',  # Router'ın IP adresi
    'server_port': '22',  # SSH portu (genellikle 22)
    'user': 'admin',  # Kullanıcı adı
    'passwd': 'admin'  # Şifre
}

router3 = {
    'server_ip': '192.168.146.30',  # Router'ın IP adresi
    'server_port': '22',  # SSH portu (genellikle 22)
    'user': 'admin',  # Kullanıcı adı
    'passwd': 'admin'  # Şifre
}

# Router listesi
routers = [router1, router2, router3]  # Tüm router'ları içeren bir liste

# Thread listesi
threads = list()  # Thread nesnelerini saklamak için boş bir liste oluşturulur

# Her bir router için thread oluşturma ve başlatma
for router in routers:
    # Thread nesnesi oluşturma. 'backup' fonksiyonunu ve ilgili router bilgisini thread'e geçiriyoruz.
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)  # Thread'i listeye ekleme

# Thread'leri başlatma
for th in threads:
    th.start()  # Her bir thread başlatılır ve 'backup' fonksiyonunu çalıştırır

# Thread'lerin tamamlanmasını bekleme
for th in threads:
    th.join()  # Ana program, tüm thread'ler tamamlanana kadar bekler
