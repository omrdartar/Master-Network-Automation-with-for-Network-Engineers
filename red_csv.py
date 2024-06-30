import csv


# with open('airtravel.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)



with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]

    print(year_1958)

    max_1958 = max(year_1958.values())
    print(max_1958)

    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Busiest Month in 1958: {k}, Flights:{v.strip()}')

"""

Tabii, bu kod parçası bir CSV dosyasından verileri okur, 
1958 yılına ait yolcu sayısını bir sözlükte toplar ve bu yıl için en yüksek yolcu sayısını bulur. 
İşte bu kodun adım adım açıklaması:

    1-CSV Dosyasını Açma ve Okuyucu Oluşturma:


with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
with open('airtravel.csv', 'r') as f:: "airtravel.csv" adlı dosyayı okuma modunda açar ve f adında bir dosya nesnesi oluşturur.

reader = csv.reader(f): csv.reader fonksiyonunu kullanarak dosyayı okuyan bir CSV okuyucu (reader) oluşturur.

next(reader): İlk satırı (genellikle başlık satırı) atlar.



    2- 1958 Yılına Ait Verileri Sözlükte Toplama:


year_1958 = dict()
for row in reader:
    year_1958[row[0]] = row[1]
    
year_1958 = dict(): Boş bir sözlük (year_1958) oluşturur.

for row in reader:: Dosyadaki her satır (ilk satır atlanmıştı) için döngüye girer.

year_1958[row[0]] = row[1]: Satırın ilk elemanını (örneğin ay adı) anahtar, ikinci elemanını (1958 yılı yolcu sayısı) değer olarak sözlüğe ekler.



    4-En Yoğun Ayı Bulma ve Yazdırma:

python
Copy code
for k, v in year_1958.items():
    if max_1958 == v:
        print(f'Busiest Month in 1958: {k}, Flights:{v.strip()}')
for k, v in year_1958.items():: year_1958 sözlüğündeki her bir anahtar-değer çifti (ay ve yolcu sayısı) için döngüye girer.
if max_1958 == v:: Eğer o ayın yolcu sayısı en yüksek yolcu sayısına eşitse (en yoğun ay ise), aşağıdaki kodu çalıştırır.
print(f'Busiest Month in 1958: {k}, Flights:{v.strip()}'): 
En yoğun ayı ve o ayın yolcu sayısını yazdırır. f'Busiest Month in 1958: {k}, Flights:{v.strip()}' ifadesi, 
Python'da formatlı bir string (f-string) kullanarak mesajı oluşturur ve v.strip() ifadesi, yolcu sayısının etrafındaki gereksiz boşlukları temizler.





    5-1958 Yılındaki Verileri ve En Yüksek Yolcu Sayısını Yazdırma:


print(year_1958
max_1958 = max(year_1958.values())
print(max_1958)

print(year_1958): year_1958 sözlüğünü yazdırır.

max_1958 = max(year_1958.values()): Sözlükteki değerler (1958 yılı yolcu sayıları) arasında en büyük değeri bulur.

print(max_1958): En yüksek yolcu sayısını yazdırır.

Örnek bir airtravel.csv dosyası şu şekilde olabilir:

sql
Copy code
Month,1958,1959,1960
JAN,340,360,417
FEB,318,342,391
MAR,362,406,419
APR,348,396,461
MAY,363,420,472
JUN,435,472,535
JUL,491,548,622
AUG,505,559,606
SEP,404,463,508
OCT,359,407,461
NOV,310,362,390
DEC,337,405,432
Bu dosya ile çalıştırıldığında, kod şu çıktıyı verecektir:

arduino
Copy code
{'JAN': '340', 'FEB': '318', 'MAR': '362', 'APR': '348', 'MAY': '363', 'JUN': '435', 'JUL': '491', 'AUG': '505', 'SEP': '404', 'OCT': '359', 'NOV': '310', 'DEC': '337'}
505
Özetle, bu kod:

airtravel.csv dosyasını açar ve içeriğini okur.
1958 yılına ait yolcu sayılarını bir sözlükte toplar.
1958 yılına ait en yüksek yolcu sayısını bulur ve yazdırır.


"""















