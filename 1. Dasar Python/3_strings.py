kata = "Panda Di Kebun Binatang" #string di inisiasi dengan "..."

print(kata + " Sangat lucu") #pada string bisa di tambahkan kalimat atau teks lain
#output : panda di kebun binatan sangat lucu
print(kata.lower()) #Lower berfungsi untuk mengecilkan font
#output :panda di kebun binatang
print(kata.upper()) #upper berfungsi untuk membesarkan font
#output :PANDA DI KEBUN BINATANG
print(len(kata)) #Menghitung panjang karakter
#output : 23
print(kata[1]) #memanggil huruf sesuai posisi array
#output : a
print(kata.index("K")) #index mencari posisi huruf sesuai posisi array
#output : 9
print(kata.replace("Kebun", "Taman")) #Replace mengganti kata dalam suatu kalimat
#output : Panda Di Taman Binatang
