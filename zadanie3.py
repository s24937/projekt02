print("Jak masz na imie oraz nazwisko?")
imieNazwisko= input()
print("Witaj ", imieNazwisko + "! \nZapraszam do wypelnienia ankiety\n")


print("1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")

a = "a) oglądanie telewizji/ filmów/ seriali"
b = "b) czytanie książek/czasopism"
c = "c) słuchanie muzyki"
d = "d) spotkania z rodziną/przyjaciółmi"
e = "e) podróżowanie"
f = "f) uprawianie sportu"
g = "g) inne, jakie?"

print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g )

odpowiedz1= input()

if odpowiedz1 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz1 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz1 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz1 == 'd':
    print("wybrana odpowiedz to: " + d)

if odpowiedz1 == 'e':
    print("wybrana odpowiedz to: " + e)

if odpowiedz1 == 'f':
    print("wybrana odpowiedz to: " + f)

if odpowiedz1 == 'g':
    wlasna_odpowiedz1 = input()
    print("wybrana odpowiedz to: " + wlasna_odpowiedz1)
    odpowiedz1 = wlasna_odpowiedz1

print("\n")
#2

print ("2. W jakich okolicznościach czytasz książki najczęściej? ")

a = "a) podczas podróży"
b = "b) w czasie wolnym (po pracy, na urlopie)"
c = "c) podczas pracy/nauki (to ich element)"
d = "d) w ogóle nie czytam"
e = "e) inne, jakie?"

print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e )

odpowiedz2 = input()

if odpowiedz2 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz2 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz2 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz2 == 'd':
    print("wybrana odpowiedz to: " + d)

if odpowiedz2 == 'e':
    wlasna_odpowiedz2 = input()
    print("wybrana odpowiedz to: " + wlasna_odpowiedz2)
    odpowiedz2 = wlasna_odpowiedz2

print("\n")
#3

print("3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")

a = "a) chęć poszerzenia wiedzy"
b = "b) czytanie mnie relaksuje/odpręża"
c = "c) fakt, że czytanie jest modne"
d = "d) czytanie to moje hobby"
e = "e) konieczność nauki w związku z wykonywaną pracą/studiami"
f = "f) odczuwam presję rodziny/środowiska, żeby czytać"
g = "g) inne, jakie?"


print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g)


odpowiedz3 = input()

if odpowiedz3 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz3 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz3 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz3 == 'd':
    print("wybrana odpowiedz to: " + d)

if odpowiedz3 == 'e':
    print("wybrana odpowiedz to: " + e)

if odpowiedz3 == 'f':
    print("wybrana odpowiedz to: " + f)

if odpowiedz3 == 'g':
    wlasna_odpowiedz3 = input()
    print ("wybrana odpowiedz to: " + wlasna_odpowiedz3)
    odpowiedz3 = wlasna_odpowiedz3

print("\n")
#4


print("4. Po książki w jakiej formie sięgasz najczęściej?")

a = "a) papierowej (tradycyjnej)"
b = "b) e-booki (książki elektroniczne) na komputerze"
c = "c) e-booki na tablecie/telefonie"
d = "d) e-booki na specjalnym czytniku (np. Kindle)"


print(a + "\n" + b + "\n" + c + "\n" + d)


odpowiedz4= input()

if odpowiedz4 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz4 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz4 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz4 == 'd':
    print("wybrana odpowiedz to: " + d)

print("\n")
#5


print("5. Ile książek czytasz średnio w ciągu roku?")

a = "a) 0"
b = "b) żadnej w całości - jedynie fragmenty"
c = "c) 1"
d = "d) 2 lub 3"
e = "e) 4-10"
f = "f) powyżej 10"


print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f)


odpowiedz5= input()

if odpowiedz5 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz5 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz5 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz5 == 'd':
    print("wybrana odpowiedz to: " + d)

if odpowiedz5 == 'e':
    print("wybrana odpowiedz to: " + e)

if odpowiedz5 == 'f':
    print("wybrana odpowiedz to: " + f)

print("\n")
#6

print("6. Jak często średnio czytasz książki? ")

a = "a) codziennie"
b = "b) raz w tygodniu"
c = "c) raz w miesiącu"
d = "d) raz na kilka miesięcy"
e = "e) raz na pół roku"
f = "f) raz na rok"
g = "g) wcale"

print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g)

odpowiedz6= input()

if odpowiedz6 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz6 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz6 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz6 == 'd':
    print("wybrana odpowiedz to: " + d)

if odpowiedz6 == 'e':
    print("wybrana odpowiedz to: " + e)

if odpowiedz6 == 'f':
    print("wybrana odpowiedz to: " + f)

if odpowiedz6 == 'g':
    print("wybrana odpowiedz to: " + g)

print("\n")
#7


print("7. Po jakie gatunki książek sięgasz najczęściej?")

a = "a) kryminały/thrillery"
b = "b) romanse"
c = "c) psychologiczne"
d = "d) horrory"
e = "e) naukowe"
f = "f) dla dzieci i młodzieży"
g = "g) fantastykę"
h = "h) biograficzne"
i = "i) historyczne"
j = "j) science fiction"
k = "k) podróżnicze"
l = "l) hobbystyczne (gotowanie, wędkarstwo itp.)"
m = "m) przygodowe"
n = "n) poezję"
o = "o) inne, jakie?"


print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e + "\n" + f + "\n" + g+ "\n" + h + "\n" + i + "\n" + j + "\n" + k+ "\n" + l+ "\n" + m + "\n" + n + "\n" + o)


odpowiedz7= input()

if odpowiedz7 == 'a':
    print("wybrana odpowiedz to: " + a)

if odpowiedz7 == 'b':
    print("wybrana odpowiedz to: " + b)

if odpowiedz7 == 'c':
    print("wybrana odpowiedz to: " + c)

if odpowiedz7 == 'd':
    print("wybrana odpowiedz to: " + d)

if odpowiedz7 == 'e':
    print("wybrana odpowiedz to: " + e)

if odpowiedz7 == 'f':
    print("wybrana odpowiedz to: " + f)

if odpowiedz7 == 'g':
    print("wybrana odpowiedz to: " + g)

if odpowiedz7 == 'h':
    print("wybrana odpowiedz to: " + h)

if odpowiedz7 == 'i':
    print("wybrana odpowiedz to: " + i)

if odpowiedz7 == 'j':
    print("wybrana odpowiedz to: " + j)

if odpowiedz7 == 'k':
    print("wybrana odpowiedz to: " + k)

if odpowiedz7 == 'l':
    print("wybrana odpowiedz to: " + l)

if odpowiedz7 == 'm':
    print("wybrana odpowiedz to: " + m)

if odpowiedz7 == 'n':
    print("wybrana odpowiedz to: " + n)

if odpowiedz7 == 'o':
    wlasna_odpowiedz7 = input()
    print("wybrana odpowiedz to: " + wlasna_odpowiedz7)
    odpowiedz7 = wlasna_odpowiedz7

print("\n")

print("Dziekuje za wypełnienie ankiety " + imieNazwisko + "!" )