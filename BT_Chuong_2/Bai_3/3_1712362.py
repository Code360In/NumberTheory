from sys import argv
script, input = argv


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
