num1 = float(input("Masukkan angka pertama : "))
operator = input("Masukkan Operator : ")
num2 = float(input("Masukkan angka kedua : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("inputan salah")

