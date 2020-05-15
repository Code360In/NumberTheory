# Bài 9: Toán tử

log = print

# Toán tử số học
a = 2
b = 3

log(a, '+', b, '=', a+b)
log(a, '-', b, '=', a-b)
log(a, '*', b, '=', a*b)
log(a, '/', b, '=', a/b)
log(a, '%', b, '=', a % b)

# a^b  - a**b
log(a, '^', b, '=', a**b)

# Toán tử quan hệ
log(a, "==", b, "? =>", a == b)
log(a, "!=", b, "? =>", a != b)
log(a, "<", b, "? =>", a < b)
log(a, ">", b, "? =>", a > b)
log(a, ">=", b, "? =>", a >= b)
log(a, "<=", b, "? =>", a <= b)

# Toán tử gán
c = a
log(c)
c += a
log(c)
c -= a
log(c)

# Toán tử logic
c = (a > b and b > a)
log(c)
c = a > b or b > a
log(c)

c = not a > b
log(c)

c = (a > b)
log(c)

# Toán tử biwter
c = a & b
log("a = ", a)
log("b = ", b)
log(c)

# Toán Tử khai thác.
arr = [1, 2, 3, 4, 5]
b = 4
c = 123
check = b in arr
check2 = c not in arr
log(check)
log(check2)
