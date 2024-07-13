import paramiko
from scp import SCPClient


ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, port=22, username=username, password=password, allow_agent=False, look_for_keys=False)


scp = SCPClient(ssh_client.get_transport())

scp.put('devices.txt')