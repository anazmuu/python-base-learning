from question import pertanyaan

print("::KUMPULAN SOAL PILIHAN GANDA::\n")

kumpulan_soal = [
    "1). Siapa presiden indonesia sekarang? \n A. Soekarno \n B. Jokowi \n C. Gusdur \n D. Habibi \n\n",
    "2). Ibukota negara indonesia adalah? \n A. Bandung \n B. Semarang \n C. Jakarta \n D. Yogyakarta \n\n",
    "3). Tahun berapa indonesia merdeka? \n A. 1920 \n B. 1955 \n C. 1990 \n D. 1945 \n\n",
    "4). Siapa Wakil dari presiden Soekarno ? \n A. Moh. Hatta \n B. Habibi \n C. Tri Sutrisno \n D. Dr.Soetomo \n\n"
]

soal = [
    pertanyaan(kumpulan_soal[0], "B"),
    pertanyaan(kumpulan_soal[1], "C"),
    pertanyaan(kumpulan_soal[2], "D"),
    pertanyaan(kumpulan_soal[3], "A")
]

def run_test(soal):
    score = 0
    for soal1 in soal:
        jawaban = input(soal1.prompt)
        if jawaban == soal1.jawaban:
            score +=1
    print("Skor kamu : " + str(score) + "/" + str(len(soal)) + " Jawaban Benar")

run_test(soal)