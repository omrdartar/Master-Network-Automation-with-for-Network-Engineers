

balance = int(input("Lutfen bir sayi giriniz: "))
price = int(input("Lutfen bir fiyat giriniz: "))

if balance >= price:
    answer = input("Do you want to continue ? Yes or No ?: ")
    answer.lower()
    if answer == 'yes':
        print("We'll move on")
    elif answer == 'no':
        print("We'll stop")
    else:
        print("invaild answer")
    new_balance = balance - price
    print(f'You can book the flight and your new balance will be {new_balance}')
else:
    print(f'Insufficient funds! Please deposiit {price - balance}')





















