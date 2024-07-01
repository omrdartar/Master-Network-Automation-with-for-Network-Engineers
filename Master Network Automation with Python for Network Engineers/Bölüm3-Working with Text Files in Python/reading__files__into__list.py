#READING FILES INTO A LIST

# 1. f.read().splitlines()

with open('configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
print('#' * 150)



"""

f.read().splitlines()
f.read():

f.read() komutu dosyanın tamamını okur ve içeriğini tek bir string olarak döner. 
Bu string, dosyadaki tüm satırları ve satır sonu karakterlerini içerir.


.splitlines():

.splitlines() metodu, bir string'i satır sonu karakterlerine göre böler 
ve her satırı ayrı bir liste elemanı olarak döner. 

Bu metot, satır sonu karakterlerini (\n, \r\n, vb.) otomatik olarak kaldırır.


content = f.read().splitlines()

Bu komut, dosyanın tamamını okur ve satır sonu karakterlerine göre böler, her bir satırı bir liste elemanı yapar. 
Satır sonu karakterleri listede yer almaz.

"""

# 2 f.readlines()
with open('configuration.txt') as f:
    content = f.readlines()
    print(content)


"""
f.readlines()
f.readlines():
f.readlines() komutu, dosyadaki tüm satırları okur ve her satırı bir liste elemanı olarak döner. Ancak, satır sonu karakterleri (\n) listede yer alır.

content = f.readlines()
Bu komut, dosyadaki tüm satırları okur ve her bir satırı satır sonu karakteriyle birlikte bir liste elemanı yapar.

"""


# Farklar

"""
Satır Sonu Karakterleri:

f.read().splitlines(): Satır sonu karakterlerini kaldırır.
f.readlines(): Satır sonu karakterlerini korur.
Performans:

f.read().splitlines(): İlk olarak dosyanın tamamını belleğe yükler, ardından satır sonu karakterlerine göre böler. 
Bu, büyük dosyalar için daha fazla bellek kullanımı anlamına gelir.
f.readlines(): Dosyayı satır satır okur ve her satırı bir liste elemanı olarak döner. 
Bu, özellikle büyük dosyalarda belleği daha verimli kullanabilir.
Hangi Durumda Hangisi Kullanılır?
Satır Sonu Karakterlerine İhtiyaç Yoksa:

f.read().splitlines(): Eğer satır sonu karakterlerini istemiyorsanız ve tüm dosyayı tek seferde belleğe yükleyebilecekseniz, bu yöntem daha temiz bir liste sağlar.
Satır Sonu Karakterlerine İhtiyaç Varsa:

f.readlines(): Eğer satır sonu karakterlerini korumanız gerekiyorsa veya dosyayı satır satır okumanız daha uygunsa, bu yöntem daha uygun olacaktır.
Özetle, her iki yöntem de dosya içeriğini satır bazında işlemek için kullanılır, ancak satır sonu karakterleri ve bellek kullanımı açısından farklılık gösterirler.

"""


print('#' * 170)

with open('configuration.txt') as f:
    print(f.readline(), end='')
    print(f.readline())
    print(f.readline())



# iterate over a file

with open('configuration.txt') as f:
    for line in f:
        print(line, end='')
























