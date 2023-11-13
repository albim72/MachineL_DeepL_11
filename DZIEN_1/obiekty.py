from datetime import datetime as dt

class Osoba:
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls, *args, **kwargs)
    def __init__(self,imie,nazwisko,rok_ur,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok_ur
        self._waga = waga
        self.wzrost = wzrost


    @property
    def wiek(self):
        return dt.now().year - self.rok
    
    def printosoba(self):
        return (f'osoba: {self.imie}  {self.nazwisko}, wiek[lata]: {self.wiek}, '
                f'waga: {self._waga} kg, wzrost: {self.wzrost} cm')

    @property
    def waga(self):
        return self._waga, self.bmi

    @waga.setter
    def waga(self,nowawaga):
        self._waga = nowawaga
        self.bmi = self._waga/(self.wzrost/100)**2


os = Osoba("Jan","Kot",1976,88,176)
print(os)
print(os.printosoba())
os.waga = 100
print(os.printosoba())
waga,bmi = os.waga
print(f'waga[kg] po zmianie: {waga}')
print(f'bmi ciała: {bmi:.2f}')
