#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py

# 2^3 

def czy_naturalna(a):
    if a.isdigit():
        return True
    return False
    
def potega_it(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a 
        return wynik
        
def potega_rek(a,n):
    if a == 0:
        return 1
    return silnia_rek(n, a)

def main(args):
    assert potega_rek(2,0)==1
    assert potega_rek(2,1)==2
    assert potega_rek(0,10)==0
    assert potega_rek(1,10)==1
    assert potega_rek(3,3)==25
    a=(input("Podaj liczbę podstawę:"))
    n=(input("Podaj liczbę wykładnik:"))
    if not czy_naturalna (a) or not czy_naturalna (n):
        print("Błędne dane")
        return 0
    print("{} do potęgi{}={}".format(a,n,potęga_it(int(a), int(n))))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
