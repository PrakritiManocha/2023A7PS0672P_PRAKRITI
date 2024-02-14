def lists_to_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result


keys = []
values = []
n = int(input("Enter the number of elements in the lists: "))

for i in range(n):
    m=input("Enter element of keys list:")
    keys.append(m)

for i in range(n):
    m=input("Enter element of values list:")
    values.append(m)

result = lists_to_dict(keys, values)
print(result)
