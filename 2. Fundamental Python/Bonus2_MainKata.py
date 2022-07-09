print("Soal 1 : Hewan Apa yang mempunyai Belalai ? ")

kata_rahasia = "Gajah"
guess = ""
guess_count = 0
guess_limit = 3 #batas nyawa
out_of_guess = False

while guess != kata_rahasia and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Masukkan Jawaban : ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Kesempatan Habis, kamu kalah")
else:
    print("Kamu Berhasil !")