# Bài 10: if-else
log = print

if 1 > 2:
    log("code if")
else:
    log("Code else")


point = 7
if(point > 0 and point <= 10):
    if(point >= 5):
        log("Qua mon")
    else:
        log("Hoc lai")
else:
    log("Diem khong hop kle!")

# if elif else
arr = ['Ca map', 'ca heo', 'ca voi']

if(arr.__contains__('ca map')):
    log("Ca map")
elif(arr.__contains__('ca heo')):
    log("Ca heo")
else:
    log("Ca voi")
