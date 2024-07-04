import paramiko
import time


# SSHClient nesnesi oluşturma
ssh_client = paramiko.SSHClient()

# Host key doğrulama politikasını ayarlama
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Her cihaz için bir sözlük oluşturma
router1 = {'hostname': '192.168.146.10', 'port': '22', 'username': 'admin', 'password': 'admin'}
router2 = {'hostname': '192.168.146.20', 'port': '22', 'username': 'admin', 'password': 'admin'}
router3 = {'hostname': '192.168.146.30', 'port': '22', 'username': 'admin', 'password': 'admin'}

# Cihazların (router'ların) sözlüklerini içeren bir liste oluşturma
routers = [router1, router2, router3]

# Cihazlar üzerinde iterasyon yaparak yapılandırmayı yedekleme
for router in routers:
    print(f'Connecting to {router["hostname"]}')

    # SSH bağlantısı kurma
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    # Shell oturumu oluşturma
    shell = ssh_client.invoke_shell()

    # Komutları gönderme
    shell.send('conf t\n')  # Global configuration mode'a girme
    shell.send('router ospf 1\n')  # OSPF yönlendirme protokolü yapılandırma
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')  # OSPF ağı yapılandırma
    shell.send('end\n')  # Configuration mode'dan çıkma
    shell.send('terminal length 0\n')  # Çıktının sayfalara bölünmesini engelleme
    shell.send('sh ip protocols\n')  # Yönlendirme protokollerini gösterme
    shell.send('wr\n')  # Yönlendirme protokollerini gösterme
    time.sleep(2)  # Komutların yürütülmesi için bekleme süresi

    # Shell'in çıktı tamponundan okuma
    output = shell.recv(10000).decode()
    print(output)

    # Bağlantının aktif olup olmadığını kontrol etme ve kapatma
c










# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # creating a dictionary for each device to connect to
# router1 = {'hostname': '192.168.146.10', 'port': '22', 'username': 'admin', 'password': 'admin'}
# router2 = {'hostname': '192.168.146.20', 'port': '22', 'username': 'admin', 'password': 'admin'}
# router3 = {'hostname': '192.168.146.30', 'port': '22', 'username': 'admin', 'password': 'admin'}
#
# # creating a list of dictionaries (of devices)
# routers = [router1, router2, router3]
#
# # iterating over the list (over the devices) and backup the config
# for router in routers:
#     print(f'Connecting to {router["hostname"]}')
#     ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
#
#     shell = ssh_client.invoke_shell()
#
#
#
#     shell.send('conf t\n')
#     shell.send('router ospf 1\n')
#     shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
#     shell.send('end\n')
#     shell.send('terminal length 0\n')
#     shell.send('sh ip protocols\n')
#     time.sleep(2)
#
#     output = shell.recv(10000).decode()
#     print(output)
#
#     if ssh_client.get_transport().is_active() == True:
#         print('Closing connection...')
#         ssh_client.close()

