with open('database.csv') as data:
    data_list = data.read().splitlines()
    data_list = [item.split("ß¤") for item in data_list]
    next_id = str(data_list[-1][0]) + 1
    print(next_id)


