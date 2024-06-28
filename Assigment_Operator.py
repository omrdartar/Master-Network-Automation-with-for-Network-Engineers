# divmod()

"""
divmod fonksiyonu, iki sayıyı böldüğümüzde bölüm ve kalanı aynı anda döndüren bir Python yerleşik (built-in) fonksiyonudur.
Bu fonksiyon, bölme işlemi sonucunda hem bölüm hem de kalan değerlerini döndürür.

"""

a, b = divmod(14, 6)
print(a, b)


"""
Yukarıdaki ifadede, 14 sayısını 6 sayısına böldüğümüzde:

a değişkeni bölümü (2) alır.
b değişkeni ise kalanı (2) alır.
Not: divmod fonksiyonu iki değeri birden döndürerek, bölüm ve kalanı ayrı ayrı hesaplamaktan daha verimli 
bir şekilde bu işlemleri yapmanızı sağlar.

"""

# pow()


"""
pow fonksiyonu, Python'da üs alma (exponentiation) işlemi yapmak için kullanılan bir yerleşik (built-in) fonksiyondur. 
Üç parametre alabilir, ancak genellikle iki parametreyle kullanılır: taban (base) ve üs (exponent). 
Bu fonksiyon, tabanın üs kuvvetini hesaplar.

"""

print(pow(5, 9))



"""

Yukarıdaki ifadede:

5 tabandır.

9 ise üssü temsil eder.

pow(5, 9) ifadesi, 5^9 (5 üzeri 9) hesaplar. Sonuç olarak:

5^9 = 1953125

Bu değer ekrana basılır.

Not: pow fonksiyonu, büyük sayılarla çalışırken 
performans açısından daha verimlidir ve üçüncü bir parametre ile 
modüler üs alma işlemi (modular exponentiation) yapabilir, 
bu da kriptografi gibi alanlarda yararlıdır.


"""






"""
sum fonksiyonu, bir dizideki (liste, demet, vb.) elemanların 
toplamını hesaplayan bir Python yerleşik (built-in) fonksiyonudur.
"""

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
Yukarıdaki ifadede:

sum fonksiyonu, verilen liste [1, 2, 3, 4, 5, 6, 7, 8, 9] içindeki tüm elemanları toplar.
Sonuç olarak, listedeki sayılar toplanır: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45.
Bu değer ekrana basılır.

Not: sum fonksiyonu, sayısal değerler içeren bir diziyi toplamak için kullanılır ve işlemi 
basit ve verimli bir şekilde gerçekleştirir.

"""






































