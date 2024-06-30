# OPENING AND READING FILES

f = open('configuration.txt', 'r')      # Burada f diye bir değişken oluşturup f değişkeninde open ile çalışma klasörümüzde bulunan
                                        # 'configuration.txt' doyasına 'r' komutu ile okuma yetkisi veririz.

content = f.read()                      # sonrasında content diye bir değişken oluşturup f değişkenini okumasını sağlarız.
print(content)                          # daha sonra content değişkenini çalıştırdıgımızda, 'configuration.tx' dosyasının içeriğini yazdıracaktır.
print(f.closed)                         # Burada dosyanın kapı oldugunu söyleriz bize dosya haala açık oldugu için false döner.
f.close()                               # Burada f değişkenini f.close ile kapattırız.
print(f.closed)                         # Burada dosyanın kapalı oldugunu tekrar söylediğimizde artık True değeri dönecektir.
















































