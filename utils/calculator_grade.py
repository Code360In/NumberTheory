from sys import argv
script, script, input = argv
log = print


# func convert string array from file to number array
# input: array string
# ouput: array number


def convert_str_arr_to_num_arr(str_arr):
    length = len(str_arr)
    for i in range(0, length):
        if(str_arr[i] != 'x'):
            str_arr[i] = int(str_arr[i])
    return str_arr

# log(convert_str_arr_to_num_arr(["1 2 3 4"]))


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
        arr_splited.append(arr_origin[i].split(","))

    result = []
    length_of_arr_splited = arr_splited.__len__()
    for i in range(0, length_of_arr_splited):
        result.append(convert_str_arr_to_num_arr(arr_splited[i]))
    fr.close()
    return result

# func process before write output file
# input: data
# output: result after processing


def processing(datas_input, datas_check):
    result = []
    # log(datas_input)
    # log(datas_check)

    for data in datas_input:
        result.append(1) if data in data_check else result.append(-1)
    return result


# get data from file and prepare to handle in file output
data_input = get_data_from_file(argv[1])
data_check = get_data_from_file(argv[2])

# func write data after handle to file output
# input: file name, data to write
# output: new file writed


def write_result_to_file(file_name):
    fw = open(file_name, 'w')
    result = processing(data_input, data_check)

    grade = 10
    for rs in result:
        if (rs != 1):
            grade -= 1
    fw.write(str(grade))
    fw.close()


write_result_to_file("output.txt")
