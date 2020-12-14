import sqlite3

class Bank:


    def membuatAkun(Nama, Jumlah_Saldo, Username, Password):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = 'INSERT INTO Akun (Nama, [Jumlah Saldo], Username, Password) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\')' 
        query = query % (Nama, Jumlah_Saldo, Username, Password)
        cur.execute(query)
        con.commit()
        con.close()
    
    def login(Username, Password):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = 'SELECT Username, Password FROM Akun \
        where Username=\'%s\' and Password=\'%s\' '
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        rows =cur.fetchall()
        accept_Login = True
        if (len(rows)) == 0:
            accept_Login = False

        if accept_Login == False:
            print("Login Gagal")
        elif Username == rows[0][0] and Password == rows[0][1]:
            accept_Login = True
            print("Login Sukses")
            return Username
        
        con.close()
    
    def cekSaldo(Username):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = "SELECT Nama,[Jumlah Saldo] From Akun where Username = \'%s\'"
        query = query % (Username)
        cur.execute(query)
        con.commit()

        rows = cur.fetchone()
        
        con.close()
        return rows
        print()

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
sessionUsername = []
intro()

while ch != 8:
    #system("cls");
    print("\tMAIN MENU")
    print("\t\t1. Membuat Akun Baru")
    print("\t\t2. LOGIN")
    print("\t\t3. Cek Saldo")
    print("\t\t4. Menarik Saldo")
    print("\t\t5. Transfer")
    print("\t\t6. Edit Akun")
    print("\t\t7. Melihat Akun")
    print("\t\t8. Exit")
    ch = int(input("\t\tMasukkan Pilihan Anda (1-8) :  "))
    #system("cls");
    
    if ch == 1:
        print("Membuat Akun")
        Nama = input("Masukkan Nama : ")
        Jumlah_Saldo = int(input("Masukkan Jumlah Saldo : "))
        Username = input("Masukkan Username Akun Anda : ")
        Password = input("Masukkan Password Anda(Password Menggunakan Angka) : ")
        Bank.membuatAkun(Nama, Jumlah_Saldo, Username, Password)
    elif ch == 2:
        print("Login")
        Username = input("Masukkan Username Akun Anda : ")
        Password = input("Masukkan Password Anda(Password Menggunakan Angka) : ")
        Akun = Bank.login(Username,Password)
        sessionUsername.append(Username)
    elif ch == 3:
        print("Cek Saldo")
        print(Akun, Bank.cekSaldo(Username))
    elif ch == 4:
        print("Menarik saldo")
    elif ch == 5:
        print("Transfer")
    elif ch == 6:
        print("Edit Akun")
    elif ch == 7:
        print("Akun yang terdaftar di Bank")
        print(Bank.melihatAkun())
    elif ch == 8:
        print("\tTerimakasih Sudah Menggunakan SISTEM MANAJEMEN BANK")
        break
    else :
        print("Error! Tidak ditemukan pilihan")
    
    ch = input("Apakah Mau kembali melihat MAIN MENU? (y/t) : ")
    if ch == "t":
        break