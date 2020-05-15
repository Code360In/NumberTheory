from sys import argv
script, input = argv
log = print


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


input = open('input.txt', 'r')
lines = [line[:-1].split(' ') for line in input.readlines()]
input.close()
print(lines)

# testFile = open('test.txt', 'w')
# result = []
# for l in lines:
#     log(l)
#     temp = gcd(int(l[0]), int(l[1]))
#     log(temp)
#     testFile.write(str(temp)+"\n")


output = open('3_1712362.txt', 'w')
# result = []
for l in lines:
    temp = gcd(int(l[0]), int(l[1]))
    output.write(str(temp) + '\n')
    # result.append(temp)
output.close()

# print(result)
