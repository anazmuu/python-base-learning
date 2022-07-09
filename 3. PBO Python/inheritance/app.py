from fauna import hewan
from fauna import fams
from piscesfam import aves

hewan1 = hewan("Gajah Sumatera", "Mamalia", "Hutan", "Belalai")

print("Nama   : " + hewan1.nama)
print("Family : " + hewan1.family)

jenisFamily = fams()
jenisFamily.mamalia()

jenisAves = aves()
jenisAves.pisces()
