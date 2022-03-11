import math
#lista1zad1

var1 = 5
var2 = 2
var3 = 2.5
var4 = 4.5
var5 = "Adrian"
var6 = "Patrycja"

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)

#lista1zad2

dodawanie = var1 + var2
odejmowanie = var1 - var2
mnozenie = var1 * var2
dzielenie = var1 / var2

print("Dodawanie: " + str(dodawanie))
print("Odejmowanie: " + str(odejmowanie))
print("Mnozenie: " + str(mnozenie))
print("Dzielenie: " + str(dzielenie))

#lista1zad3

var1 += 1
var1 -= 1
var1 *= 1
var1 /= 1
var1 **= 1
var1 %= 1


#lista1zad4

e = 3
potega = pow(e, 10)
print(potega)
pierwiastek = pow(math.log(5+pow(math.sin(8),2)),1/6)
print(pierwiastek)
bezwzgl = math.fabs(3.55)
print(bezwzgl)
bezwzgl = math.fabs(4.80)
print(bezwzgl)

#lista1zad5

imie = "ADRIAN"
nazwisko = "KWIATKOWSKI"

imie = imie.capitalize()
nazwisko = nazwisko.capitalize()

print(imie + " " + nazwisko)

#lista1zad6

piosenka = "la la la la la la la la la la la la la"
x = piosenka.count("la")
print(x)

#lista1zad7
string = "Nie pije alkoholu w ciąży"
print(string[1] + " " + string[len(string) - 1])

#lista1zad8

print(piosenka.split(" "))

#lista1zad9

a = "Adrian"
b = 15.5
c = 0x54
print(str(a))
print(float(b))
print(hex(c))

#lista2zad1

lista = ["łyżwiarstwo", "hokej", "piłka nożna", "siatkówka"]
lista.reverse()
lista.append("skoki narciarskie")
lista.append("rzut kulą")
print(lista)

#lista2zad2

slownik = {'itp.' : 'I tym podobne', 'np.' : "Na przykład", 'itd.' : 'I tak dalej', 'cd.' : 'Ciąg dalszy'}

#lista2zad3

gry = {'Fifa' : 'Electronic Arts', 'Far Cry' : 'Ubisoft', 'Gothic' : 'Piranha Bytes', 'Mass Effect' : 'BioWare'}
print("Ilość gier: " + str(len(gry.keys())))

#lista2zad4
counter = 0
print("Podaj zdanie: ")
#zdanie = input()
#for x in range(len(zdanie)):
    #if zdanie[x] == 'a':
        #counter+=1

print("Ilość litery a w zdaniu: " + str(counter))

#lista2zad5

file = open('plik.txt', 'r')
a = int(file.readline())
b = int(file.readline())
c = int(file.readline())
wynik = pow(a, b) + c
file.close()
file = open('plik.txt', 'a')
file.write('\n' + str(wynik))
file.close()


#lista2zad6

a = 1000
b = 324
c = 18

if a>b:
    if a>c:
        max = a
    else:
        max = c
else:
    if b>c:
        max = b
    else:
        max = c

#lista2zad7

lista = [13 , 12.5, 8, 54, 6.9, 11]

for x in range(len(lista)):
    lista[x] **= 2

#lista2zad8

parzyste = []
i = 0
while i <= 9:
    x = input()
    x = int(x)
    i += 1
    if x % 2 == 0:
        parzyste.append(x)

print(parzyste)


#lista2zad9
number = input()
number = int(number)


if number < 0:
    print("Liczba jest ujemna!")
else:
    wynik = math.sqrt(number)
    print(wynik)
