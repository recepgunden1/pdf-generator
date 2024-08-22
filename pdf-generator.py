from PIL import Image
from fpdf import FPDF

# PDF oluştur
pdf = FPDF()

# Dönüştürmek istediğin resim dosyalarının listesi
image_files = ['resim1.jpg', 'resim2.jpg']

for image_file in image_files:
    # Resim dosyasını aç
    image = Image.open(image_file)

    # Resmin genişlik ve yüksekliğini al
    width, height = image.size

    # Resmi mm cinsinden almak için pikseli mm'ye çeviriyoruz
    width, height = width * 0.264583, height * 0.264583

    # Sayfa boyutunu resmin boyutuna göre ayarlıyoruz
    pdf.add_page(orientation='P' if width < height else 'L', format=(width, height))

    # Resmi PDF'e ekliyoruz
    pdf.image(image_file, 0, 0, width, height)

# PDF dosyasını kaydet
pdf.output("resimler.pdf")
