'''
ini adalah komentar

'''

def translate(phrase):
    translation = ""
    for huruf in phrase:
        if huruf.lower() in "aiueo":
            if huruf.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + huruf
    return translation

print(translate(input("Masukkan Kata : ")))

