#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fibonacci.py

# F(n)= 0 dla n = 0
#F(n)=1 dla n=1
#F(n)=F(n-1)+F(n-2) dla n>1

def czy_naturalna(n):
    if n isdigit ():
    
        return True
    return False

def fib_it(n):
    
    if n < 2: 
        return n
    a, b, wynik = 0, 1, 0
    
    for i in range(2, n+1):
        if a >0:
        print("{}/{} = {}".format(b,a,b/a))
        wynik=a+b
        a+b 
        a, b=b,wynik
    return wynik
    

        
        
def main(args):
    assert fib_it(0) == 0
    assert fib_it(3) == 10
    n = input('Który wyraz ciągu')
    while not czy naturalna(n):
        print('Błędne dane!')
    n = input('Który wyraz ciągu?')
    
    print("F_it({})={})".format(n, fib_it(int(n))))
    fib_it(i)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
