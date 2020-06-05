from sys import argv
script, input = argv

log = print


# problem handle
# -------------------------------------------------------------------


# func find maximun of a,b
# input: number a,b
# output: max of a,b


# def find_max_ab(a, b):
#     return a if a >= b else b

# func find BCNN, lowest common multiple
# input: number a,b
# output: lcm of them


# def lcm(a, b):
#     max_ab = find_max_ab(a, b)
#     mul_ab = abs(a*b)
#     lcm = 0
#     for i in range(max_ab, mul_ab+1):
#         if(i % a == 0 and i % b == 0):
#             lcm = i
#             break
#     return lcm


# log(lcm(1, 1))


# def gcd(a, b):
#     if(a == 0 and b == 0):
#         return -1
#     else:
#         lcm_ab = lcm(a, b)
#         mul_ab = abs(a*b)
#         gcd = mul_ab/lcm_ab
#     return int(gcd)

# a = b = 0 -------------------------------------- error

# func find UCLN, greates common divisor
# input: number a,b
# output: greates common divsor of them


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


# log(gcd(0, 0))


# func check number n is primes
# input: number n
# output: true or false


def is_primes(n):
    if(n < 2):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True

# log(is_primes(5))

# func dem phan tu trong mang
# input: mang
# output: dem cac phan tu trong mang, kieu dictionary


def dem_phan_tu_mang(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i] = 1
    return count


# log(dem_phan_tu_mang([2, 2, 2, 5, 5]))

# func convert n to array primes: phan tich thua so nguyen to cua n, va lay he so mu
# input: so nguyen n
# ouput: mang chua cac thua so nguyen to n


def thua_so_nguyen_to_va_mu_cua_no(n):
    i = 2
    array_tsnt = []

    while(n > 1):
        if(n % i == 0):
            n = int(n/i)
            array_tsnt.append(i)
        else:
            i += 1
    if(len(array_tsnt) == 0):
        array_tsnt.append(n)
    # dem cac thua so nguyen to trung nhau - dua ve kieu dictionary
    result = dem_phan_tu_mang(array_tsnt)
    # log(count)
    return result


# dic = thua_so_nguyen_to_va_mu_cua_no(100)
# log(dic.__len__())
# log(type(dic[2]))

# func tim thang du binh phuong mod p
# input: so nguyen to le p
# output: mang chua cac phan tu tdbp mod p


def thang_du_binh_phuong(p):
    if(p <= 2):
        return -1
    else:
        if(p % 2 == 0):
            return -1
        else:
            array_origin = []
            array_contain_surplus = []  # chua cac mod cua x^2 mod p
            result = []
            count_tdpb = (p-1)/2
            count_temp = 0

            for i in range(1, p):
                # log(i)
                array_origin.append(i)
                surplus = (i*i) % p
                array_contain_surplus.append(surplus)

            # luoc bo cac phan tu da ton tai trong mang
            for value in array_contain_surplus:
                if value in array_contain_surplus:
                    array_contain_surplus.remove(value)

            array_origin.sort()
            array_contain_surplus.sort()
            length_array_origin = array_origin.__len__()
            length_array_surplus = array_contain_surplus.__len__()
            # log(array_contain_surplus)
            # log(array_origin)
            for i in range(0, length_array_origin):
                for j in range(0, length_array_surplus):
                    if(array_contain_surplus[j] == array_origin[i]):
                        result.append(array_origin[i])
                        count_temp += 1
                if(count_temp == count_tdpb):
                    break
            return result


# arr_tdbp = thang_du_binh_phuong(17)
#log("Thang du: ", arr_tdbp)

# func legendre: ham tinh ky hieu legendre
# input: so nguyen a, so nguyen to le p
# ouput: 1 hoac -1 hoac 0 neu loi


def legendre_handle(a, p):
    if(a % p == 0):
        return 0
    elif (is_primes(p) == False):
        return 0
    elif(p % 2 == 0):
        return 0
    else:
        if(a < p):
            array_tdpb = thang_du_binh_phuong(p)
            len_array_tdpb = array_tdpb.__len__()
            if(array_tdpb[0] == -1):
                return 0
            else:
                for i in range(0, len_array_tdpb):
                    if(a == array_tdpb[i]):
                        return 1
                return -1
        else:
            temp_a = a
            a = temp_a % p
            array_tdpb = thang_du_binh_phuong(p)
            len_array_tdpb = array_tdpb.__len__()
            if(array_tdpb[0] == -1):
                return 0
            else:
                for i in range(0, len_array_tdpb):
                    if(a == array_tdpb[i]):
                        return 1
                return -1


# log("legen handle: ", legendre_handle(21, 17))
# for i in range(0, 21):
#     log(legendre_handle(i, 21))


# func jacobi: ham tinh ky hieu jacobi
# input: 2 so tu nhien a,n
# output: ket qua jacobi cua a n


def jacobi_handle(a, n):
    if(gcd(a, n) != 1):
        return 0
    elif(n <= 2):
        return 0
    elif(n % 2 == 0):
        return 0
    else:
        array_primes_factors = thua_so_nguyen_to_va_mu_cua_no(n)
        legendre_array = []
        for factor, value in array_primes_factors.items():
            legendre_array.append(pow(legendre_handle(a, factor), value))
            #log(factor, value)
        result = 1
        for legendre in legendre_array:
            result *= legendre

        #log("legen: ", legendre_array)
        return result


#log(jacobi_handle(21, 221))
# file handle
# -------------------------------------------------------------------


# func convert string array from file to number array
# input: array string
# ouput: array number


def convert_str_arr_to_num_arr(str_arr):
    length = len(str_arr)
    for i in range(0, length):
        str_arr[i] = int(str_arr[i])
    return str_arr

# func get data from file
# input: file name
# ouput: array contain data from file


def get_data_from_file(file_name):
    fr = open(file_name, 'r')
    lines = fr.readlines()

    arr_origin = []
    for line in lines:
        # beutify it, rm \n
        line_striped = line.strip()
        format(arr_origin.append(line_striped))
    # split string array to separate each one
    length_arr_origin = arr_origin.__len__()
    arr_splited = []
    for i in range(0, length_arr_origin):
        arr_splited.append(arr_origin[i].split(" "))

    result = []
    length_of_arr_splited = arr_splited.__len__()
    for i in range(0, length_of_arr_splited):
        result.append(convert_str_arr_to_num_arr(arr_splited[i]))
    fr.close()
    return result


# get data from file and prepare to handle in file output
data = get_data_from_file(argv[1])


# func process before write output file
# input: data
# output: result after processing
def processing(datas):
    jacobi_result = []
    for data in datas:
        jacobi_result.append(jacobi_handle(data[0], data[1]))
    return jacobi_result


# func write data after handle to file output
# input: file name, data to write
# output: new file writed


def write_result_to_file(file_name, data):
    fw = open(file_name, 'w')
    result = processing(data)
    count = 0
    for rs in result:
        if(count == result.__len__()-1):
            fw.write(str(rs))
        else:
            fw.write(str(rs)+"\n")
        count += 1
    fw.close()


# write data after handle to output file
write_result_to_file('3_1712362.txt', data)
