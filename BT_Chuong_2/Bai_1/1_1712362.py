from sys import argv
script, input = argv

log = print


# arrStrOrigin = ["1 2 3 4", "2 3 4 5"]
# arrStrSplit = arrStrOrigin[0].split(" ")

# log(arrNum)


# convert str arr to num arr function
def converStrArr_to_numArr(strArr):
    for i in range(0, len(strArr)):
        strArr[i] = int(strArr[i])
    return (strArr)


# arrNum = converStrArr_to_numArr(arrStrSplit)
# log(arrNum)


# tach cac dong trong file thanh mang so nguyen function
def tachFileThanhMangSoNguyen(file):
    fr = open(file, 'r')
    lines = fr.readlines()
    fr.close()
    arrStrOrigin = []
    # lay mang chuoi trong file, loai bo \n bang format, strip
    for line in lines:
        format(arrStrOrigin.append(line.strip()))

    # log(arrStrOrigin)

    arrStrSplited = []
    # tach mang chuoi co dau cach thanh mang chuoi khong dau cach
    for i in range(0, arrStrOrigin.__len__()):
        arrStrSplited.append(arrStrOrigin[i].split(" "))

    # log(arrStrSplited)

    # convert arr string sang arr number
    arrNumber = []
    for i in range(0, arrStrSplited.__len__()):
        arrNumber.append(converStrArr_to_numArr(arrStrSplited[i]))
    return arrNumber
    # log(arrNumber)


# 1 mean input.txt
arr_number_from_file = tachFileThanhMangSoNguyen(argv[1])


# log(arr_number_from_file)
# ucln


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

# ham tim a kha nghich trong Zn


def a_khanghich_n(a, n):
    d = gcd(a, n)
    if(d != 1):
        return -1
    else:
        xa = 1
        xn = 0
        n_origin = n
        while (n != 0):
            q = a // n
            xr = xa - q*xn
            xa = xn
            xn = xr
            r = a % n
            a = n
            n = r
        result = xa
        if(result < 0):
            result = result - n_origin*(result//n_origin)
    return result


# log(a_khanghich_n(2, 4))

# ham giai pt ax=b (z n)
def giai_pt_modulo(a, b,  n):
    d = gcd(a, n)
    x = []
    if(b % d != 0):
        return -1
    else:
        a1 = a//d
        b1 = b//d
        n1 = n//d
        a1_kn = a_khanghich_n(a1, n1)
        if(a1_kn == -1):
            return -1
        else:
            for i in range(0, d):
                # log(i)
                x.append(a1_kn*b1+i*n1)
            for i in range(0, d):
                if(x[i] > n):
                    x[i] = x[i]-n*(x[i]//n)
    x.sort()
    return x


# x = giai_pt_modulo(9, 6, 15)
# log(x)

# module equation solve

# ax+b = c mod n <=> ax+b=c (Z n)
# ax = c - b = k (z n)
# if k = 0 -> x
# if k < 0
# + tim  b1 = k - n*(k//n)
# + k = b1
# + ax = b1 (z n)
#  -> giai pt ax = b1 zn
# if k > 0
# giai pt ax = k zn


# ham giai pt modulo ax + b = c (mod n)

def solve_origin_equation_modulo(a, b, c, n):
    k = c - b
   # log(" k = ", k)
    rs_arr = []
    if(k == 0):
        rs_arr.append([str('x')])
    elif(k > 0):
        rs_temp = giai_pt_modulo(a, k, n)
        if(rs_temp == -1):
            rs_arr.append([str('x')])
        else:
            rs_arr.append(rs_temp)
    else:
        b1 = k-n*(k//n)
        rs_temp = giai_pt_modulo(a, b1, n)
        if(rs_temp == -1):
            rs_arr.append([str('x')])
        else:
            rs_arr.append(rs_temp)
    return rs_arr


# rs_arr = solve_origin_equation_modulo(15, -36, 29, 85)
# log(rs_arr)

# test thu ghi file


def write_file_result(arr_number_from_file):
    fw = open('1_1712362.txt', 'w')

    # log(arr_number_from_file)
    result_write = []
    for i in arr_number_from_file:
        # log(i)
        temp = solve_origin_equation_modulo(i[0], i[1], i[2], i[3])
        result_write.append(temp)
    # log(result_write)
    # log(result_write[0][0][0])
    length_from_file = result_write.__len__()
    for i in range(0, length_from_file):
        length_child = result_write[i][0].__len__()
        # log("len child ", i, " = ", length_child_1)
        # log(result_write[i])
        length_separate_result = result_write[i][0].__len__()
        for j in range(0, length_child):
            # log(j)
            # log(result_write[i][0][j])

            # spacing bugs - fixed
            if(j == length_separate_result-1):
                fw.write(str(result_write[i][0][j]))
            else:

                fw.write(str(result_write[i][0][j])+" ")
        # drop down the line bugs
        if(i == length_from_file - 1):
            fw.write("")
        else:
            fw.write("\n")

    fw.close()
    log("Write file success!")


write_file_result(arr_number_from_file)
