from sys import argv
script, input = argv


log = print

# log(int("1001", base=2))
# func chuyen co so n sang 10


def convert_basen_to_base10(value, base_a):
    str_val = str(value)
    base_10 = int(str_val, base=base_a)
    return base_10


# base_10 = convert_basen_to_base10(6324146781641642652, 4)
# log(base_10)


# func chuyen co so 10 sang b
def convert_base10_to_baseb(base_10, base_b):
    if (base_10 < 0 or base_b < 2 or base_b > 16):
        return ""
    sb = ""
    m = 0
    remainder = base_10

    while (remainder > 0):
        if (base_b > 10):
            m = remainder % base_b
            if (m >= 10):
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % base_b)
        remainder = int(remainder / base_b)
    return "".join(reversed(sb))


base_10 = (convert_basen_to_base10(6324146781641642652, 16))
base_b = convert_base10_to_baseb(base_10, 3)
# log(base_b)


def divide_data(n, base_a, base_b):
    base_10 = 0
    base_k = 0
    result = ""
    if(base_b == 10):
        base_10 = convert_basen_to_base10(n, base_a)
        result += base_10
    else:
        base_10 = convert_basen_to_base10(n, base_a)
        # log(base_10)
        base_k = convert_base10_to_baseb(base_10, base_b)
        # log(base_k)
        result += base_k
    return result


# data = divide_data(1234, 5, 6)
# log(data)


# chen them 1 hang
fw = open('input.txt', 'r')
# log(fw.readlines())
log(fw.__sizeof__())
# for l in lines:
#     log(l)
#     result=divide_data(str(l[0]), int(l[1]), int(l[2]))
#     fw.write(str(result)+"\n")


# doc file
# fr = open('input.txt', 'r')
# lines = [line[:-1].split(" ") for line in fr.readlines()]
# fr.close()
# log(lines)


# ghi file
# fw = open('1_1712362.txt', 'w')
# for l in lines:
#     log(l)
#     result = divide_data(str(l[0]), int(l[1]), int(l[2]))
#     fw.write(str(result)+"\n")

# fw.write(lines)
# fw.close()
