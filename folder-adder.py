import os

# Ana klasörünüzün yolu
base_folder = "C:/Users/aydin_000/Desktop/EposidesHere"

# Ana klasördeki her alt klasör için döngü
for folder in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder)
    if os.path.isdir(folder_path):
        # Yeni klasörlerin oluşturulması
        for i in range(1, 25):
            new_folder_name = f"eposide {i}"
            new_folder_path = os.path.join(folder_path, new_folder_name)
            os.mkdir(new_folder_path)
        print(f"Yeni klasörler oluşturuldu: {folder_path}")

