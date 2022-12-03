#List : Data sesuai indeks dengan urutan
#List : dimulai dari 0 dan seterusnya
#List : Data dalam list tidak boleh sama
#List : Data dapat dirubah

buah = ["Apple", "Mangga", "Stroberi", "Durian"] #List seperti array
          #0        #1          #2        #3
          
buah2 = ["sirsak", "jeruk", "anggur", "pisang"]
angka = [14, 8, 17, 20]

print(buah)
#output : ['Apple', 'Mangga', 'Stroberi', 'Durian']
print(buah[2]) #pemanggilan secara satu satu
#output : Stroberi
print(buah[1:3]) #memanggil secara range
#output :['Mangga', 'Stroberi']
buah[0] = "Anggur" #mengganti huruf

### LIST FUNCTION ###
buah.extend(angka) #gabungan antara list 1 dan lainnya
print(buah)
#output : ['Anggur', 'Mangga', 'Stroberi', 'Durian', 14, 8, 17, 20]
buah.append("Pepaya") #menambahkan data di akhir
print(buah)
#output : ['Anggur', 'Mangga', 'Stroberi', 'Durian', 14, 8, 17, 20, 'Pepaya']
buah.insert(1, "Markisa") #menambahkan data dengan di sesuaikan posisinya
print(buah)
#output : ['Anggur', 'Markisa', 'Mangga', 'Stroberi', 'Durian', 14, 8, 17, 20, 'Pepaya']
buah.remove("Pepaya") #menghapus data sesuai nama
print(buah)
#output : ['Anggur', 'Markisa', 'Mangga', 'Stroberi', 'Durian', 14, 8, 17, 20]
angka.pop() #menghapus data terakhir
print(angka)
#output :[14, 8, 17]
print(buah.index("Markisa")) #memanggil data secara posisi
#output : 1
print(buah.count("Apple")) #menghitung jumlah data pada list
#output : 0
buah2.sort()
print(buah2) #di sort sesuai abjad pertama
#output : ['anggur', 'jeruk', 'pisang', 'sirsak']
angka.sort()
print(angka) #di sort sesuai nilai terkecil
#output : [8, 14, 17]
angka.reverse()
print(angka) #sort terbalik dari terbesar
#output : [17, 14, 8]

buah3 = buah.copy() #membuat list baru dengan copy list
print(buah3)

#output : ['Anggur', 'Markisa', 'Mangga', 'Stroberi', 'Durian', 14, 8, 17, 20]
