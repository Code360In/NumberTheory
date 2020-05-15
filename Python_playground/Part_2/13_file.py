# Bài 13: Thao tác File
log = print

"""
# input
log("Hello")
age = input("How old are you ? ")
log("Age: "+age)

"""

# open file
# open('filePath','mode',buffer)
# mode
# r	Chế độ chỉ được phép đọc., rb	Chế độ chỉ được phép đọc nhưng cho định dạn nhị phân.
# r+	Chế độ này cho phép đọc và ghi file, con trỏ nó sẽ nằm ở đầu file.
# rb+	Chế độ này cho phép đọc và ghi file ở dạng nhị phân, con trỏ sẽ nằm ở đầu file.
# w	Chế độ ghi file, nếu như file không tồn tại thì nó sẽ tạo mới file và ghi nội dung,
# # còn nếu như file đã tồn tại nó sẽ ghi đè nội dung lên file cũ.

f = open('13_input.txt', 'r')
data = f.read()
f.close()
log(data)


# write file
f = open('13_input.txt', 'w')
write = f.write("22,33,44")
f.close()
