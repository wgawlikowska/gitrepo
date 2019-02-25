#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  napisy.py

def pobierz_dane1():
    imie = imput('Podaj imie:').strip()
    nazwisko = imput('Podaj nazwisko:').strip
    print("Witaj {} {}!".format(imie.strip().capilalize(),nazwisko.strip().capitalize()))
    
    if len(imie)>len(nazwisko):
        print("Imię>nazwisko")
    elif len(imie)<len(nazwisko):
        print("Imię<nazwisko")
    else:
        print("Imię==nazwisko")
        
    if imie[-1]=='a':
        print("kobieta")
    else:
        print("mężczyzna")
        
        
def pobierz_dane2():
    nazwa = input("Imię i nazwisko:").strip()
    while nazwa.count('')!=1:
       nazwa = input("Imię i nazwisko:").strip() 
    samogłoski = set(['a','o','u','e','y','i','ę','ą'])
    imie= set([',','.','!','?'])
    
    ileSa=0
    for znak in nazwa:
        if znak in samogloski:
            ileSa+=1
        elif znak not in imie:
            ileSp+=1
    if ileSa > ileSp:
        print("Samogłoski>spółgłoski")
    elif ileSa<ileSp:
        print("Spółgłoski>samogłoski")
    else:
        print("Samogłoski = spółgłoski")
        
def pobierz_dane3():
     napis1 = input("Tekst:").strip()
     napis2=
     inne= set([',','.','!','?','!','',])
     for znak in napis1:
         if znak not in inne and not znak.isdigit():
             if znak.islower():
                 napis2+=znak.upper()
                else:
                    napis2 += znak.lower()
                else:
                    napis2

def main(args):
    #pobierz_dane1()
    pobierz_dane2()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
