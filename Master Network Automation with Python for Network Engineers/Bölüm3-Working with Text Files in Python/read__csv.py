
import csv



"""

Burada bir csv dosyasının nasıl okunacagına ve print edileceğine bakıyoruz

"""
with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)








"""

Burada bir csv dosyasının içinde ki listin 1. lerini yazdırmalarının nasıl yapılacagına bakıyoruz.

"""
import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])








"""

Burada bir csv dosyasının içinde ki listin ilk satırını atlayıp  1. lerini yazdırmalarının nasıl yapılacagına bakıyoruz.

next(reader) diyerek

"""

import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)





























