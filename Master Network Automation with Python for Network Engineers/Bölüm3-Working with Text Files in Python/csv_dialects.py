import csv

# 'with' kullanımı, dosyanın işlemler tamamlandığında otomatik olarak kapanmasını sağlar.
with open('passwd.csv', 'r') as f:
    # csv.reader fonksiyonunu kullanarak dosyanın içeriğini okuyoruz.
    # 'delimiter' parametresi, sütunlar arasındaki ayırıcı karakteri ':' olarak belirler.
    # 'lineterminator' parametresi, satır sonu karakterini '\n' olarak belirler.
    reader = csv.reader(f, delimiter=':', lineterminator='\n')

    # reader nesnesi, dosyadaki her satırı bir liste olarak döndürecek.
    # Bu döngü, her satırı tek tek işler.
    for row in reader:
        # Her satırı (bir liste olarak) ekrana yazdırıyoruz.
        print(row)

# Bu kod, 'passwd.csv' dosyasını ':' ile ayrılmış sütunlar ve '\n' ile sonlandırılmış satırlar olarak okur.
# Her bir satır bir liste olarak temsil edilir ve bu listeler ekrana yazdırılır.

