
# zadanie1
print("\nzadanie1 \n ")

a= "Python 2023"
b = "Python 2023"
c = "Python 2023"

print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))

# zadanie1a
print("\nzadanie1a \n ")
print(a == b)
print(b == c)

# zadanie1b
print("\nzadanie1b \n ")

print(id(a))
print(id(b))
print(id(c))

print("adres liczb w postaci heksadecymalnej: ", hex(int(id(a))))
print("adres liczb w postaci heksadecymalnej: ", hex(int(id(b))))
print("adres liczb w postaci heksadecymalnej: ", hex(int(id(c))))

print(type(a))
print(type(b))
print(type(c))

c ="Java 11"
print(c)
print("po zmianie c")
print()
print(a == b)
print(b == c)
print()

print(id(a))
print(id(b))
print(id(c))
print()
print("adres liczb w postaci heksadecymalnej: ", hex(int(id(a))))
print("adres liczb w postaci heksadecymalnej: ", hex(int(id(b))))
print("adres liczb w postaci heksadecymalnej: ", hex(int(id(c))))