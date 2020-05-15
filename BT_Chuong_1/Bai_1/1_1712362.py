# from sys import argv
# script, input = argv


log = print


# ham chuyen co so


# def convert_number_nab(n, a, b):
#     if(b == 10):


# log(oct(1001))
# log(bin(1001))
# log(int("1001", base=2))
# log(int("FAB", base=16))

# log(int("123", base=4, base=5))
# int()

# ham chuyen he 2 sang he 10


def convert_base_nab(n, a, b):
    log("n = ", n)
    log("a = ", a)
    log("b = ", b)
    convert = int("%s" % (n), base=a)
    log("Result = ", convert)


# convert_base_nab(123, 4, 5)

# doc file
fr = open('input.txt', 'r')
lines = [line[:-1].split() for line in fr.readlines()]
fr.close()

# log(lines)


# ghi file
# fw = open('1_1712362.txt', 'wb')
# for line in lines:
#     log(line)
#     # fw.write(line)
