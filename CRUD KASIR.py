hoodie_polos = {'ukuran' : ['Hoodie Polos Ukuran S', 'Hoodie Polos Ukuran M', 'Hoodie Polos Ukuran L', 'Hoodie Polos Ukuran XL', 'Hoodie Polos Ukuran XXL'],
                'harga' : [67000, 72000, 72000, 77000, 77000],
                'stok' : [6, 7, 11, 5, 3]
}

hoodie_sablon = {'ukuran' : ['Hoodie Sablon Ukuran S', 'Hoodie Sablon Ukuran M', 'Hoodie Sablon Ukuran L', 'Hoodie Sablon Ukuran XL', 'Hoodie Sablon Ukuran XXL'],
                'harga' : [72000, 77000, 77000, 83000, 83000],
                'stok' : [9, 7, 20, 11, 7]
}

hoodie_bordir = {'ukuran' : ['Hoodie Bordir Ukuran S', 'Hoodie Bordir Ukuran M', 'Hoodie Bordir Ukuran L', 'Hoodie Bordir Ukuran XL', 'Hoodie Bordir Ukuran XXL'],
                'harga' : [72000, 77000, 77000, 83000, 83000],
                'stok' : [7, 7, 18, 10, 5]
}

basic_sweater = {'ukuran' : ['Basic Sweater Ukuran S', 'Basic Sweater Ukuran M', 'Basic Sweater Ukuran L', 'Basic Sweater Ukuran XL', 'Basic Sweater Ukuran XXL'],
                'harga' : [63000, 70000, 70000, 76000, 76000],
                'stok' : [5, 10, 20, 11, 7]
}

kaos_polos = {'ukuran' : ['Kaos Polos Ukuran S', 'Kaos Polos Ukuran M', 'Kaos Polos Ukuran L', 'Kaos Polos Ukuran XL', 'Kaos Polos Ukuran XXL'],
                'harga' : [53000, 58000, 58000, 63000, 63000],
                'stok' : [11, 10, 19, 15, 7]
}

kaos_sablon = {'ukuran' : ['Kaos Sablon Ukuran S', 'Kaos Sablon Ukuran M', 'Kaos Sablon Ukuran L', 'Kaos Sablon Ukuran XL', 'Kaos Sablon Ukuran XXL'],
                'harga' : [56000, 61000, 61000, 66000, 66000],
                'stok' : [4, 5, 22, 19, 9]
}

kaos_bordir = {'ukuran' : ['Kaos Bordir Ukuran S', 'Kaos Bordir Ukuran M', 'Kaos Bordir Ukuran L', 'Kaos Bordir Ukuran XL', 'Kaos Bordir Ukuran XXL'],
                'harga' : [56000, 61000, 61000, 66000, 66000],
                'stok' : [4, 8, 19, 9, 4]
}

def kembali_ke_menu() : 
    print("\n")
    input("Tekan Enter Untuk Kembali Ke Menu Awal...")
    menu_admin()

