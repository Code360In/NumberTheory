# Bài 6 - List
log = print

gioHang = ["Giày", 22, "Áo", 11, "Giá", 200]
log(gioHang)
log(gioHang[0], gioHang[gioHang.__len__()-1])

# index - list[start:end]
log(gioHang[0:gioHang.__len__()-1])

# update
gioHang[gioHang.__len__()-1] = 30000
log(gioHang)

# delete
del gioHang[gioHang.__len__()-1]
log(gioHang)

# list in list
option = [22, 2, 1998]
myList = ['Không cu', 'Thông tin', option]
log(myList)

# h - trong không
log(myList[0][1])

# 1998 - option
log(myList[2][2])
