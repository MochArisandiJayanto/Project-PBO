  
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
    print("\t\t4. Cek Sisa Saldo")
    print("\t\t5. Edit Akun")
    print("\t\t6. EXIT")
    ch = int(input("\t\tMasukkan Pilihan Anda (1-6) :  "))
    #system("cls");
    
    if ch == '1':
        print("Membuat Akun")
    elif ch =='2':
        print("Jumlah Saldo")
    elif ch == '3':
        print("Menarik saldo")
    elif ch == '4':
        print("Sisa Saldo")
    elif ch == '5':
        print("Edit Akun")
    elif ch == '6':
        print("\tTerimakasih Sudah Menggunakan SISTEM MANAJEMEN BANK")
        break
    else :
        print("Error! Tidak ditemukan pilihan")
    
    ch = input("Apakah Mau kembali melihat MAIN MENU? (y/t) : ")
    if ch == "t":
        break