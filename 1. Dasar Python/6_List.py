#List : Data sesuai indeks dengan urutan
#List : dimulai dari 0 dan seterusnya
#List : Data dalam list tidak boleh sama
#List : Data dapat dirubah

buah = ["Apple", "Mangga", "Stroberi", "Durian"] #List seperti array
          #0        #1          #2        #3
angka = [14, 8, 17, 20]

#print(buah)
#print(buah[2]) #pemanggilan secara satu satu
#print(buah[1:3]) #memanggil secara range

#buah[0] = "Anggur" #mengganti huruf

#print(buah)


### LIST FUNCTION ###
#buah.extend(angka) #gabungan antara list 1 dan lainnya
#print(buah)
buah.append("Pepaya") #menambahkan data di akhir
print(buah)
buah.insert(1, "Markisa") #menambahkan data dengan di sesuaikan posisinya
print(buah)
buah.remove("Pepaya") #menghapus data sesuai nama
print(buah)
angka.pop() #menghapus data terakhir
print(angka)
print(buah.index("Markisa")) #memanggil data secara posisi
print(buah.count("Apple")) #menghitung jumlah data pada list
buah.sort()
print(buah) #di sort sesuai abjad pertama
angka.sort()
print(angka) #di sort sesuai nilai terkecil
angka.reverse()
print(angka) #sort terbalik dari terbesar

buah2 = buah.copy() #membuat list baru dengan copy list

print(buah2)