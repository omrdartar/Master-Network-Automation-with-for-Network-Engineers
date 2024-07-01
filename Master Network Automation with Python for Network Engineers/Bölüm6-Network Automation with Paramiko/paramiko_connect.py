

# Paramiko modülünü import ederiz. Bu modül, Python ile SSH protokolü kullanarak uzaktan
# bağlantı ve komut çalıştırma işlemleri için kullanılır.
import paramiko

# SSHClient sınıfından bir örnek oluştururuz. Bu sınıf, SSH bağlantısı kurmak ve yönetmek için kullanılır.
ssh_client = paramiko.SSHClient()

# Uzak sunucunun SSH anahtarını daha önce bilmesek bile kabul etmemizi sağlayan bir politika belirleriz.
# AutoAddPolicy, bilmediğimiz anahtarları otomatik olarak kabul etmemizi sağlar.
# Bu, test ortamları için kullanışlı olabilir ancak
# prodüksiyon ortamlarında güvenlik riskleri taşıyabilir.
# Bu yüzden, gerçek dünyada bu politikayı kullanırken dikkatli olmalıyız.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Kullanıcıya SSH bağlantısı kurulacağını belirten bir bilgi mesajı yazdırırız.
print('Connecting to 192.168.146.10')

# ssh_client.connect() metodunu kullanarak SSH bağlantısı kurarız.
# hostname parametresi, bağlanmak istediğimiz uzak sunucunun IP adresi veya DNS adıdır.
# port parametresi, SSH bağlantısı için kullanılan port numarasıdır (genellikle 22).
# username ve password parametreleri, SSH bağlantısı için kullanılan kimlik doğrulama bilgilerini içerir.
# look_for_keys=False, SSH bağlantısı kurarken yerel SSH anahtar dosyalarını aramamasını sağlar.
# allow_agent=False, SSH agent'ı kullanmamasını sağlar. Bu iki parametre,
# doğrudan kullanıcı adı ve şifre ile bağlantı kurmamıza izin verir.
ssh_client.connect(hostname='192.168.146.10', port=22, username='admin', password='admin',
                   look_for_keys=False, allow_agent=False)

# SSH bağlantısının kapatılacağını belirten bir bilgi mesajı yazdırırız.
print('Closing connection')

# ssh_client.close() metodunu kullanarak SSH bağlantısını kapatırız.
# Bu, uzaktaki kaynakları serbest bırakır ve bağlantıyı düzgün bir şekilde sonlandırır.
ssh_client.close()

