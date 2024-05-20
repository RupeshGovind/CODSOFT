import random
Operations = ["Add  +","Subtract +","Multiply *","Divide /",
            "Expontiation **","Modulus %","Floor division //"]

random.shuffle(Operations)

for item in Operations:
 print(item)

print("  ")

num1 = int(input("Type your first number__"))
num2 = int(input("Type your second number__"))

choice = input("Enter choice (+),(-),(*),(**),(/),(//),(%)______")

a = num1 + num2
b = num1 - num2
c = num1 * num2
d = num1 / num2
f = num1 ** num2
e = num1 % num2
g = num1 //num2

if choice == "+":
  print(f"{num1} + {num2} = {a}")

elif choice == "-":
 print(f"{num1} - {num2} = {b}")

elif choice == "*":
  print(f"{num1} * {num2} = {c}")

elif choice == "/":
  print(f"{num1} / {num2} = {d}")

elif choice == "%":
  print(f"{num1} % {num2} = {e}")

elif choice == "**":
  print(f"{num1} ** {num2} = {f}")
elif choice == "//":
  print(f"{num1} // {num2} = {g}")
else:
  a = ("invalid operations")
  print(a.center(50,"_"))

