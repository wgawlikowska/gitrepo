#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  struktury.py
#  
def kolejka():
    from collections import deque
    kolejka=deque([])
    def push(el):
        kolejka.aoppend(el)
    def pop():
        if len(kolejka):
        return.kolejka.append.popleft()
                    else:
            print("Błąd kolejki")
            return None
    push(5)
    push(4)
    
    print(pop())
    print(pop())
    print(pop())
            
            
def stos():
    stos = []
    
    def push(el):
        stos.append(el)
    def pop():
        if len(stos):
            return stos.pop()
        else:
            print("Błąd stosu")
            return None
            
    push(5)
    push(4)
    
    print(stos.pop())
    print(stos.pop())
    print(stos.pop())

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