def daftar_barang() :
    print("=======================================================")
    print("                   TREASURE THINGZ                     ")
    print("=======================================================")
    print("         Nama Barang          Harga           Stok     ")
    print("=======================================================")
    print("{}         Rp{}          {}".format(hoodie_polos['ukuran'][0], hoodie_polos['harga'][0], hoodie_polos['stok'][0]))
    print("{}         Rp{}          {}".format(hoodie_polos['ukuran'][1], hoodie_polos['harga'][1], hoodie_polos['stok'][1]))
    print("{}         Rp{}          {}".format(hoodie_polos['ukuran'][2], hoodie_polos['harga'][2], hoodie_polos['stok'][2]))
    print("{}         Rp{}          {}".format(hoodie_polos['ukuran'][3], hoodie_polos['harga'][3], hoodie_polos['stok'][3]))
    print("{}         Rp{}          {}".format(hoodie_polos['ukuran'][4], hoodie_polos['harga'][4], hoodie_polos['stok'][4]))
    print("{}         Rp{}          {}".format(hoodie_sablon['ukuran'][0], hoodie_sablon['harga'][0], hoodie_sablon['stok'][0]))
    print("{}         Rp{}          {}".format(hoodie_sablon['ukuran'][1], hoodie_sablon['harga'][1], hoodie_sablon['stok'][1]))
    print("{}         Rp{}          {}".format(hoodie_sablon['ukuran'][2], hoodie_sablon['harga'][2], hoodie_sablon['stok'][2]))
    print("{}         Rp{}          {}".format(hoodie_sablon['ukuran'][3], hoodie_sablon['harga'][3], hoodie_sablon['stok'][3]))
    print("{}         Rp{}          {}".format(hoodie_sablon['ukuran'][4], hoodie_sablon['harga'][4], hoodie_sablon['stok'][4]))
    print("{}         Rp{}          {}".format(hoodie_bordir['ukuran'][0], hoodie_bordir['harga'][0], hoodie_bordir['stok'][0]))
    print("{}         Rp{}          {}".format(hoodie_bordir['ukuran'][1], hoodie_bordir['harga'][1], hoodie_bordir['stok'][1]))
    print("{}         Rp{}          {}".format(hoodie_bordir['ukuran'][2], hoodie_bordir['harga'][2], hoodie_bordir['stok'][2]))
    print("{}         Rp{}          {}".format(hoodie_bordir['ukuran'][3], hoodie_bordir['harga'][3], hoodie_bordir['stok'][3]))
    print("{}         Rp{}          {}".format(hoodie_bordir['ukuran'][4], hoodie_bordir['harga'][4], hoodie_bordir['stok'][4]))
    print("{}         Rp{}          {}".format(basic_sweater['ukuran'][0], basic_sweater['harga'][0], basic_sweater['stok'][0]))
    print("{}         Rp{}          {}".format(basic_sweater['ukuran'][1], basic_sweater['harga'][1], basic_sweater['stok'][1]))
    print("{}         Rp{}          {}".format(basic_sweater['ukuran'][2], basic_sweater['harga'][2], basic_sweater['stok'][2]))
    print("{}         Rp{}          {}".format(basic_sweater['ukuran'][3], basic_sweater['harga'][3], basic_sweater['stok'][3]))
    print("{}         Rp{}          {}".format(basic_sweater['ukuran'][4], basic_sweater['harga'][4], basic_sweater['stok'][4])) 
    print("{}         Rp{}          {}".format(kaos_polos['ukuran'][0], kaos_polos['harga'][0], kaos_polos['stok'][0]))
    print("{}         Rp{}          {}".format(kaos_polos['ukuran'][1], kaos_polos['harga'][1], kaos_polos['stok'][1]))
    print("{}         Rp{}          {}".format(kaos_polos['ukuran'][2], kaos_polos['harga'][2], kaos_polos['stok'][2]))
    print("{}         Rp{}          {}".format(kaos_polos['ukuran'][3], kaos_polos['harga'][3], kaos_polos['stok'][3]))
    print("{}         Rp{}          {}".format(kaos_polos['ukuran'][4], kaos_polos['harga'][4], kaos_polos['stok'][4]))    
    print("{}         Rp{}          {}".format(kaos_sablon['ukuran'][0], kaos_sablon['harga'][0], kaos_sablon['stok'][0]))
    print("{}         Rp{}          {}".format(kaos_sablon['ukuran'][1], kaos_sablon['harga'][1], kaos_sablon['stok'][1]))
    print("{}         Rp{}          {}".format(kaos_sablon['ukuran'][2], kaos_sablon['harga'][2], kaos_sablon['stok'][2]))
    print("{}         Rp{}          {}".format(kaos_sablon['ukuran'][3], kaos_sablon['harga'][3], kaos_sablon['stok'][3]))
    print("{}         Rp{}          {}".format(kaos_sablon['ukuran'][4], kaos_sablon['harga'][4], kaos_sablon['stok'][4])) 
    print("{}         Rp{}          {}".format(kaos_bordir['ukuran'][0], kaos_bordir['harga'][0], kaos_bordir['stok'][0]))
    print("{}         Rp{}          {}".format(kaos_bordir['ukuran'][1], kaos_bordir['harga'][1], kaos_bordir['stok'][1]))
    print("{}         Rp{}          {}".format(kaos_bordir['ukuran'][2], kaos_bordir['harga'][2], kaos_bordir['stok'][2]))
    print("{}         Rp{}          {}".format(kaos_bordir['ukuran'][3], kaos_bordir['harga'][3], kaos_bordir['stok'][3]))
    print("{}         Rp{}          {}".format(kaos_bordir['ukuran'][4], kaos_bordir['harga'][4], kaos_bordir['stok'][4]))   
    print("=======================================================")   
      
