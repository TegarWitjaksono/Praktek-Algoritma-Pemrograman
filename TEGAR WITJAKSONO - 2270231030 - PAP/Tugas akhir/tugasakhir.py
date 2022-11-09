import time;
localtime = time.ctime()

print("----------------- Program Kasir Warung UNKRIS -----------------")
Pelanggan = input("Masukkan nama pelanggan: ")
print ("Nama Pelanggan :", Pelanggan) 

alamat = input("Masukkan alamat pelanggan: ")
print ("alamat Pelanggan :", alamat) 

telepon = input("Masukkan No. tlp Pelanggan: ")
print ("No.tlp Pelanggan :", telepon) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   global satuan
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Soto - Rp 9000")
   print("3. Mie Ayam - Rp 11000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   if nomor==1:
       satuan=15000
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       satuan=9000
       totalmkn=porsi*9000
       print (porsi," porsi Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       satuan=11000
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   global satuanmnm
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Es kopi - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       satuanmnm=2000
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       satuanmnm=3500
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       satuanmnm=4000
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pelanggan: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("======= W A R U N G  U N K R I S =======")
print("==================================")
print ("Nama\t\t:",Pelanggan)
print ("alamat\t\t:",alamat)
print ("no.tlp\t\t:",telepon)
print ("Membeli pada\t:",localtime)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Satuan\t\t:",mkn, "( Rp", satuan,")")
print ("\t\t"   ,   mnm, "( Rp",satuanmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")