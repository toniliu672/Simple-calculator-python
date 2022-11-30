import locale
import pandas as pd
locale.setlocale(locale.LC_ALL, 'IND')


database = [
    {
        "Kode Buku": "123",
        "Nama Barang": "Buku Tulis",
        "Harga Barang": locale.currency(10000, grouping=True),
        "Jumlah Barang": 10
    },
    {
        "Kode Buku": "456",
        "Nama Barang": "Buku Komputer",
        "Harga Barang": locale.currency(20000, grouping=True),
        "Jumlah Barang": 20
    },
    {
        "Kode Buku": "789",
        "Nama Barang": "Buku Masak",
        "Harga Barang": locale.currency(30000, grouping=True),
        "Jumlah Barang": 30
    }
    ]

def tunjukan_data():
    pilihan="y"
    while pilihan=="y":
        cari_kode = input("Masukkan kode buku: ")
        for data in database:
            for val in data.values():
                if val == cari_kode:
                    df = pd.DataFrame(data, index=[0])
                    print(df)
                    break
        pilihan = input("cari lagi (y/t)? ")
    pilihan="t"
    while pilihan=="t":
        books_data()

def tambah():
    add_data= {}
    while True:
        
        try:   
            add_data["Kode Buku"] = input("input kode buku: ")
            if len(add_data["Kode Buku"]) != 3:
                raise ValueError     
            break
        except ValueError:
            if add_data["Kode Buku"].strip() == "":
                print("tidak boleh kosong")
            else:
                print("please enter 3 digits number")

    add_data["Nama Barang"] = input("input nama barang: ")
    while True:
        try:
            add_data["Harga Barang"] = locale.currency(int(input("input harga barang: ")), grouping=True)
            add_data["Jumlah Barang"] = int(input("input jumlah barang: "))
            break
        except ValueError:
            print("please enter number")

    database.append(add_data)
    print("Data berhasil ditambahkan")
    books_data()

def ubah():
    pilihan="y"
    while pilihan=="y":
        print("Data Changes")
        try:
            cari_kode = input("Masukkan kode buku: ")
            if cari_kode.strip() == "" :
                print("Kode tidak ditemukan")
            for data in database:
                for val in data.values():
                    if val == cari_kode:
                        data['Nama Barang']=input("masukkan nama barang: ")
                        while True:
                            try:
                                new_harga=int(input('masukkan harga barang: '))
                                break
                            except ValueError:
                                print("masukkan angka")
                        data['Harga Barang']=locale.currency(new_harga, grouping=True)
                        data['Jumlah Barang']=input("masukkan jumlah jumlah barang : ") 
                        print("data berhasil diubah")
            break
        except KeyboardInterrupt:
            print("Kembali ke menu")
            books_data()
    pilihan = input("cari lagi (y/t)? ")
    pilihan="t"
    while pilihan=="t":
        books_data()

def hapus():
    pilihan="y"
    while pilihan=="y":
        cari_kode = input("Masukkan kode buku: ")
        for data in database:
            if data.get('Kode Buku') == cari_kode:
                database.remove(data)
                print("data berhasil dihapus")
        pilihan = input("cari lagi (y/t)? ")
    pilihan="t"
    while pilihan=="t":
        books_data()



