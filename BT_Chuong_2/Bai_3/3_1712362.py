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

# func write data after handle to file output
# input: file name, data to write
# output: new file writed


def write_result_to_file(file_name, data):
    fw = open(file_name, 'w')
    len_data = data.__len__()
    for i in range(0, len_data):
        len_separated_rs = data[i].__len__()
        for j in range(0, len_separated_rs):
            if(j == len_separated_rs-1):
                fw.write(str(data[i][j]))
            else:
                fw.write(str(data[i][j])+" ")
        if(i == len_data - 1):
            fw.write("")
        else:
            fw.write("\n")
    fw.close()


# write data after handle to output file
write_result_to_file('3_1712362.txt', data)
