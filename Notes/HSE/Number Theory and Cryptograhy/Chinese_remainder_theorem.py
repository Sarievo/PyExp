def gcd(a, b):
    assert a >= b >= 0 and a + b > 0
    return gcd(b, a % b) if b > 0 else a

def extended_gcd(a: int, b: int):
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return d, x, y

def ExtendedEuclid(a: int, b: int) -> tuple[int, int]:
    # return (x, y) such that ax + by = gcd(a, b)
    if b == 0:
        return 1, 0
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return y, x - k * y

# use extended Euclid's algorithm to find such x, y that ax + ay = 1
# take n = ra * by + rb * ax


print(extended_gcd(686579304, 26855093))


def ChineseRemainderTheorem(n1, r1, n2, r2):
    (x, y) = ExtendedEuclid(n1, n2)
    print(str(x) + " " + str(y))
    assert n1 * x + n2 * y == 1
    return (r1 * y * n2 + r2 * x * n1) % (n1 * n2)


print(ChineseRemainderTheorem(76, 14, 7, 3))
print(ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207))
