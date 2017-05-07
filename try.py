with open('database.csv') as data:
    data_list = data.read().splitlines()
    data_list = [item.split("ß¤") for item in data_list]
    data_list = sorted(data_list, key=lambda x: float(x[5]))
    for item in data_list:
        print(item)