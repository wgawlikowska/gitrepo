#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  palindromy.py

import os

def czy_palindrom(tekst):
    ile = len(tekst)
    for i in range(ile//2):
        if tekst[i]!=tekst[-i-1]:
            return False
    return True
    
def czytaj_dane(plik):
    if not os.path_exists(plik):
        print('Plik niedostepny!')
        return False
    teksty=[]
    with open(plik,"r") as f:
        for wiersz in f:
            teksty.append(linia.strip())
    return teksty
def main(args):
    #tekst=input('Podaj tekst')
    teksty = czytaj_dane('dane01.txt')
    print(teksty)
    ile = 0
    
    # ~if czy_palindrom(tekst):
        # ~print('To Palindrom')
            # ~else:
        # ~print('To nie palindrom')

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
