# Gerekli Kütüphanelerin İçe Aktarılması
import paramiko
import time


# Bağlantı Fonksiyonu
def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(
        hostname=server_ip,
        port=server_port,
        username=user,
        password=passwd,
        look_for_keys=False,
        allow_agent=False
    )
    return ssh_client


# Shell Alma Fonksiyonu
def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell


# Komut Gönderme Fonksiyonu
def send_command(shell, command, timout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timout)


# Çıktı Alma Fonksiyonu
def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()


# Bağlantı Kapatma Fonksiyonu
def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()


# Ana Program
if __name__ == '__main__':
    # Router Bilgilerinin Tanımlanması
    router1 = {
        'server_ip': '192.168.146.10',  # Router'ın IP adresi
        'server_port': '22',  # SSH portu (genellikle 22)
        'user': 'admin',  # Kullanıcı adı
        'passwd': 'admin'  # Şifre
    }

    # Router'a Bağlantı Kurulması
    client = connect(**router1)

    # Shell Elde Edilmesi
    shell = get_shell(client)

    # Komutların Gönderilmesi
    send_command(shell, 'term len 0')  # Terminal çıktısının uzunluğunu sınırsız yap
    send_command(shell, 'sh version')  # Router yazılım versiyonunu göster
    send_command(shell, 'sh ip int brief')  # Router IP arayüz özet bilgisini göster

    # Çıktının Alınması
    output = show(shell)
    print(output)

    # Bağlantının Kapatılması
    close(client)











































import paramiko
import time

def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd,
                       look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'server_ip': '192.168.146.10', 'server_port': '22', 'user':'admin', 'passwd':'admin'}
    client = connect(**router1)
    shell = get_shell(client)


    send_command(shell, 'term len 0')
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')

    output = show(shell)
    print(output)



# client = connect('192.168.146.10', '22', 'admin', 'admin')
# shell = get_shell(client)
#
# send_command(shell, 'terminal len 0')
# send_command(shell, 'show version')
# send_command(shell, 'sh ip int brief')
#
# output = show(shell)
#
# print(output)

