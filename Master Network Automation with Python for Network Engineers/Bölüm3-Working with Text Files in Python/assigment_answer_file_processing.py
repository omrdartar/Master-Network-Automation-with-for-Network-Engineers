



with open('devicess.txt') as f:
    devices = f.read().splitlines()
    print(devices)



my_list = list()
for item in devices:
    tmp = item.split(':')
    print(tmp)

for item in devices:
    tmp = item.split(':')
    my_list.append(tmp)
print(my_list)
















