# Bài 11: Loop
log = print

name = "ca heo"
count = 0
for i in name:
    log(i)
    count += 1
log(count)

# loop in loop
for i in range(0, 10):
    for j in range(i, 10):
        log(j, end=" ")
    log(" ")

r = 5

while (r != 1):
    r = r-1
    log(r)
    if(r == 2):
        break
log(r)
