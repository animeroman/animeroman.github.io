import os

# İstenen klasör ismi
folder_name = "GATE Part 2"

# Kullanıcının masaüstü yolu
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Dosya adı ve tam yolu
file_name = os.path.join(desktop_path, "downloads_output.py")

# Metni oluşturma
downloads_text = "downloads = [\n"
for i in range(1, 13):
    for lang in ["en", "jp"]:
        downloads_text += f"\t# Eposide {i} ({lang}) ({folder_name})\n"
        downloads_text += f"\t('m3u8', '/content/drive/MyDrive/{folder_name}/{lang}/Eposide {i}/Eposide {i}.mp4'),\n"
    # Aralık bırak sadece son iterasyonda
    if i != 0:
        downloads_text += "\n"
downloads_text = downloads_text.rstrip(",\n")  # Virgül ve son satırı sil

downloads_text += "\n]"

# Metni dosyaya yaz
with open(file_name, "w", encoding="utf-8") as file:
    file.write(downloads_text)

print(f"Metin '{file_name}' dosyasına başarıyla kaydedildi.")
