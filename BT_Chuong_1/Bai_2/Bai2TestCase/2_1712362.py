from sys import argv
script, input = argv

log = print

# chia de tri cai bai nay


def phanTichSoNguyenThanhMang(n):
    i = 2
    listNumbers = []
    count = 0
    while (n > 1):
        if (n % i == 0):
            n = int(n / i)
            count = count + 1
            listNumbers.append(i)
        else:
            i = i + 1

    if (len(listNumbers) == 0):
        listNumbers.append(n)

    return listNumbers


# n = 120
# arr = phanTichSoNguyenThanhMang(n) # [2,2,2,3,5]
# log(arr)


def demPhanTuMang(mang):
    count = {}
    for i in mang:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    return count


# listResult = demPhanTuMang(arr) # {2:3,3:1,5:1}


# print(listResult)


def ketQua(listRs):
    result = ''
    for d in listRs.items():
        # log(d)
        if d[1] > 1:
            result += str(d[0]) + '^' + str(d[1]) + 'x'
        else:
            result += str(d[0]) + 'x'
    return result[:-1]


# print(ketQua(listResult)) - 2^3*3*5


# doc file
fr = open('input.txt', 'r')
lines = [line[:-1].split(' ') for line in fr.readlines()]
fr.close()
# log(lines)
# log(data)

# ghi file
fw = open('2_1712362.txt', 'w')
for l in lines:
    # log(l[0])
    arr = phanTichSoNguyenThanhMang(int(l[0]))
    # log(arr)
    listRs = demPhanTuMang(arr)
    # log("List result:", listRs)
    result = ketQua(listRs)
    # log("Result:", result)

    fw.write(result+"\n")


fw.close()
