# Bài 8: Dictionary

# {key1: value1, key2: value2,..., keyN: valueN}

# Các phần tử đều phải có key.
# Và Key chỉ có thể là số hoặc chuỗi.
# Key phải là duy nhất, nếu không nó sẽ nhận giá trị của phần tử có key được xuất hiện cuối cùng.
# Key khi đã được khai báo thì không thể đổi được tên.
# Key có phân biệt hoa thường.

log = print

person = {
    'name': 'Ca Heo',
    'age': 3,
    'male': True,
    'status': "single"
}

log(person)
log(person["name"])
log(person['age'])

# update
person['age'] = 5
log(person)

# delete
del person['status']
log(person)

# del all key & val
person.clear()
log(person)

# del all dictionary
del person
# log(person)  # undefine

# dic in dic
person = {
    'name': "ca heo",
    'option': {
        'age': 3,
        'male': False,
    }
}

log(person)
log(person['name'])
log(person['option']['male'])
