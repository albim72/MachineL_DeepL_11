#przykład 1
n=100
def policz(a,b,c=1):
    global n
    n = (a+b)*c + n
    return n

print(policz(4,7,3))
print(policz(4,7))
print(n)


#przykład 2
num = [67,8.9,-1,0,34,55,100,-99,35,68,98,2,8,0,9]
kr = [(9,4),(9,6),(11,45),(2,101)]

parzyste = list(filter(lambda x:x%2==0,num))
print(parzyste)

cube = list(map(lambda x:x**3,num))
print(cube)

def multifive(n):
    return n*5

five = list(map(multifive,num))
print(five)

def multifiveplus(n):
    return n[0]*5+n[1]

dwa = list(map(multifiveplus,kr))
print(dwa)

#przykład 3

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f'Uczestnik konkursu {imie}, liczba punktów: {punkty}'

def kierowca(imie,latad,prawoj = True,kraj="PL"):
    return f"kierowca {imie}, doświadczenie: {latad} lat, prawo jazdy: {prawoj}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Henryk"))
print(osoba(konkurs,"Olga", 56))
print(osoba(kierowca,"Leon",6))
print(osoba(kierowca,"Leon",6,False,"SLO"))

#przykład 4 - funkcje dekoracyjne
def startstop(funkcja):
    def wrapper(*args):
        print("_"*35)
        print("startowanie funckji...")
        funkcja(*args)
        print("kończenie funkcji...")
        print("_"*35)
    return wrapper


def zawijanie(czego):
    print(f'zawijanie {czego} w sreberka.')

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na torcie urodzinowym")

dmuchanie("świeczek")


def startoblicz(funkcja):
    def wrapper(*args):
        print("_"*35)
        print("startowanie funckji...")
        g = funkcja(*args) + 4
        print(f"wynik 6*f(x) = {6*g}")
        print("kończenie funkcji...")
        print("_"*35)
        return g
    return wrapper

@startoblicz
def fx(a,b):
    return a*2+b

wynik = fx(6,8)
print(wynik)