def update_stok() :
    print("")
    print("=======================================================")
    print("                    UPDATE STOK                      ")
    print("=======================================================")
    
    print("[1]. Hoodie Polos ", "\n[2]. Hoodie Sablon", "\n[3]. Hoodie Bordir", "\n[4]. Basic Sweater", "\n[5]. Kaos Polos", "\n[6]. Kaos Sablon", "\n[7]. Kaos Bordir")
    pilihan_tb = int(input("Masukkan Pilihan Anda : "))
    if pilihan_tb == 1 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_polos['stok'][0] += penambahan
                    hoodie_polos['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else : 
                    break 
        elif pilihan_ukuran == 2 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_polos['stok'][1] += penambahan
                    hoodie_polos['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else : 
                    break
        elif pilihan_ukuran == 3 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_polos['stok'][2] += penambahan
                    hoodie_polos['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_polos['stok'][3] += penambahan
                    hoodie_polos['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_polos['stok'][4] += penambahan
                    hoodie_polos['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else : 
                    break
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 2 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_sablon['stok'][0] += penambahan
                    hoodie_sablon['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 2 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_sablon['stok'][1] += penambahan
                    hoodie_sablon['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 3 :
            while True : 
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_sablon['stok'][2] += penambahan
                    hoodie_sablon['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_sablon['stok'][3] += penambahan
                    hoodie_sablon['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_sablon['stok'][4] += penambahan
                    hoodie_sablon['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        print("")
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 3 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_bordir['stok'][0] += penambahan
                    hoodie_bordir['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 2 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_bordir['stok'][1] += penambahan
                    hoodie_bordir['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 3 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_bordir['stok'][2] += penambahan
                    hoodie_bordir['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_bordir['stok'][3] += penambahan
                    hoodie_bordir['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    hoodie_bordir['stok'][4] += penambahan
                    hoodie_bordir['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        print("")
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 4 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    basic_sweater['stok'][0] += penambahan
                    basic_sweater['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 2 :
            while True:
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    basic_sweater['stok'][1] += penambahan
                    basic_sweater['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 3 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    basic_sweater['stok'][2] += penambahan
                    basic_sweater['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    basic_sweater['stok'][3] += penambahan
                    basic_sweater['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    basic_sweater['stok'][4] += penambahan
                    basic_sweater['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        print("")
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 5 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_polos['stok'][0] += penambahan
                    kaos_polos['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 2 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_polos['stok'][1] += penambahan
                    kaos_polos['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 3 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_polos['stok'][2] += penambahan
                    kaos_polos['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_polos['stok'][3] += penambahan
                    kaos_polos['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else : 
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_polos['stok'][4] += penambahan
                    kaos_polos['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        print("")
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 6 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_sablon['stok'][0] += penambahan
                    kaos_sablon['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 2 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_sablon['stok'][1] += penambahan
                    kaos_sablon['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 3 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_sablon['stok'][2] += penambahan
                    kaos_sablon['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_sablon['stok'][3] += penambahan
                    kaos_sablon['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_sablon['stok'][4] += penambahan
                    kaos_sablon['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        print("")
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 7 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate : "))
        if pilihan_ukuran == 1 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_bordir['stok'][0] += penambahan
                    kaos_bordir['stok'][0] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 2 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_bordir['stok'][1] += penambahan
                    kaos_bordir['stok'][1] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 3 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_bordir['stok'][2] += penambahan
                    kaos_bordir['stok'][2] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 4 : 
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_bordir['stok'][3] += penambahan
                    kaos_bordir['stok'][3] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        elif pilihan_ukuran == 5 :
            while True :
                try :
                    pengurangan = int(input("Masukkan Jumlah Barang Yang akan Dikurangkan(Masukkan 0 jika tidak ada) : "))
                    penambahan = int(input("Masukkan Jumlah Barang Yang akan Ditambahkan(Masukkan 0 jika tidak ada) : "))
                    kaos_bordir['stok'][4] += penambahan
                    kaos_bordir['stok'][4] -= pengurangan
                except :
                    print("Masukkan angka yang benar untuk jumlah barang...")
                else :
                    break
        print("")
        print(">>>>>>>>>>>>>>Barang Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    daftar_barang()
    kembali_ke_menu()

def edit_harga() :
    print("=======================================================")
    print("                       EDIT HARGA                      ")
    print("=======================================================")
    print("[1]. Hoodie Polos ", "\n[2]. Hoodie Sablon", "\n[3]. Hoodie Bordir", "\n[4]. Basic Sweater", "\n[5]. Kaos Polos", "\n[6]. Kaos Sablon", "\n[7]. Kaos Bordir")
    pilihan_tb = int(input("Masukkan Pilihan Anda : "))
    daftar_barang()
    if pilihan_tb == 1 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_polos['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_polos['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_polos['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_polos['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_polos['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 2 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_sablon['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_sablon['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_sablon['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_sablon['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_sablon['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")    
    elif pilihan_tb == 3 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_bordir['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_bordir['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_bordir['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_bordir['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            hoodie_bordir['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 4 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            basic_sweater['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            basic_sweater['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            basic_sweater['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            basic_sweater['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            basic_sweater['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")        
    elif pilihan_tb == 5 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_polos['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_polos['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_polos['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_polos['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_polos['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 6 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_sablon['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_sablon['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_sablon['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_sablon['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_sablon['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    elif pilihan_tb == 7 :
        print("[1]. Ukuran S", "\n[2]. Ukuran M", "\n[3]. Ukuran L", "\n[4]. Ukuran XL", "\n[5]. Ukuran XXL")
        pilihan_ukuran = int(input("Masukkan Ukuran Yang Akan Diupdate Harganya : "))
        if pilihan_ukuran == 1 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_bordir['harga'][0] = harga
        elif pilihan_ukuran == 2 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_bordir['harga'][1] = harga
        elif pilihan_ukuran == 3 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_bordir['harga'][2] = harga
        elif pilihan_ukuran == 4 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_bordir['harga'][3] = harga
        elif pilihan_ukuran == 5 :
            harga = int(input("Harga Diupdate Menjadi : " ))
            kaos_bordir['harga'][4] = harga
        print("")
        print(">>>>>>>>>>>>>>Harga Sudah Diuapdate<<<<<<<<<<<<<<")
        print("")
    kembali_ke_menu()

def menu_admin() :
    print("")
    print("=======================================================")
    print("               MENU ADMIN TREASURE THINGZ              ")
    print("=======================================================")
    print(" [1]     DAFTAR BARANG")
    print(" [2]     UPDATE STOK")
    print(" [3]     EDIT HARGA")
    print(" [0]     EXIT")
    print("=======================================================")
    print("")
    pilihan_ma = int(input("Masukkan Pilihan : "))
    if pilihan_ma == 1 :
        daftar_barang()
        kembali_ke_menu()
    elif pilihan_ma == 2 :
        update_stok()
    elif pilihan_ma == 3 :
        edit_harga()
    elif pilihan_ma == 4 :
        hapus_barang()
    elif pilihan_ma == 0 :
        print("Anda Sudah Keluar Dari Akun Admin...")
        print("")
        line()
        login()

def login() :
    while True :
        username = str(input("Masukkan Username : "))
        password = str(input("Masukkan Password : "))
        if username == "admin" and password == "100" :
            menu_admin()
            print("")
        elif username == "user" and password == "210" :
            daftar_barang()
            print("")

            nama_barang = [""] * (20)
            harga_barang = [0] * (20)
            jumlah_barang = [0] * (20)
            total_harga = [0] * (20)
            total_bayar = [0] * (20)
            discount = [0] * (20)
            no = 0
            p = 0
            r = 0

            while True : 
                print(">>>>>>>>>>>>TULIS PESANAN ANDA<<<<<<<<<<<<<")
                nama_barang[p] = input("Nama Barang ke - " + str(p+1) + ": ")
                harga_barang[p] = int(input("Harga Barang : "))
                jumlah_barang[p] = int(input("Jumlah Barang : "))

                total_harga[p] = harga_barang[p] * jumlah_barang[p]
                discount[p] = total_harga[p] - (total_harga[p] * 0)
                kontinu = input("Apakah Anda Ingin Lanjut? [Y/T] : ")

                p = p + 1

                if not(kontinu=="Y" or kontinu=="y") : break

            total = 0
            print("")
            print("==============================================================")
            print("                       TREASURE THINGZ                        ")
            print("==============================================================")
            print("No       Nama                   Harga       Jumlah      Harga ")
            print("         Barang                 Satuan      Barang      Total ")
            print("==============================================================")

            for r in range(0,p) :
                no = no + 1
                total = total + discount[r]
                if total >=150000 :
                    discount[r] = 0.10 * total
                    total_bayar[r] = total - discount[r]
                elif total>=250000 :
                    discount[r] = 0.25 * total
                    total_bayar[r] = total - discount[r]
                else :
                    discount[r] = 0 * total
                    total_bayar[r] = total - discount[r]
                
                print("{}       {}              {}      {}      {}".format(no, nama_barang[r], harga_barang[r], jumlah_barang[r], total_harga[r]))

            print("==============================================================")
            print("Total Harga : {}".format(total))
            print("Discount : {}".format(discount[r]))
            print("Total Pembayaran : {}".format(total_bayar[r]))
            print("==============================================================")
            print("              TERIMAKASIH SUDAH BERBELANJA DISINI !           ")
            print("                       TREASURE THINGZ                        ")
            print("==============================================================")

        else :
            print("")
            print("Username Atau Password Yang Anda Masukkan Salah!")
            print("Silahkan Masukkan Ulang...")
        print("")

# username admin : 'admin'
# password admin : '100'
# username user : 'user'
# password user : '210'
def line() :
    print("==============================================================================")
    print("                                 TREASURE THINGZ                              ")
    print("                            !!!!!HAPPY SHOPPING!!!!!                          ")
    print("==============================================================================")

line()
login()
