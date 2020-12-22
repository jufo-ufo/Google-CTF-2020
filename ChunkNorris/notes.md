# Notes Yeah!


## Code

### Gen Prime
```python
a = 0xe64a5f84e2762be5
chunk_size = 64

def gen_prime(bits):
  s = random.getrandbits(chunk_size)

  while True:
    s |= 0xc000000000000001
    p = 0
    for _ in range(bits // chunk_size):
      p = (p << chunk_size) + s
      s = a * s % 2**chunk_size
    if gmpy2.is_prime(p):
      return p
```

### Flag
```python
n = gen_prime(1024) * gen_prime(1024)
e = 65537
flag = open("flag.txt", "rb").read()
print('n =', hex(n))
print('e =', hex(e))
print('c =', hex(pow(bytes_to_long(flag), e, n)))
```

---
## Analyse 
### Flag
 - Probably RSA -> Get Primes factors of n
 - Primes so large -> no factorization possible

### Gen Prime
 - Probably The weak spot aka the security hole
 - number is always 1024 bits long, first and last bit is always set!

---
## Ideas
 No Ideas 
