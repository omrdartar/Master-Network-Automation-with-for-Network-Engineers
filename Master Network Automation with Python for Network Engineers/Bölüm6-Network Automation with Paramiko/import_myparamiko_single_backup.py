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

# Çıktının Dosyaya Yazılması
with open('router1-backup.txt', 'w') as f:
    f.write(output)  # İşlenmiş çıktıyı dosyaya yaz

# Bağlantının Kapatılması
myparamiko.close(client)  # SSH bağlantısını kapat
