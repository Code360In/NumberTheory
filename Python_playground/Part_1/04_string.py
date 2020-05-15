# Bài 4: String
log = print

# ky tu " "
log("Ky tu nay \"Dac biet\" ")
log("Lam lai \"Dac biet \"", end=" - ")
log("\"dac biet\"")

# /n /t
log("Câu này sẽ xuống dòng\n")
log("Câu này sẽ tab \t - tab ở đây")

# \a
log("\a chuông cảnh báo ?")
log("\a")

# \b xóa bỏ khoảng trắng trước nó
log("Khoảng trắng \bxóa được k ?")

# bining %s - chuỗi, %i, %d - int, %x - hệ 16 in thường, %X - hệ 16 in hoa, %0 - hệ 8 ,%e - số mũ, %f - float
guy = "Không Cu"
bindit = "Chào bạn %s" % (guy)
log(bindit)

a = 95
binda = "a = %x" % (a)
log(binda)

# index string
stringName = "Không cu,  có, cu không ?"
log(stringName[2])
log(stringName[stringName.__len__()-1])
log(stringName.split())
log(stringName.splitlines())

# lấy cu không ? string[a:b]
splitLinesStringName = stringName.splitlines()
indexToCut = splitLinesStringName[splitLinesStringName.__len__()-1]
log(splitLinesStringName)
log(indexToCut)

splitStrName = stringName.split()
log(splitStrName)
conCatStuff = splitStrName[splitStrName.__len__()-3:splitStrName.__len__()-1]
log(conCatStuff)
log(str(conCatStuff))

# nối mảng chuỗi thành chuỗi
string = ""
arrString = ["Không cu", " có ", "cu không"]
log(arrString)
log(string)

for i in arrString:
    log("i Lúc đầu: ", i)
    string += str(i)
    log("i lúc sau: ", i)

log(string)
