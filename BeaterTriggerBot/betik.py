import random
import os
import shutil

def add_random_comments(filename, output_filename, comment_probability=0.5):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if random.random() < comment_probability:
                random_number = random.randint(1, 100000000000)
                file.write(f"#_{random_number}_{random_number}_{random_number}_rastgele_sayi_{random_number}_{random_number}_{random_number}_{random_number}_{random_number}\n")

# Orijinal Python dosyasının adı
original_file_name = 'main.py'
# Rastgele yorumlar eklenmiş Python dosyasının adı
modified_file_name = 'main_with_comments.py'

# Betiğin çalıştırıldığı dizini al
current_directory = os.path.dirname(os.path.abspath(__file__))
original_file = os.path.join(current_directory, original_file_name)
modified_file = os.path.join(current_directory, modified_file_name)

# Rastgele yorumlar ekle
add_random_comments(original_file, modified_file)

# Nuitka ile exe dosyasına çevir
print("Converting to exe with Nuitka...")
os.system(f'nuitka --onefile {modified_file}')

# Silinecek klasörlerin yolları
directories_to_delete = [
    os.path.join(current_directory, 'main_with_comments.build'),
    os.path.join(current_directory, 'main_with_comments.dist'),
    os.path.join(current_directory, 'main_with_comments.onefile-build')
]

# Klasörleri silme işlemini çağır
for directory_path in directories_to_delete:
    try:
        shutil.rmtree(directory_path)
        print(f"{directory_path} başarıyla silindi.")
    except Exception as e:
        print(f"{directory_path} silinirken bir hata oluştu: {e}")

files_to_keep = ['main_with_comments.exe', 'config.json']
for file in os.listdir(current_directory):
    if file not in files_to_keep:
        file_path = os.path.join(current_directory, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting {file}: {e}")