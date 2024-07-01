import paramiko
import time
import getpass


# SSHClient nesnesi oluşturma
ssh_client = paramiko.SSHClient()

# Uzak sunucunun SSH anahtarını otomatik olarak kabul etme politikası belirleme
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Kullanıcıdan güvenli bir şekilde parola isteme
password = getpass.getpass('Enter password:')

# SSH bağlantısını kurmak için gereken parametreleri bir sözlük (dictionary) olarak tanımlama
router = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': password}

# Kullanıcıya SSH bağlantısı kurulacağını belirten bir bilgi mesajı yazdırma
print(f'Connecting to {router["hostname"]}')

# Birleştirilmiş sözlüğü kullanarak SSH bağlantısı kurma
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# SSH bağlantısı üzerinden bir shell (kabuk) nesnesi oluşturma
shell = ssh_client.invoke_shell()

# Uzak cihazda komutları çalıştırmak için komut gönderme
# Her komut '\n' ile biter (yeni satır, enter tuşu)
shell.send('terminal length 0\n')  # Çıktının sayfalara bölünmesini engeller
shell.send('show version\n')       # Cihazın yazılım versiyonunu gösterir
shell.send('show ip int brief\n')  # IP arabirimlerinin özetini gösterir

# Uzak cihazın komutları çalıştırmasını beklemek için bekleme süresi (zorunlu)
time.sleep(1)

# Shell'in çıkış tamponundan veri okuma
output = shell.recv(10000)  # Çıkış tamponundan 10000 byte okuma

# Okunan veriyi bayt türünden string türüne dönüştürme
output = output.decode('utf-8')
print(output)

# Bağlantı aktifse kapatma
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()











# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # prompting for the user's password securely
# password = getpass.getpass('Enter password:')
# router = {'hostname': '192.168.146.10', 'port': '22', 'username':'admin', 'password': password}
# print(f'Connecting to {router["hostname"]}')
# ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
# shell = ssh_client.invoke_shell()
# shell.send('terminal length 0\n')
# shell.send('show version\n')
# shell.send('show ip int brief\n')
# time.sleep(1)
# output = shell.recv(10000)
# # print(type(output))
# output = output.decode('utf-8')
# print(output)
# if ssh_client.get_transport().is_active() == True:
#     print('Closing connection')
#     ssh_client.close()