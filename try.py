with open('database.csv') as data:
    data_list = data.read().splitlines()
    data_list = [item.split("ß¤") for item in data_list]
    for i in range(len(data_list)):
        data_list[i][0] = i

with open('database.csv', 'w') as file:
    for item in data_list:
        print(item)
        # asd = "ß¤".join(str(item))
        file.write("".join(str(item)) + "\n")