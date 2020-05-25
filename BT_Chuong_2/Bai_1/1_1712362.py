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
    fr = open(file)
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


arrNumber = tachFileThanhMangSoNguyen(argv[1])


log(arrNumber)


# test thu ghi file
def write_file_result():
    return 0
