with open('database.csv') as data:
    data_list = data.read().splitlines()
    data_list = [item.split(',') for item in data_list]
    q = []
    for item in data_list:
        if item[1] == "qwe":
            q.append(["kutya", "macska"])
        else:
            q.append(item)
    print(data_list)
    print(q)
