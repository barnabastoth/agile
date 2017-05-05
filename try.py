with open('database.csv') as data:
    data_list = data.read().splitlines()
    data_list = [item.split('ß¤') for item in data_list]
    id = 1
    for item in data_list:
        if int(item[0]) == id:
            data_list.remove(item)
    for item in data_list:
        item[0] = data_list.index(item)
    print(data_list)