#Berisi key dan Value
#setiap key di pisah oleh semicolon ;

bulan = {
    "Jan" : "Januari",  # KEY : Value
    "Feb" : "Februari",
    "Mar" : "Maret"
}

print(bulan)
print(bulan["Jan"]) #Memanggil key satu persatu
print(bulan.get("Feb")) #memanggil menggunakan get