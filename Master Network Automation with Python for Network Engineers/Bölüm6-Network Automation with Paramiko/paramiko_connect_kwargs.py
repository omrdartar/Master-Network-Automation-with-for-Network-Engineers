
# Paramiko modülünü import ederiz.
# Bu modül, Python ile SSH protokolü kullanarak uzaktan bağlantı ve komut çalıştırma işlemleri için kullanılır.
import paramiko

# SSHClient sınıfından bir örnek oluştururuz. Bu sınıf, SSH bağlantısı kurmak ve yönetmek için kullanılır.
ssh_client = paramiko.SSHClient()

# ssh_client nesnesinin tipini yazdırmak için kullanılabilir (şu an yorum satırı olarak bırakılmıştır).
# print(type(ssh_client))

# Uzak sunucunun SSH anahtarını daha önce bilmesek bile kabul etmemizi sağlayan bir politika belirleriz.
# AutoAddPolicy, bilmediğimiz anahtarları otomatik olarak kabul etmemizi sağlar.
# Bu, test ortamları için kullanışlı olabilir ancak
# prodüksiyon ortamlarında güvenlik riskleri taşıyabilir.
# Bu yüzden, gerçek dünyada bu politikayı kullanırken dikkatli olmalıyız.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# SSH bağlantısını kurmak için gereken parametreleri bir sözlük (dictionary) olarak tanımlarız.
# Bu parametreler, bağlanmak istediğimiz uzak sunucunun IP adresi, SSH port numarası, kullanıcı adı ve şifresini içerir.
router = {'hostname': '192.168.146.10', 'port': '22', 'username': 'admin', 'password': 'admin', 'look_for_keys': 'False', 'allow_agent': 'False'}

# Kullanıcıya SSH bağlantısı kurulacağını belirten bir bilgi mesajı yazdırırız.
print(f'Connecting to {router["hostname"]}')

# ssh_client.connect() metodunu kullanarak SSH bağlantısı kurarız.
# **router kullanımı, router sözlüğündeki anahtar-değer çiftlerini fonksiyona argüman olarak geçirmemizi sağlar.
# look_for_keys=False ve allow_agent=False ayarları, bağlantı sırasında
# sadece kullanıcı adı ve şifreyi kullanmamızı sağlar (anahtar dosyalarını veya SSH agent'ını kullanmıyoruz).

"""
Bir fonksiyon çağrısında ** kullanarak bir sözlüğü unpack etmek, sözlüğün anahtarlarını 
fonksiyonun parametre isimleriyle eşleştirir ve değerlerini bu parametrelere atar. 
Bu, fonksiyon çağrısını daha temiz ve dinamik hale getirir.
ssh_client.connect(**router)
"""

# Bağlantının aktif olup olmadığını kontrol eder ve sonucu yazdırırız.
print(ssh_client.get_transport().is_active())

# SSH üzerinden komut göndermek için kullanılabilecek yer (şu an için bu kısım yorum satırı olarak bırakılmıştır).
# Komut gönderme işlemi bu noktada yapılabilir.
# ...

# SSH bağlantısının kapatılacağını belirten bir bilgi mesajı yazdırırız.
print('Closing connection')

# ssh_client.close() metodunu kullanarak SSH bağlantısını kapatırız.
# Bu, uzaktaki kaynakları serbest bırakır ve bağlantıyı düzgün bir şekilde sonlandırır.
ssh_client.close()








