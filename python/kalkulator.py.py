#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py.py
def pokaz_liste():
    print('''Lista działań:
          +  – dodawanie
          -  – odejmowanie
          *  – mnożenie
          /  – dzielenie
          // – dzielenie całkowite
          %  – dzielenie modulo
          ^  – potęgowanie
          !  – silnia
          sin – sinus
          cos – cosinus
          koniec – wyjście z programu
          ''')
          
def pobierz_liczbe(komunikat='Pobierz liczbę: '):
    a = input(komunikat)
    if a.isdigit():
        return int(a)
    return False

def dodaj(a, b):
    return a+b
    
def odejmij(a, b):
    return a-b
    
def mnoz(a, b):
    if b != 0:
        return a*b
    else:
        print("Błąd! Mnożenie przez zero!")
    return False

def dziel(a, b):
    if b != 0:
        return a/b
    else:
        print("Błąd! Dzielenie przez zero!")
    return False
    
def dzielcal(a, b):
    if b != 0:
        return a//b
    else:
        print("Błąd! Dzielenie przez zero!")
    return False

def mod(a, b):
    if b != 0:
        return a%b
    else:
        print("Błąd! Dzielenie przez zero!")
    return False

def poteg(a, b):
        return a**b

def main(args):
    pokaz_liste()
    while True:
        d = input("Wybierz działanie: ")
        if d == '+':
            a = pobierz_liczbe("Podaj pierwszy składnik: ")
            b = pobierz_liczbe("Podaj drugi składnik: ")
            if a and b:
                wynik = dodaj(a, b)
                if wynik:
                    print('{} + {} = {}'.format(a, b, wynik))
        elif d == '-':
            a = pobierz_liczbe("Podaj odjemną: ")
            b = pobierz_liczbe("Podaj odjemnik: ")
            if a and b:
                wynik = odejmij(a, b)
                if wynik:
                    print('{} - {} = {}'.format(a, b, wynik))
        elif d == '*':
            a = pobierz_liczbe("Podaj pierwszy czynnik: ")
            b = pobierz_liczbe("Podaj drugi czynnik: ")
            if a and b:
                wynik = mnoz(a, b)
                if wynik:
                    print('{} * {} = {}'.format(a, b, wynik))
        elif d == '/':
            a = pobierz_liczbe("Podaj dzielną: ")
            b = pobierz_liczbe("Podaj dzielnik: ")
            if a and b:
                wynik = dziel(a, b)
                if wynik:
                    print('{} / {} = {}'.format(a, b, wynik))
        elif d == '//':
            a = pobierz_liczbe("Podaj dzielną: ")
            b = pobierz_liczbe("Podaj dzielnik: ")
            if a and b:
                wynik = dzielcal(a, b)
                if wynik:
                    print('{} // {} = {}'.format(a, b, wynik))
        elif d == '%':
            a = pobierz_liczbe("Podaj dzielną: ")
            b = pobierz_liczbe("Podaj dzielnik: ")
            if a and b:
                wynik = mod(a, b)
                if wynik:
                    print('{} % {} = {}'.format(a, b, wynik))
        elif d == '^':
            a = pobierz_liczbe("Podaj podstawę: ")
            b = pobierz_liczbe("Podaj wykładnik: ")
            if a and b:
                wynik = poteg(a, b)
                if wynik:
                    print('{} ^ {} = {}'.format(a, b, wynik))
        elif d == '!':
            pass
        elif d == 'sin':
            pass
        elif d == 'cos':
            pass
        elif d == 'l':
            pokaz_liste()
        elif d == 'koniec':
            return 0
        else:
            print("Błędny wybór!")
            
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
