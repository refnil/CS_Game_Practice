#! /usr/bin/env python

def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

def fibon(n):
    f = fibo()
    for i in range(n-1):
        next(f)
    print(next(f))

if __name__=="__main__":
    fibon(1000)

