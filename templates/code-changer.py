import os
import re

# Değiştirmek istediğiniz HTML kodu
eski_kod = 'rel="stylesheet" href="css'
yeni_kod = 'rel="stylesheet" href="{{ url_for('static', filename='css'

# Klasör yolunu belirtin
klasor_yolu = 'C:/Users/aydin_000/Desktop/RomanFlask/templates/ChangeZone'  # İlgili klasörün yolu

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
