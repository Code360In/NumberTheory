# Bài 5: Number
log = print

# lưu vào nhiều vùng nhớ
a = 5
a = 6
print(a)

# giải phóng
del a
# print(a) - err

# ép kiểu
a = 5.5
b = int(a)
log(b)
log(a)
b = float(a)
log(b)
b = str(a)
log(b)

del a, b

# Toán tử
a = 5
b = 3
log(a, "+", b, "=", a+b)
log(a, "-", b, "=", a-b)
log(a, "*", b, "=", a*b)
log(a, "/", b, "=", a/b)
log(a, "%", b, "=", a%b)
