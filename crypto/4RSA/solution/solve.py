from Crypto.Util.number import *
from itertools import combinations
import math

phi = 5766519321732303614602774063039817994229059369350942586704472004284400792639050641102051094143465282172553506082870684687445379400436177178525327208209136

# since the bit length of phi is 511 the bit length of the primes should be 255 or 256
print(phi.bit_length()) # 511

# https://www.dcode.fr/decomposition-nombres-premiers
factors = [
    2,
    2,
    2,
    2,
    11,
    53,
    1231,
    3011,
    6311,
    42764336533,
    6092059936124221,
    302778436501851567289,
    15891009937926808303685601511,
    155281495565701884820879394479,
    135773862498011055774105095957930299,
]

assert all(isPrime(p) for p in factors), "we need all the factors to be primes so we can get the public modulus"

p=1
out = False
l = len(factors)
for i in range(1, l + 1):
    for combo in combinations(factors, i):
        product = math.prod(combo)
        if isPrime(product + 1) and (product + 1).bit_length() in [255, 256]:
            out = True
            p = product + 1
            print(p)
            break
    if out:
        break

assert p!=1, "attack failed"
q = phi // (p - 1) + 1
print(q)
e = 0x10001
c = 611142254405063827592801146302447289406583406739037319967831929495820356540197143799949439570575545193567545373382063508745891664959358452805982104434526
d = inverse(e,phi)
n = p * q
m = pow(c, d, n)
print(long_to_bytes(m).decode())
