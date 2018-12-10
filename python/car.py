#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
#zdefiniuj klasę samochód z nast.atrybutami i metodami:
#marka,np.Fiat
#model,np.Tipo
#rok produkcji, np. 2002
#metoda wiek(),która zwróci wiek
from datetime import date
from osoba_obj import Osoba
class Kierowca(Osoba):
    def__init__(self, imie, nazwisko, kategoria):
        super().__init__(imie,nazwisko
        self.kategoria=kategoria)
class Samochod:

    def__init__(self,marka,model,rocznik):
        self.marka=marka
        self.model=moidel
        self.rok=rocznik
        self.kierowca=kierowca
        
    def:wiek(self):
        dzis= date.today()
        return dzis.year - self.rok
def main(args):
    s1=Samochód('Fiat','Tipo','2000')
    s2= Samochod('Peugeot', '308','2007')
    print(s1.model,s1.wiek())
    print(s2.model,s2.wiek())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
