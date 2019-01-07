#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gawlikowska_petle.py
def cwl1():
    suma = 0
    liczba = int(input("Podaj liczbę:"))
    while suma <=75:
        suma += liczba
        print(suma)
        liczba=int(input("Podaj liczbę:"))
    print()


def cwl2():
    

    n=int(input("Od:"))
    m=int(input("Do:"))
    for in range(n,m+1):
 print(i, end=' ')




def cwl3():
licznik=0
    n = int(input("Liczba:"))
    for in range (n+1):
        print(i*i)
        
    
    
    
    


def main(args):
    cwl1()
    cwl2()
    cwl3()
    print()
    print()
    print(kwadrat)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
