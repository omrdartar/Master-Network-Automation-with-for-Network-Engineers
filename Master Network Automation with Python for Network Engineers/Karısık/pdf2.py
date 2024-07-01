from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'Python Kod Açıklaması', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('DejaVu', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create a PDF object
pdf = PDF()

# Add a Unicode font (DejaVu)
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.sfd', uni=True)
pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.sfd', uni=True)

# Add a page
pdf.add_page()

# Title
pdf.chapter_title('Python Kod Açıklaması')

# Body content
body_content = """
with open('devices.txt') as f:
    content = f.read().splitlines()
    print(content)
    devices = list()
    for line in content:
        devices.append(line.split(':'))
    print(devices)

Bu komutları tek tek detaylı bir şekilde açıklayalım:

1. Dosyayı Açma ve Okuma

with open('devices.txt') as f:
    content = f.read().splitlines()

Bu kısımda birkaç şey gerçekleşiyor:

1. with open('devices.txt') as f: Bu, devices.txt adlı dosyayı okumak için açar. with ifadesi, dosya işlemlerinde kaynak yönetimi sağlar ve dosyanın otomatik olarak kapatılmasını garanti eder. f değişkeni, dosya nesnesini temsil eder.

2. content = f.read().splitlines(): 
    - f.read(): Dosyanın içeriğini bir string olarak okur.
    - .splitlines(): Bu, dosyanın içeriğini satır satır ayırır ve her bir satırı bir liste elemanı olarak döner. Boş satırlar da dahil olmak üzere her satır bir liste elemanı olur.

2. İçeriği Yazdırma

print(content)

Bu komut, content değişkeninin içeriğini yazdırır. content bir liste olduğundan, dosyanın her satırını bir liste elemanı olarak ekrana yazdırır.

3. Cihazlar Listesini Oluşturma

devices = list()

Bu satır, devices adlı boş bir liste oluşturur. Bu liste, daha sonra dosyadaki her satırın belirli bir işleme tabi tutulmuş halini saklamak için kullanılacaktır.

4. Satırları Bölme ve Listeye Ekleme

for line in content:
    devices.append(line.split(':'))

Bu döngü, content listesindeki her bir satırı işler:

1. for line in content: content listesindeki her bir eleman (line) üzerinde döngü yapar.

2. line.split(':'): Her bir satırı (string) : karakterine göre böler ve bu, bir liste döner. Örneğin, "device1:info1" satırı ["device1", "info1"] listesine dönüşür.

3. devices.append(line.split(':')): Bölünmüş listeyi devices listesine ekler. Bu, devices listesinin her bir elemanının, content listesindeki bir satırın : karakterine göre bölünmüş hali olmasını sağlar.

5. devices Listesini Yazdırma

print(devices)

Bu komut, devices listesinin içeriğini yazdırır. devices listesi, content listesindeki her bir satırın : karakterine göre bölünmüş hallerinden oluşur.

Örnek Dosya ve Çıktılar

Varsayalım ki devices.txt dosyasının içeriği şu şekilde olsun:

device1:info1
device2:info2
device3:info3

Yukarıdaki kod şu adımları izler:

1. Dosya açılır ve content listesi şu şekilde olur:
   ['device1:info1', 'device2:info2', 'device3:info3']

2. content listesi ekrana yazdırılır.

3. Boş bir devices listesi oluşturulur.

4. Döngü, her bir satırı : karakterine göre böler ve devices listesine ekler:
   [['device1', 'info1'], ['device2', 'info2'], ['device3', 'info3']]

5. devices listesi ekrana yazdırılır.

Bu, dosyadaki her bir satırın iki parçaya bölündüğü ve sonuçların iki boyutlu bir liste olarak saklandığı bir süreçtir.
"""

# Add body content to PDF
pdf.chapter_body(body_content)

# Save the PDF to a file
pdf.output("Python_Kod_Aciklamasi.pdf")
