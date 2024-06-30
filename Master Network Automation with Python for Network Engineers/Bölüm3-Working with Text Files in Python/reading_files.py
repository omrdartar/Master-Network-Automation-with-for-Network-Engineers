

f = open('configuration.txt', 'r')
content = f.read(5)
# Burada configuration dosyasının içinde ki 0 dan başlayıp 5. karekter kadar okumasını sağlarız.

print(content)

content = f.read(3)
# Burada artık bir üstteki çıktıda 5 byte ileri gittiğimiz için oradan itibaren 3 byte ilerisini gösterir.
print(content)

print(f.tell())

# f.tell(): Dosya işaretçisinin mevcut konumunu döner.
# Bu konum, dosyanın başından itibaren kaç byte  ileride olunduğunu gösterir.
# Ornegin ikinci yaptıgımız content 20 olsaydı biz 20 byte ileri gittiğimiz için oradan geriye doğru gösterecekti.


"""

Özetle, print(f.tell()) ifadesi, dosya işaretçisinin mevcut konumunu ekrana yazdırarak, 
dosyada ne kadar ilerlenmiş olduğunu gösterir. 
Bu bilgi, dosyada belirli bir konumda işlem yapmak istendiğinde veya dosya işlemlerini izlemek gerektiğinde faydalıdır.

"""



t = open('configuration.txt', 'r')
t.seek(4)
content_1 = t.read(5)
print(content_1)

"""
t.seek(4) ifadesi burada okumaya hangi karekterden başlıcağını söyler content_1 de de 5 ileri gitmesini söylediğimiz
için bize 'name ' kısmını yazdırır. Boşukla birlikte 5 karekte

"""






