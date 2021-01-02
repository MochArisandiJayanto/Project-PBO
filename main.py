import sqlite3
import abc
class akunn(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def membuatAkun():
        pass
    @abc.abstractmethod
    def login():
        pass
    @abc.abstractmethod
    def cekSaldo():
        pass
    @abc.abstractmethod
    def menarikSaldo():
        pass
    @abc.abstractmethod
    def Transfer():
        pass
    @abc.abstractmethod
    def EditAkun():
        pass

class Bank(akunn):


    def membuatAkun(Nama, Jumlah_Saldo, Username, Password, tempat_tanggal_lahir, nama_ibu, ktp, alamat, status_kewarganegaraan, status_perkawinan, pendidikan_terakhir, agama, alamat_sekarang, telepon_seluler, email):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = 'INSERT INTO Akun (Nama, [Jumlah Saldo], Username, Password,[tempat tanggal lahir],[nama ibu],ktp,alamat,[status kewarganegaraan],[status perkawinan],[pendidikan terakhir],agama,[alamat sekarang],[telepon seluler],email) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\',\'%s\', \'%s\',\'%s\', \'%s\',\'%s\', \'%s\',\'%s\', \'%s\',\'%s\', \'%s\',\'%s\')' 
        query = query % (Nama, Jumlah_Saldo, Username, Password, tempat_tanggal_lahir, nama_ibu, ktp, alamat, status_kewarganegaraan, status_perkawinan, pendidikan_terakhir, agama, alamat_sekarang, telepon_seluler, email)
        cur.execute(query)
        con.commit()
        con.close()
        print("selamat Akun anda telah terdaftar di Bank BKIDs")
    
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
        rows = cur.fetchall()
        print("\n============================================================================================")
        print("Nama : ",rows[0][0],"\nJumlah Saldo : ",rows[0][1])
        print("============================================================================================")
        con.close()
        return rows

    def menarikSaldo(Username, Password):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = "SELECT [Jumlah Saldo] From Akun where Username = \'%s\' and Password = \'%s\'"
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        tarik = int(input("Masukkan jumlah penarikan : "))
        a = rows[0][0] - tarik
        print("\n============================================================================================")
        print("Penarikan Saldo Senilai", tarik, "Sukses.", "\nSisa Saldo Anda Saat Ini : ",a)
        print("============================================================================================")
        sql = "UPDATE Akun SET [Jumlah Saldo] = \'%s\' where Username = \'%s\' and Password = \'%s\' "
        sql = sql % (a, Username, Password)
        cur.execute(sql)
        con.commit()
        con.close()
        return rows

    def Transfer(Username, Password):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = "SELECT [Jumlah Saldo] From Akun where Username = \'%s\' and Password = \'%s\'"
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        rows = cur.fetchall()
        UsernameTujuan = input("Masukkan Username Tujuan : ")
        Tf = int(input("Masukkan jumlah uang untuk ditransfer : "))
        a = rows[0][0] - Tf
        sql = "UPDATE Akun SET [Jumlah Saldo] = \'%s\' where Username = \'%s\' and Password = \'%s\'"
        sql = sql % (a, Username, Password)
        cur.execute(sql)
        con.commit()

        query = "SELECT [Jumlah Saldo] From Akun where Username = \'%s\'"
        query = query % (UsernameTujuan)
        cur.execute(query)
        con.commit()
        quen = cur.fetchall()
        b = quen[0][0] + Tf
        sql = "UPDATE Akun SET [Jumlah Saldo] = \'%s\' where Username = \'%s\'"
        sql = sql % (b, UsernameTujuan)
        cur.execute(sql)
        con.commit()
        con.close()
        print("\n============================================================================================")
        print("Transfer Senilai", Tf, "Ke Akun", UsernameTujuan, "Sukses","\nSisa Saldo Anda Saat Ini : ",a)
        print("============================================================================================")
        return rows
    
    def EditAkun(Username, Password):
        con=sqlite3.connect("data.db")
        cur =con.cursor()
        query = "SELECT Password From Akun where Username = \'%s\' and Password = \'%s\'"
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        quen = cur.fetchall()
        a = input("Masukkan Password Baru : ")
        b = quen[0][0]
        b = a
        query = "UPDATE Akun SET Password = \'%s\' Where Username = \'%s\' and Password = \'%s\'" 
        query = query % (b, Username, Password)
        cur.execute(query)
        con.commit()
        con.close()
        print("Perubahan Password Sukses")

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBank BKIDs")
    print("\t\t\t\t**********************")

    print("\t\t\t\tDibuat Oleh:")
    print("\t\t\t\tMOCH. ARISANDI JAYANTO")
    print("\t\t\t\tAHMAD FAISHOL FAWWAS")
    input("Klik Enter Untuk Lanjut")

ch=''
num=0
sessionUsername = []
intro()

while ch != 8:
    print("\tMAIN MENU")
    print("\t\t1. Membuat Akun Baru")
    print("\t\t2. LOGIN")
    print("\t\t3. Cek Saldo")
    print("\t\t4. Menarik Saldo")
    print("\t\t5. Transfer")
    print("\t\t6. Edit Akun")
    print("\t\t7. Exit")
    ch = int(input("\t\tMasukkan Pilihan Anda (1-8) :  "))
    
    if ch == 1:
        print("Membuat Akun")
        Nama = input("Masukkan Nama : ")
        tempat_tanggal_lahir = input("masukkan tempat,tanggal lahir sesuai ktp: ")
        nama_ibu = input("masukkan nama ibu kandung asli : ")
        ktp = input("masukkan nomer ktp : ")
        alamat = input("masukkan alamat tinggal sesuai ktp  : ")
        status_kewarganegaraan = input("masukkan status kewarganegaraan WNI/WNA : ")
        status_perkawinan = input("masukkan status perkawinan apakah lajang/single/duda/janda : ")
        pendidikan_terakhir = input("masukkan pendidikan terakhir anda : ")
        agama = input("masukkan agama anda : ")
        alamat_sekarang = input("masukkan alamat tinggal sekarang : ")
        telepon_seluler = input("masukkan nomer telepon seluler : ")
        email = input("masukkan email anda (ex: babykids@gmail.com) : ")
        Username = input("Masukkan Username Akun Anda : ")
        Password = input("Masukkan Password Anda : ")
        Jumlah_Saldo = int(input("Masukkan Jumlah Deposit : "))
        Bank.membuatAkun(Nama, Jumlah_Saldo, Username, Password, tempat_tanggal_lahir, nama_ibu, ktp, alamat, status_kewarganegaraan, status_perkawinan, pendidikan_terakhir, agama, alamat_sekarang, telepon_seluler, email)
    elif ch == 2:
        print("Login")
        Username = input("Masukkan Username Akun Anda : ")
        Password = input("Masukkan Password Anda : ")
        Akun = Bank.login(Username,Password)
        sessionUsername.append(Username)
    elif ch == 3:
        print("Cek Saldo")
        Akun, Bank.cekSaldo(Username)
    elif ch == 4:
        print("Tarik saldo")
        Akun, Bank.menarikSaldo(Username, Password)
    elif ch == 5:
        print("Transfer")
        Akun, Bank.Transfer(Username, Password)
    elif ch == 6:
        print("Edit Akun")
        Akun, Bank.EditAkun(Username, Password)
    elif ch == 7:
        print("\tTerimakasih Sudah Menggunakan Bank BKIDs")
        break
    else :
        print("Error! Tidak ditemukan pilihan")
    
    ch = input("Apakah Mau kembali melihat MAIN MENU? (y/t) : ")
    if ch == "t":
        break