

balance = int(input("Lutfen bir sayi giriniz: "))
price = int(input("Lutfen bir fiyat giriniz: "))

if balance >= price:
    new_balance = balance - price
    print(f'You can book the flight and your new balance will be {new_balance}')
else:
    print(f'Insufficient funds! Please deposiit {price - balance}')





















