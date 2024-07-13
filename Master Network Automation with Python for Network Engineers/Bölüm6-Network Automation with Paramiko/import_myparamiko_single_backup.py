# Gerekli Kütüphanelerin İçe Aktarılması
import time
import myparamiko

# Router Bilgilerinin Tanımlanması
router1 = {
    'server_ip': '192.168.146.10',  # Router'ın IP adresi
    'server_port': '22',            # SSH portu (genellikle 22)
    'user': 'admin',                # Kullanıcı adı
    'passwd': 'admin'               # Şifre
}

# Router'a Bağlantı Kurulması
client = myparamiko.connect(**router1)

# Shell Elde Edilmesi
shell = myparamiko.get_shell(client)

# Terminal Uzunluğunun Ayarlanması
myparamiko.send_command(shell, 'terminal len 0')  # Terminal çıktısının uzunluğunu sınırsız yap

# Yapılandırma Çıktısının Alınması
myparamiko.send_command(shell, 'show run')  # Router yapılandırmasını göster

# Bekleme Süresi
time.sleep(3)  # 4 saniye bekle, komutun tamamlanmasını sağla

# Komut Çıktısının Alınması
output = myparamiko.show(shell)

# Çıktının İşlenmesi
output_list = output.splitlines()  # Çıktıyı satır satır ayır
output = '\n'.join(output_list)    # Satırları yeniden birleştir


from  datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router1['server_ip']}_{year}-{month}-{day}.txt'
print(file_name)

# Çıktının Dosyaya Yazılması
with open(file_name, 'w') as f:
    f.write(output)  # İşlenmiş çıktıyı dosyaya yaz

# Bağlantının Kapatılması
myparamiko.close(client)  # SSH bağlantısını kapat
