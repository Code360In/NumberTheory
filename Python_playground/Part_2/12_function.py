# Bài 12: Function
log = print


def say():
    log("Hello function ")


say()


def sum(a, b):
    return log(a, "+", b, "=", a+b)


def logSomething(stuff):
    log(stuff)


arr = [1, 2, 3]
logSomething(arr)


# global var
a = 5


def change__global_val(val):
    global a
    a += val
    log(a)


change__global_val(55)
log(a)


# REST parameter javascript
def sum__level__master(*argv):
    tmp = 0
    for i in argv:
        tmp += i
    return tmp


result = sum__level__master(1, 2, 3, 4, 5)
log(result)
