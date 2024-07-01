

with open('configuration.txt') as file:
    content = file.read()
    print(content)


"""
Yukarıdaki örnekte daha öncesinde değişkeni norma ' f = open('configuration.txt', 'r') şeklinde açtığımızda
işlemlerin sonun file.close() yazmadan print(file.closed) yazdıgımızda false verirdi fakat şuan işlemi with ile
yaptığımız için işlemi tamamladığında dosyayı kendisi kapatıyor.
 
"""

file.read()

"""

Yukarıdaki gibi wiht den sonra gidip dosyayı okumak istediğimizde Aşağıdaki hatayı verecektir.

'ValueError: I/O operation on closed file.'


"""