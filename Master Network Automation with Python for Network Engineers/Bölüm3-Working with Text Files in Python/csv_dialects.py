import csv

"""

# 'passwd.csv' adlı dosyayı okuma modunda ('r' - read) açıyoruz.
# 'with' kullanımı, dosyanın işlemler tamamlandığında otomatik olarak kapanmasını sağlar.
# Bu, dosya işlemleri sırasında oluşabilecek olası hatalarda kaynak sızıntısını önler.
with open('passwd.csv', 'r') as f:
    # csv.reader fonksiyonunu kullanarak dosyanın içeriğini okuyoruz.
    # 'delimiter' parametresi, sütunlar arasındaki ayırıcı karakteri ':' olarak belirler.
    # 'lineterminator' parametresi, satır sonu karakterini '\n' olarak belirler.
    # Bu ayarlar genellikle Unix/Linux sistemlerindeki /etc/passwd dosyasının biçimini simüle eder.
    reader = csv.reader(f, delimiter=':', lineterminator='\n')

    # reader nesnesi, dosyadaki her satırı bir liste olarak döndürecek.
    # Bu döngü, dosyadaki her bir satırı sırasıyla işler.
    for row in reader:
        # Her satırı (bir liste olarak) ekrana yazdırıyoruz.
        # Bu, dosyadaki her bir satırın ':' ile ayrılmış alanlarını bir liste olarak gösterir.
        print(row)

# Bu kod, 'passwd.csv' dosyasını ':' ile ayrılmış sütunlar ve '\n' ile sonlandırılmış satırlar olarak okur.
# Her bir satır bir liste olarak temsil edilir ve bu listeler ekrana yazdırılır.
# Bu, dosya içeriğini analiz etmek veya işlemek için başlangıç noktası sağlar

print(csv.list_dialects())

"""




# CSV dialekti tanımlıyoruz. Bu, CSV dosyasının nasıl okunacağını belirten bir yapılandırmadır.
# 'delimiter' parametresi, her bir sütun arasındaki ayırıcı karakteri belirtir. Bu örnekte, '#' kullanılmıştır.
# 'quoting=csv.QUOTE_NONE' parametresi, hücrelerin alıntılanmasını gerektirmediğini belirtir.
# 'lineterminator' parametresi, satır sonu karakterini belirtir. Bu örnekte '\n' kullanılmıştır.
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

# 'items.csv' dosyasını okuma modunda ('r') açıyoruz.
# 'with' ifadesi, dosyanın kullanımı tamamlandığında otomatik olarak kapatılmasını sağlar.
with open('items.csv', 'r') as csvfile:
    # csv.reader fonksiyonunu kullanarak dosyanın içeriğini okuyoruz.
    # 'dialect' parametresi, daha önce tanımladığımız 'hashes' dialektini kullanmamızı sağlar.
    reader = csv.reader(csvfile, dialect='hashes')

    # reader nesnesi, dosyadaki her satırı bir liste olarak döndürecektir.
    # Bu döngü, dosyadaki her bir satırı tek tek işler.
    for row in reader:
        # Her satırı (bir liste olarak) ekrana yazdırıyoruz.
        # Bu, dosyadaki her bir satırın '#' ile ayrılmış alanlarını bir liste olarak gösterir.
        print(row)

# Bu kod, 'items.csv' dosyasını '#' karakteri ile ayrılmış sütunlar ve '\n' ile sonlandırılmış satırlar olarak okur.
# Her bir satır bir liste olarak temsil edilir ve bu listeler ekrana yazdırılır.
# csv.register_dialect fonksiyonu, dosyanın okunma biçimini özelleştirmek için kullanılır.
# Bu örnekte, '#', hücreleri ayırmak için kullanılan ayırıcı karakterdir.

"""
    Açıklamalar:
        1- CSV Dialektini Tanımlama:

    * csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n'):

    * 'hashes': Bu dialekti belirten ad. Diğer yerlerde bu adı kullanarak bu yapılandırmayı referans alacağız.

    * delimiter='#': Hücreler arasındaki ayırıcı karakteri belirler. Burada '#' kullanılmıştır.
    
    * quoting=csv.QUOTE_NONE: Hücrelerin alıntılanmasını gerektirmediğimizi belirtir. 
      Bu, hücrelerde alıntı olmadan verilerin okunmasını sağlar.

    * lineterminator='\n': Satır sonu karakterini belirtir. 
      Bu örnekte, her satırın sonu yeni bir satır ('\n') karakteri ile bitmektedir.
      
        2- Dosyanın Açılması ve Okunması:

    * with open('items.csv', 'r') as csvfile::
        
        * 'items.csv' dosyasını okuma modunda açar.

        * with ifadesi, dosyanın işlemleri tamamlandığında otomatik olarak kapatılmasını sağlar, 
          bu da kaynak yönetimini kolaylaştırır.
          
        3- Reader Nesnesinin Kullanımı:

    * reader = csv.reader(csvfile, dialect='hashes'):
    
     
        * csv.reader fonksiyonunu kullanarak dosyanın içeriğini okur.
     
        * dialect='hashes': Daha önce tanımladığımız 'hashes' dialektini kullanır.



        4- Satırların İşlenmesi:

    * for row in reader::
    
        * reader nesnesi, dosyadaki her satırı bir liste olarak döndürür.
        
        *Bu döngü, dosyadaki her bir satırı tek tek işler.

    * print(row):
        
        * Her satırı bir liste olarak ekrana yazdırır. Bu, dosyanın içeriğini görsel olarak incelememizi sağlar.


Ekstra Bilgi:
    Dialektlerin Kullanımı:
    
    Dialektler, CSV dosyalarının farklı biçimlerde okunmasını sağlar. Özelleştirilmiş bir dialekt, 
    belirli bir dosya formatı için özel kurallar tanımlamak için kullanılır.    

"""

# 'items.csv' dosyasına yeni veri eklemek için 'a' (append) modunda açıyoruz.
# 'with' ifadesi, dosyanın kullanımı tamamlandığında otomatik olarak kapatılmasını sağlar.
with open('items.csv', 'a') as csvfile:
    # csv.writer fonksiyonunu kullanarak dosyaya yazma işlemi için bir writer nesnesi oluşturuyoruz.
    # 'dialect' parametresi, daha önce tanımladığımız 'hashes' dialektini kullanmamızı sağlar.
    writer = csv.writer(csvfile, dialect='hashes')

    # writer.writerow fonksiyonuyla yeni bir satır ekliyoruz.
    # Parametre olarak bir liste veriyoruz. Her bir öğe, CSV dosyasındaki sırasıyla sütunlara karşılık gelir.
    writer.writerow(['spoon', 3, 1.5])

# Bu kod, 'items.csv' dosyasına yeni bir satır ekler.
# Dosya, '#' ile ayrılmış sütunlar ve '\n' ile sonlandırılmış satırlar olarak işlenir.
# 'csv.writer' fonksiyonu, verilen dialekt ve dosya ile birlikte kullanılarak CSV dosyasına veri yazma işlemini yönetir.
# writer.writerow fonksiyonu, dosyaya veri eklemek için kullanılır. Verilen liste, CSV dosyasındaki bir satıra denk gelir.




















