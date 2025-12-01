import os
import platform 

def tulis_list_nim(nama_folder, nama_file, nim_list):
    """Membuat folder dan menulis list NIM ke dalam file."""
    try:
        if not os.path.exists(nama_folder):
            os.makedirs(nama_folder)

        file_path = os.path.join(nama_folder, nama_file)
        with open(file_path, 'w') as file:
            for nim in nim_list:
                file.write(f"{nim}\n")
        print(f"✅ Data berhasil ditulis ke: {file_path}")
    except Exception as e:
        print(f"❌ Error saat menulis file: {e}")

def baca_list_nim(nama_folder, nama_file):
    """Membaca list NIM dari file, mengembalikan list string."""
    nim_list = []
    file_path = os.path.join(nama_folder, nama_file)
    
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                nim_list = [line.strip() for line in lines if line.strip()]
            print(f"✅ Data berhasil dibaca dari: {file_path}")
        except Exception as e:
            print(f"❌ Error saat membaca file: {e}")
            return []
    else:
        print(f"⚠️ File tidak ditemukan di: {file_path}")
        
    return nim_list


def tampilkan_data_per_index(nim_list):
    """Menampilkan data per index."""
    if not nim_list:
        print("List NIM kosong.")
        return

    print("Data per index:")
    for i, nim in enumerate(nim_list):
        print(f"Index {i}: {nim}")

def hitung_rata_rata(nim_list):
    """Menghitung nilai rata-rata dari data list setelah memvalidasi sebagai integer."""
    valid_numbers = []
    for nim in nim_list:
        try:
            valid_numbers.append(int(nim))
        except ValueError:
            print(f"⚠️ Peringatan: Data '{nim}' bukan angka dan dilewati dalam perhitungan rata-rata.")

    if not valid_numbers:
        return 0.0 

    total = sum(valid_numbers)
    rata_rata = total / len(valid_numbers)
    return rata_rata


def buka_file(nama_folder, nama_file):
    """Membuka file hasil, mendukung multi-platform."""
    file_path = os.path.join(nama_folder, nama_file)
    
    if os.path.exists(file_path):
        try:
            if platform.system() == "Windows":
                os.startfile(file_path) 
            elif platform.system() == "Darwin": 
                os.system(f"open {file_path}")
            else: 
                os.system(f"xdg-open {file_path}")
            print(f"✅ Mencoba membuka file: {file_path}")
        except Exception as e:
            print(f"❌ Gagal membuka file: {e}")
    else:
        print("❌ File tidak ditemukan untuk dibuka.")


def main():
    initial_nim_list = [3, 1, 2, 3, 1, 0, 5, 2, 0]

    main_nim_id = "".join(map(str, initial_nim_list))
    nama_folder = f"folder_nim_{main_nim_id}"
    nama_file = f"{main_nim_id}.txt"

    print(f"--- Skrip Manajemen Data NIM ({main_nim_id}) ---")
    
    tulis_list_nim(nama_folder, nama_file, initial_nim_list)

    print("-" * 30)

    nim_list_dari_file = baca_list_nim(nama_folder, nama_file)

    print("-" * 30)

    tampilkan_data_per_index(nim_list_dari_file)

    print("-" * 30)

   rata_rata_nim = hitung_rata_rata(nim_list_dari_file)
    print("\n🔢 Rata-rata Nilai: **{:.2f}**".format(rata_rata_nim))
    
    print("-" * 30)

    buka_file(nama_folder, nama_file)

if __name__ == "__main__":
    main()
