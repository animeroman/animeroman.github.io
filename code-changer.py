import os
import re

# Değiştirmek istediğiniz HTML kodu
eski_kod = 'i><a href="./sci-fi.html">Sci-Fi 2</a><'
yeni_kod = 'i><a href="./sci-fi.html">Sci-Fi</a><'

# Klasör yolunu belirtin
klasor_yolu = 'C:/Users/aydin_000/Desktop/AnimeRoman/demo-file'  # İlgili klasörün yolu

# Klasör içinde dolaşarak dosyaları işleyin
for klasor_yolu, alt_klasorler, dosya_listesi in os.walk(klasor_yolu):
    for dosya in dosya_listesi:
        if dosya.endswith('.html'):  # Sadece HTML dosyalarını işle
            dosya_yolu = os.path.join(klasor_yolu, dosya)
            with open(dosya_yolu, 'r') as f:
                icerik = f.read()

            # Eski kodu yeni koda değiştir
            yeni_icerik = re.sub(re.escape(eski_kod), yeni_kod, icerik)

            with open(dosya_yolu, 'w') as f:
                f.write(yeni_icerik)

print("Process completed. Files have been updated.")
