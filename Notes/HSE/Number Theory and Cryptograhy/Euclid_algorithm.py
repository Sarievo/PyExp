# def gcd(a, b):
#     assert a >= b >= 0 and a + b > 0
#     return gcd(b, a % b) if b > 0 else a

# def extended_gcd(a: int, b: int):
#     assert a >= 0 and b >= 0
#
#     if b == 0:
#         d, x, y = a, 1, 0
#     else:
#         (d, p, q) = extended_gcd(b, a % b)
#         x = q
#         y = p - q * (a // b)
#
#     assert a % d == 0 and b % d == 0
#     assert d == a * x + b * y
#     return d, x, y

# def extended_euclid(a: int, b: int) -> tuple[int, int]:
#     if b == 0:
#         return 1, 0
#     (x, y) = extended_euclid(b, a % b)
#     k = a // b
#     return y, x - k * y

# def diophantine(a, b, c):
#     (d, x, y) = extended_gcd(a, b)
#     assert c % d == 0
#     factor = c // d
#     return factor * x, factor * y
#
#
# print(diophantine(3, 5, 2))

# def invert_modulo(a: int, n: int) -> int:
#     """
#     This function find the inverses of a i.e., a^(-1)
#     >>> invert_modulo(2, 5)
#     3
#     >>> invert_modulo(8,7)
#     1
#     """
#     (b, x) = extended_euclid(a, n)  # Implemented below
#     if b < 0:
#         b = (b % n + n) % n
#     return b

# def divide(a, b, n):
#     assert n > 1 and a > 0 and gcd(a, n) == 1
#
#     a = a % n
#     inv = pow(b, n - 2, n)
#     return (inv * a) % n


# def divide(a, b, n):
#     return pow(b, n - 2, n) * a % n

# print(divide(11, 4, 5))

# def lcm(a, b):
#     assert a > 0 and b > 0
#     product = a * b
#     while a > 0 and b > 0:
#         if a >= b:
#             a = a % b
#         else:
#             b = b % a
#     return product // max(a, b)
