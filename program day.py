print("contoh soal kasus 1")
nama_karyawan=input("nama karyawan:")
banyak_anak=int(input("banyak anak:"))
gaji_pokok=int(input("gaji pokok:"))
tunjangan_istri=20/100*gaji_pokok
tunjangan_anak=5/100*gaji_pokok
total_tunjangan=tunjangan_istri+tunjangan_anak
gaji_kotor=gaji_pokok+total_tunjangan
pajak=10/100*gaji_kotor


if tunjangan_istri and tunjangan_anak != gaji_pokok :
    print("tunjangan istri:",tunjangan_istri)
    print("tunjangan anak:",tunjangan_anak)

print("total_tunjangan:",total_tunjangan)
print("gaji_kotor:",gaji_kotor)
print("pajak:",pajak)
print("gaji_bersih:",gaji_kotor-pajak)

print("contoh kasus ke 2")
jumlah_sak_semen=int(input("banyak sak semen:"))
harga=jumlah_sak_semen*50000


if jumlah_sak_semen == 100:
    print("total harga semen maksimal 100 :",harga-(harga*25/10/100))
elif jumlah_sak_semen > 200:
    print("total harga semen di atas 200:",harga-(harga*10/100))
else:
    print("tidak mendapatkan potongan",harga)
    
