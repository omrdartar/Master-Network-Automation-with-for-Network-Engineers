import csv






with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)

"""


Python kodu people.csv adında bir CSV dosyasına yeni bir satır ekler. İşte adım adım açıklaması:

with open('people.csv', 'a') as csvfile:: Bu satırda, mevcut bir people.csv dosyasını açıyoruz veya 
dosya yoksa oluşturuyoruz ('a' moduyla, yani ekleme modunda). Bu mod, dosyanın sonuna yeni veriler eklememizi sağlar. 
as csvfile ifadesiyle dosyayı csvfile adında bir değişkene atıyoruz, böylece bu değişken aracılığıyla dosyaya erişebiliriz.



writer = csv.writer(csvfile): csv.writer fonksiyonuyla, 
csvfile üzerinde yazma işlemi yapacak bir yazıcı (writer) oluşturulur.



csvdata = (5, 'Anne', 'Amsterdam'): csvdata adında bir tuple oluşturulur. 
Bu tuple'da sırasıyla bir ID (5), bir isim ('Anne') ve bir şehir ('Amsterdam') bilgileri bulunmaktadır.



writer.writerow(csvdata): writerow metodu kullanılarak csvdata tuple'ı CSV dosyasına yazılır. 
Yani, people.csv dosyasının sonuna yeni bir satır eklenir ve bu satırda 5, Anne, Amsterdam bilgileri sırasıyla yer alır.



Bu kod parçası, mevcut bir CSV dosyasına veya yeni oluşturduğumuz bir CSV dosyasına veri eklemek için kullanılır. 
Dosyanın sonuna csvdata tuple'ındaki verileri içeren bir satır ekler.


"""





with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])

"""

Python programı bir CSV dosyası oluşturur ve her satırda bir matematiksel işlem sonucunu içerir. 
İşte programın adım adım açıklaması:



with open('numbers.csv', 'w', newline='') as f:: Bu satırda, numbers.csv isimli bir dosya oluşturuyoruz 
('w' moduyla, yani yazma modunda). newline='' parametresi, yeni satır karakterlerinin otomatik 
olarak eklendiğini önler, böylece dosyaya yazılan satırlar arasında ek bir boş satır oluşmaz. 
as f ifadesi ise dosyayı f adında bir değişkene atar, böylece bu değişken aracılığıyla dosyaya erişebiliriz.




writer = csv.writer(f): csv.writer fonksiyonuyla, f (yani numbers.csv dosyası) 
üzerinde yazma işlemi yapacak bir yazıcı (writer) oluşturulur.




writer.writerow(['x', 'x**2', 'x**3', 'x**4']): İlk olarak, CSV dosyasının başlığını belirlemek için 
writerow metoduyla bir satır yazılır. Bu satırda, sırasıyla 'x', 'x2', 'x3', 'x**4' başlıkları yer alır.



for x in range(1, 101):: Bu satırda for döngüsü kullanılarak 1 ile 100 arasındaki 
sayılar (range(1, 101) ile ifade edilir) üzerinde iterasyon yapılır.



writer.writerow([x, x**2, x**3, x**4]): Her iterasyonda, x, x**2, x**3, x**4 değerlerini hesaplayarak 
bir liste oluşturulur ve bu liste writerow metoduyla CSV dosyasına yazılır. 
Yani her satırda x değeri ve bu değerlerin sırasıyla karesi, kübü ve dördüncü kuvveti yer alır.




Sonuç olarak, bu program numbers.csv adında bir dosya oluşturacak ve dosyaya 1'den 100'e kadar olan sayıların karesi, 
kübü ve dördüncü kuvvetini içeren bir tablo yazacaktır. Her satırda bir sayı ve bu sayının üç farklı kuvveti bulunacaktır.

"""





















