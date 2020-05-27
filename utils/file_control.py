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


# doc file
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


def write_result_to_file(file_name, data):
    #log("Hello write file")
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