def kasir():
    def input_user():
        global pesan, j_kamar, harga, listnama
        while True:
            try:
                pesan=int(input("Pesan Kamar : "))
                j_kamar=int(input("Jumlah Kamar : "))
                break
            except ValueError:
                print("Silahkan pilih menu dengan angka")
            
        if pesan== 1:
            listnama="Standard"
            harga=(100000*j_kamar)  
        elif pesan== 2:
            listnama="Deluxe"
            harga=(150000*j_kamar)
        elif pesan== 3:
            listnama="VIP"
            harga=(200000*j_kamar)
        else:
            print("Pilihan tidak tersedia")
            input_user()
 
                    
    def harga_tambahan():
        global namatambahan, totalharga, hargatambahan
        while True:
            try:
                tambahan = int(input("Tambahan : "))
                break
            except ValueError:
                print("silahkan masukkan pilihan yang tersedia")
        
        if tambahan==1: #makan siang
            namatambahan="Makan Siang"
            hargatambahan=int(10000)
        elif tambahan==2: #bantal
            namatambahan="Bantal"
            hargatambahan=int(2000)
        elif tambahan==3: #kasur
            namatambahan="Kasur"
            hargatambahan=int(50000)
        elif tambahan==4:  #makan siang + bantal
            namatambahan="Makan Siang + Bantal"
            hargatambahan=int(12000)
        elif tambahan==5: #makan siang + kasur
            namatambahan="Makan Siang + Kasur"
            hargatambahan=int(60000)
        elif tambahan==6: #bantal + kasur
            namatambahan="Bantal + Kasur"
            hargatambahan=int(22000)
        elif tambahan==7:  #makan siang + bantal + kasur
            namatambahan="Makan Siang + Bantal + Kasur"
            hargatambahan=int(72000)
        else:
            tambahan==0
            namatambahan="Tidak Ada"
            hargatambahan=0
            totalharga = harga
        totalharga=int(harga+hargatambahan)

    def pemesanan():

        print("""
Pilih Menu:
-------------------------------------------------
LIST KAMAR DAHLIA
1. Kamar Standard : Rp. 100.000
2. Kamar Deluxe : Rp. 150.000
3. Kamar VIP : Rp. 200.000
-------------------------------------------------
Tambahan :
1. Makan Siang : Rp. 10.000
2. Bantal : Rp. 2.000
3. Kasur : Rp. 50.000
4. Makan Siang + Bantal : Rp. 12.000
5. Makan Siang + Kasur : Rp. 60.000
6. Bantal + Kasur : Rp. 22.000
7. Makan Siang + Bantal + Kasur : Rp. 72.000
""")
        input_user()
        harga_tambahan()

        print("""
    ----------------------------------------)
    Penginapan Dahlia
    ----------------------------------------""")
        print(f"""
Tipe Kamar : {listnama}
Harga Kamar    : {locale.currency(harga, grouping=True)}
Jumlah kamar   : {j_kamar}
Jenis Tambahan : {namatambahan}
Harga Tambahan : {locale.currency(hargatambahan, grouping=True)}
----------------------------------------""")
        print("Total Harga    :  ",locale.currency(totalharga, grouping=True))
        opsi=input("Lanjutkan pemesanan? ? (y/n) ")
        if opsi == "y" or "Y":
            print("Terima kasih, Pesanan Anda Berhasil")
            main_menu()
        else:
            print("Pesanan dibatalkan, Silahkan buat pesanan baru")
            pemesanan()
    pemesanan()

def main_menu():
    print("==========================================")
    print("|               PROGRAM                  |")
    print("==========================================")
    print("1. Books Data")
    print("2. Aplikasi Kasir Penginapan")
    print("3. Exit")
    pilih = input("Masukkan pilihan: ")
    if pilih == "1":
        books_data()
    elif pilih == "2":
        kasir()
    elif pilih == "3":
        exit()
    else:
        print("masukkan pilihan lainnya")

def books_data():
    print("==========================================")
    print("|            Welcome                    |")
    print("1. Search Data")
    print("2. Add Data")
    print("3. Change Data")
    print("4. Delete Data")
    print("5. Show All available Data")
    print("6. Exit")
    pilih = input("Masukkan pilihan: ")

    if pilih == "1":
       tunjukan_data()
    elif pilih == "2":
        tambah()
    elif pilih == "3":
        ubah()
    elif pilih == "4":
        hapus()
    elif pilih == "5":
        df = pd.DataFrame(database,)
        print(df.to_string())
        jumlahdata = len(database)
        print("--------------------")
        print("jumlah data dalam database : ", jumlahdata)
        books_data()
    elif pilih == "6":
        main_menu()
    else: 
        main_menu()

if __name__ == "__main__":

    while(True):
        main_menu()
