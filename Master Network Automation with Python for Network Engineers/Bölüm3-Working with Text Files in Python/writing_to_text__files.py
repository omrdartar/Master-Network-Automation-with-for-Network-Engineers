# WRITING TO TEXT FILES

with open('myfile.txt', 'w') as f:
    f.write('Just a line')

"""

Burad myfile diye bir dosya olmasa ile bile write ettiğimiz için kendisi olusturup f.write() içine yazdıklarımızı
yazacaktır. 


"""


with open('myfile.txt', 'w') as f:
    f.write('Just a line.\n')
    f.write('Just 2nd line.\n')

"""

 '\n' ile komutları alt satıra geçirebiliriz. 


"""


with open('myfile.txt', 'a') as f:
    f.write('Some Text Here.\n')
    f.write('Another Text.\n')


"""

 'a' komutu ile var olan bir dosya ya ek olarak yazabiliriz. 


"""

with open('myfile.txt', 'r+') as f:
    f.seek(5)
    f.write('100')


"""

 eğer burada 'r+' ile işlem yapar ve seek ile kaçıncı byte'dan sonra başlamasını istersek bu şekildede yapabiliriz.


"""





















