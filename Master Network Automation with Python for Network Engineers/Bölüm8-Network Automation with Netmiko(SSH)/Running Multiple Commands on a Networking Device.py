from netmiko import ConnectHandler


cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.146.10',
    'username': 'admin',
    'password': 'admin',
    'port': '22',
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()


commands = ['int loopback 0', ' ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']

output = connection.send_config_set(commands)

print(output)
print(connection.find_prompt())

connection.send_command('write memory')



print('Closing connection')
connection.disconnect()