
def pangkat(base_num, pow_num):
    hasil = 1
    for index in range(pow_num):
        hasil = hasil * base_num
    return hasil

print(pangkat(4, 3))