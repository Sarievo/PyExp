def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res


def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
            return b
        else:
            return b * a % mod


def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


def Encrypt(message, modulo, exponent):
    return PowMod(ConvertToInt(message), exponent, modulo)


def Decrypt(ciphertext, p, q, exponent):
    d = InvertModulo(exponent, (p - 1) * (q - 1))
    return ConvertToStr(PowMod(ciphertext, d, p * q))


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    # brutal force using dictionary
    for i in range(len(potential_messages)):
        if ciphertext == Encrypt(potential_messages[i], modulo, exponent):
            return potential_messages[i]
    return "don't know"


def DecipherSmallPrime(ciphertext, modulo, exponent):
    for i in range(2, 1000000):
        if modulo % i == 0:
            small_prime = i
            big_prime = modulo // i
            return Decrypt(ciphertext, small_prime, big_prime, exponent)


def IntSqrt(n):
    low = 1
    high = n
    iterations = 0
    while low < high and iterations < 5000:
        iterations += 1
        mid = (low + high + 1) // 2
        if mid * mid <= n:
            low = mid
        else:
            high = mid - 1
    return low


def DecipherSmallDiff(ciphertext, modulo, exponent):
    n_root = IntSqrt(modulo)
    for p in range(n_root - 5000, n_root + 1):
        if modulo % p == 0:
            return Decrypt(ciphertext, p, modulo // p, exponent)


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo,
                          second_exponent):
    common_prime = GCD(first_modulo, second_modulo)
    if common_prime > 1:
        q1 = first_modulo // common_prime
        q2 = second_modulo // common_prime
        return (Decrypt(first_ciphertext, common_prime, q1, first_exponent),
                Decrypt(second_ciphertext, common_prime, q2, second_exponent))
    return ("unknown message 1", "unknown message 2")


def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2)
  return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)


def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
    r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
    return ConvertToStr(IntSqrt(r))
