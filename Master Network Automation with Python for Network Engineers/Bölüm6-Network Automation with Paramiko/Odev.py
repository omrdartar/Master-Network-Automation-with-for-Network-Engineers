import paramiko
import getpass
import time

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('Connecting to 192.168.146.10')

my_password = getpass.getpass('Enter your password:')

ssh_client.connect(hostname='192.168.146.10', port='22', username='admin', password=my_password,
                   look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()
shell.send('show users\n')
time.sleep(1)

output = shell.recv(100000).decode()
print(output)


with open('show-users.txt', 'w') as f:
    f.write(output)

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()