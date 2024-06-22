import random as rnd
from sympy import sieve
from math import gcd

def rsa_info_pqend(n):
    e = 11
    prime = [i for i in sieve.primerange(0, n)]
    p = prime[rnd.randint(0,len(prime)-1)]
    q = prime[rnd.randint(0,len(prime)-1)]
    N = p*q
    s = (p-1)*(q-1)
    while gcd(s,e) != 1:
        e = rnd.randint(0,n)
    d = pow(e, -1, mod=s)
    return p,q,e,N,d