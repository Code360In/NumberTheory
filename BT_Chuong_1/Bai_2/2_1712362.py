def phanTichSoNguyenMang(n):
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
# arr = phanTichSoNguyenMang(n)


def demPhanTuMang(mang):
    count = {}
    for i in mang:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    return count


# listResult = demPhanTuMang(arr)


# print(listResult)


def ketQua(listRs):
    result = ''
    for d in listRs.items():
        if d[1] > 1:
            result += str(d[0]) + '^' + str(d[1]) + '*'
        else:
            result += str(d[0]) + '*'
    return result[:-1]


# print(ketQua(listResult))


# doc file
input = open('input.txt', 'r')


lines = [line[:-1].split(' ') for line in input.readlines()]
input.close()
print(lines)
print("Line lengt", lines.__len__())
lengt = lines.__len__()

# ghi ket qua
output = open('result.txt', 'w')
for i in range(0, lengt):
print(i)
listNumbers = phanTichSoNguyenMang(lines.get(l))
listResult = demPhanTuMang(listNumbers)
output.write(ketQua(listResult) + '\n')
# result.append(temp)  # bo di cung duoc
