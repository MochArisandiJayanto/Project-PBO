import sqlite3

class Bank:

    def melihatSaldo():
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        cur.execute("SELECT Nama,[Jumlah Saldo] From Akun")
        rows =cur.fetchall()
        con.close()
        return rows

    def melihatAkun():
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        cur.execute("SELECT Nama From Akun")
        rows =cur.fetchall()
        con.close()
        return rows

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tSISTEM MANAJEMEN BANK")
    print("\t\t\t\t**********************")

    print("\t\t\t\tDibuat Oleh:")
    print("\t\t\t\tMOCH. ARISANDI JAYANTO")
    print("\t\t\t\tAhmad Faishol Fawwas")
    input("Klik Enter Untuk Lanjut")

ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("\tMAIN MENU")
    print("\t\t1. Membuat Akun Baru")
    print("\t\t2. Jumlah Saldo")
    print("\t\t3. Menarik Saldo")
    print("\t\t4. Transfer")
    print("\t\t5. Edit Akun")
    print("\t\t6. Melihat Akun")
    print("\t\t7. Exit")
    ch = int(input("\t\tMasukkan Pilihan Anda (1-7) :  "))
    #system("cls");
    
    if ch == 1:
        print("Membuat Akun")
    elif ch == 2:
        print("Jumlah Saldo")
        print(Bank.melihatSaldo())
    elif ch == 3:
        print("Menarik saldo")
    elif ch == 4:
        print("Transfer")
    elif ch == 5:
        print("Edit Akun")
    elif ch == 6:
        print(Bank.melihatAkun())
    elif ch == 7:
        print("\tTerimakasih Sudah Menggunakan SISTEM MANAJEMEN BANK")
        break
    else :
        print("Error! Tidak ditemukan pilihan")
    
    ch = input("Apakah Mau kembali melihat MAIN MENU? (y/t) : ")
    if ch == "t":
        break