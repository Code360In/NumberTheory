log = print

# original karatsuba algorithm


def karat(x, y):
    if(len(str(x)) == 1 or len(str(y)) == 1):
        return x*y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m//2
        a = x//(10**m2)
        b = x % (10**m2)
        c = y//(10**m2)
        d = y % (10**m2)
        z0 = karat(b, d)
        z1 = karat(a+b, c+d)
        z2 = karat(a, c)
        return z2*(10**(2*m2))+(z1-z2-z0)*(10**m2)+z0


# my custom
def myKaratsuba(x, y):
    if(len(str(x)) == 1 or len(str(y)) == 1):
        return x*y
    else:
        max_length = max(len(str(x)), len(str(y)))
        m = max_length//2
        a = x//(10**m)
        b = x % (10**m)
        c = y//(10**m)
        d = y % (10**m)
        z0 = myKaratsuba(b, d)
        z2 = myKaratsuba(a, c)
        z1 = myKaratsuba(a+b, c+d)-z0-z2
        return z2*(10**(2*m))+z1*(10**m)+z0

# custom high level - could use for any base
# input: x and y - big number, base is base of them
# output: the result of x*y in base = base


def superKaratsuba(x, y, base):
    if(len(str(x)) == 1 or len(str(y)) == 1):
        return x*y
    else:
        max_length = max(len(str(x)), len(str(y)))
        m = max_length//2
        if(base == 2):
            a = int(bin(x//(base**m)))
            b = int(bin(x % (base**m)))
            c = int(bin(y//(base**m)))
            d = int(bin(y % (base**m)))
            z0 = superKaratsuba(a, c, base)
            z2 = superKaratsuba(b, d, base)
            z1 = superKaratsuba(a+b, c+d, base)-z0-z2
            return bin(z2*(base**(2*m))+z1*(base**(m))+z0)


log(karat(123, 321))
log(myKaratsuba(1234, 4321))
# log(superKaratsuba(10, 11, 2))
