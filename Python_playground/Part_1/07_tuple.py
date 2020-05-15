# Bài 7: Tuple
log = print

# Like const
day = ('monday', 'tuesday', 'wednesday',
       'thursday', 'friday', 'saturday', 'sunday')
log(day)

# empty
a = ()
log(a)

# 1 value
b = (1,)
log(b)

# get list - tuple[start:end]
log(day[0:5])

# tuple[start:] - from start to end
log(day[0:])

# typle[:end] - from 0 to end
log(day[:3])

# cannot update - delete
del day
# log(day) # undefine

# tuple in tuple
day1 = ('monday', 'tuesday', 'wednesday')
day2 = (day1, 'thursday', 'saturday', 'sunday')
log(day1)
log(day2)

log(day2[0])
log(day2[0][1])
