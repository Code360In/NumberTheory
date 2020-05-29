from sys import argv
script, input = argv

log = print

# log("Hello world!")


# function convert string arr from file to num arr
def convert_str_arr_to_num_arr(str_arr):
    lenght = len(str_arr)
    for i in range(0, lenght):
        str_arr[i] = int(str_arr[i])
    return str_arr


# str_arr_test = ["1 2 3 4", "1 2 3 4", "1 2 3 4"]
# test = str_arr_test[0].split(" ")
# log(test)
# temp = convert_str_arr_to_num_arr(test)
# log(temp)


# func: lay data tu file - chuyen thanh mang
# input: ten file
# output: mang data
def get_data_from_file(file_name):
    # log(file_name)
    fr = open(file_name, 'r')
    lines = fr.readlines()
    # log(lines)

    # remove \n from arr string
    arr_origin = []
    for line in lines:
        line_striped = line.strip()
        format(arr_origin.append(line_striped))
    # log(arr_origin)

    # split str_arr to separate arr string
    length_of_arr_origin = arr_origin.__len__()
    arr_splited = []
    for i in range(0, length_of_arr_origin):
        arr_splited.append(arr_origin[i].split(" "))
    # log(arr_splited)

    # convert to num arr
    result = []
    lenght_of_arr_splited = arr_splited.__len__()
    for i in range(0, lenght_of_arr_splited):
        result.append(convert_str_arr_to_num_arr(arr_splited[i]))
    fr.close()
    return result


# log(argv[1]) - input txt
data = get_data_from_file(argv[1])
log(data)


# func ghi kech qua vao file
# input: ten file, data ghi vao file
# output: file kech qua, thong bao ghi thanh cong tren console


def write_result_to_file(file_name, data):
    # log("Hello write file")
    fw = open(file_name, 'w')
    len_data = data.__len__()
    for i in range(0, len_data):
        len_sepated_rs = data[i].__len__()
        for j in range(0, len_sepated_rs):
            if(j == len_sepated_rs-1):
                fw.write(str(data[i][j]))
            else:
                fw.write(str(data[i][j])+" ")
        if(i == len_data - 1):
            fw.write("")
        else:
            fw.write("\n")
    log("Write file success!")
    fw.close()


write_result_to_file('2_1712362.txt', data)

# func gcd - tien de euclid
# input: 2 so nguyen a,b
# output: UCLN cua a,b


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


# func kt so ng to
# input: n - so nguyen bat ky
# output: True or False


def is_primes(n):
    if(n < 2):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True

# func kt stn cung nhau
# input: 2 so nguyen
# output: True or false


def is_coprimes(a, b):
    ab_gcd = gcd(a, b)
    if(ab_gcd == 1):
        return True
    else:
        return False


log(is_coprimes(6, 25))


# func phi euler
# input: so nguyen n
# ouput: tong so cac so nto cung nhau voi n hoac -1 neu khong ton tai
def phi_euler(n):
    arr_coprimes_with_n = []
    for i in range(1, n+1):
        #log(i, n)
        if(is_coprimes(i, n) == True):

            arr_coprimes_with_n.append(i)
    len = arr_coprimes_with_n.__len__()
    log(arr_coprimes_with_n)
    if(len >= 1):
        return len
    else:
        return -1


log(phi_euler(10))
