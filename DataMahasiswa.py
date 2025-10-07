# Program Data Mahasiswa & Dosen
# Versi sederhana (tanpa database, tanpa GUI)
# Dilengkapi data awal dosen dan mahasiswa

# === Data Awal ===
dosen_list = [
    {"nama": "Pak Budi", "nidn": "12345", "prodi": "Informatika"},
    {"nama": "Bu Sinta", "nidn": "67890", "prodi": "Sistem Informasi"}
]

mahasiswa_list = [
    {"nama": "Hilda", "npm": "231001", "prodi": "Informatika", "kelas": "IF-A", "angkatan": "2023", "pa": "Pak Budi"},
    {"nama": "Rian", "npm": "231002", "prodi": "Informatika", "kelas": "IF-A", "angkatan": "2023", "pa": "Pak Budi"},
    {"nama": "Della", "npm": "221005", "prodi": "Sistem Informasi", "kelas": "SI-B", "angkatan": "2022", "pa": "Bu Sinta"}
]

# --- Fungsi Input Data Dosen ---
def input_dosen():
    print("\n=== INPUT DATA DOSEN ===")
    nama = input("Nama Dosen: ")
    nidn = input("NIDN Dosen: ")
    prodi = input("Program Studi: ")

    dosen = {"nama": nama, "nidn": nidn, "prodi": prodi}
    dosen_list.append(dosen)
    print("✅ Data dosen berhasil disimpan!\n")

# --- Fungsi Input Data Mahasiswa ---
def input_mahasiswa():
    if len(dosen_list) == 0:
        print("⚠️ Belum ada data dosen! Silakan input dosen dulu.")
        return
    
    print("\n=== INPUT DATA MAHASISWA ===")
    nama = input("Nama Mahasiswa: ")
    npm = input("NPM: ")
    prodi = input("Program Studi: ")
    kelas = input("Kelas: ")
    angkatan = input("Angkatan: ")

    print("\nPilih Dosen PA dari daftar berikut:")
    for i, dosen in enumerate(dosen_list):
        print(f"{i+1}. {dosen['nama']} ({dosen['prodi']})")

    try:
        pilihan = int(input("Masukkan nomor dosen PA: "))
        if 1 <= pilihan <= len(dosen_list):
            pa = dosen_list[pilihan-1]['nama']
        else:
            print("Pilihan tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka!")
        return

    mahasiswa = {
        "nama": nama,
        "npm": npm,
        "prodi": prodi,
        "kelas": kelas,
        "angkatan": angkatan,
        "pa": pa
    }
    mahasiswa_list.append(mahasiswa)
    print("✅ Data mahasiswa berhasil disimpan!\n")

# --- Fungsi Tampilkan Semua Mahasiswa ---
def tampilkan_data_mahasiswa():
    print("\n=== DAFTAR SEMUA DATA MAHASISWA ===")
    if len(mahasiswa_list) == 0:
        print("Belum ada data mahasiswa.")
    else:
        for i, mhs in enumerate(mahasiswa_list, start=1):
            print(f"{i}. {mhs['nama']} | NPM: {mhs['npm']} | "
                  f"Prodi: {mhs['prodi']} | Kelas: {mhs['kelas']} | "
                  f"Angkatan: {mhs['angkatan']} | PA: {mhs['pa']}")
    print()

# --- Fungsi Cari Mahasiswa ---
def cari_mahasiswa():
    print("\n=== CARI DATA MAHASISWA ===")
    keyword = input("Masukkan Nama atau NPM yang ingin dicari: ").lower()
    hasil = [mhs for mhs in mahasiswa_list if keyword in mhs['nama'].lower() or keyword in mhs['npm'].lower()]
    
    if hasil:
        for mhs in hasil:
            print("\nData ditemukan:")
            print(f"Nama       : {mhs['nama']}")
            print(f"NPM        : {mhs['npm']}")
            print(f"Prodi      : {mhs['prodi']}")
            print(f"Kelas      : {mhs['kelas']}")
            print(f"Angkatan   : {mhs['angkatan']}")
            print(f"Dosen PA   : {mhs['pa']}")
    else:
        print("❌ Data mahasiswa tidak ditemukan.\n")

# --- Menu Utama ---
def menu():
    while True:
        print("""
=============================
 SISTEM DATA MAHASISWA & DOSEN
=============================
1. Input Data Dosen
2. Input Data Mahasiswa
3. Lihat Semua Data Mahasiswa
4. Cari Data Mahasiswa
5. Keluar
""")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            input_dosen()
        elif pilihan == '2':
            input_mahasiswa()
        elif pilihan == '3':
            tampilkan_data_mahasiswa()
        elif pilihan == '4':
            cari_mahasiswa()
        elif pilihan == '5':
            print("Terima kasih, program selesai 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi.\n")

# --- Jalankan Program ---
menu()
