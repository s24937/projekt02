
print("podaj liczbę a")
a = float(input())

print("podaj liczbę b")
b = float(input())
print("podaj operator logiczny ('+', '-', '*', '/')")

c = input()

if c == "+":
    print("wynik wynosi: ", a + b )

if c == '-':
    print("wynik wynosi: ", a-b)

if c == '*':
    print("wynik wynosi: ", a*b)

if c == '/':
    print("wynik wynosi: ", a / b)


