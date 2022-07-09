a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

is_male = True
is_tall = True

if is_male or is_tall:
  print("Kamu laki laki atau tinggi atau keduanya")
else:
  print("Kamu bukan laki laki atau tinggi")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
      return num1
    elif num2 >= num1 and num2 >= num3:
      return num2
    else:
      return num3

print(max_num(3, 40, 5))