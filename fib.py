# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:45:28 2021

@author: vathsav
"""
a=0;
b=1;
n=int(input());
print(a);
print(b);
fib=0;
fib=a+b;
while True:
    fib=a+b;
    a=b;
    b=fib;
    if fib<n:
        print(fib);
    else:
        break;
   