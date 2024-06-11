# ujian praktek Pertemuan 14
# Kelompok 12
# anggota 
# M. Riziq Sirfatullah Alfarizi - i.2211266
# Muhamad Noufal Falah - i.2210466
# Muhammad Risyad Fadilah - i.2210148

import mysql.connector

# Koneksi ke server MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

# Membuat database dan tabel jika belum ada
def create_database():
    db = connect_db() 
    cursor = db.cursor() 
    cursor.execute("CREATE DATABASE IF NOT EXISTS database_tugas")  
    cursor.execute("USE database_tugas")  
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kelompok_12 (
        id INT AUTO_INCREMENT PRIMARY KEY,  # Membuat tabel dengan kolom id, name, dan kota
        name VARCHAR(255) NOT NULL,
        kota VARCHAR(255) NOT NULL
    )
    """)
    db.close()  

# Menambahkan data 
def insert_data(name, kota):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE database_tugas") 
    cursor.execute("INSERT INTO kelompok_12 (name, kota) VALUES (%s, %s)", (name, kota))  
    db.commit()  
    db.close()  

# Menampilkan semua data 
def display_data():
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE database_tugas")  
    cursor.execute("SELECT * FROM kelompok_12")  
    results = cursor.fetchall()  
    for row in results:
        print(row)  
    db.close()  

# update data dalam tabel
def update_data(id, name, kota):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE database_tugas")  
    cursor.execute("UPDATE kelompok_12 SET name = %s, kota = %s WHERE id = %s", (name, kota, id))  
    db.commit()  
    db.close()  

# Menghapus data dari tabel
def delete_data(id):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE database_tugas")  
    cursor.execute("DELETE FROM kelompok_12 WHERE id = %s", (id,))  
    db.commit()  
    db.close()  

# Mencari data yang ada dalam tabel 
def search_data(name):
    db = connect_db()  
    cursor = db.cursor()  
    cursor.execute("USE database_tugas")  
    cursor.execute("SELECT * FROM kelompok_12 WHERE name = %s", (name,))  
    results = cursor.fetchall()  
    for row in results:
        print(row)  
    db.close()  

# Menu utama menjalakan
def main():
    create_database()  

    while True:
        print("\n=== KELOMPOK 12 ===")
        print("=== APLIKASI DATABASE PYTHON ===")
        print("1. Insert Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Cari Data")
        print("0. Keluar")
        pilihan = input("Pilih menu> ")

        if pilihan == "1":
            name = input("Nama: ")
            kota = input("Kota: ")
            insert_data(name, kota)
        elif pilihan == "2":
            display_data()
        elif pilihan == "3":
            id = input("ID: ")
            name = input("Nama baru: ")
            kota = input("Kota baru: ")
            update_data(id, name, kota)
        elif pilihan == "4":
            id = input("ID: ")
            delete_data(id)
        elif pilihan == "5":
            name = input("Nama: ")
            search_data(name)
        elif pilihan == "0":
            break
        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()
