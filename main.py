

import csv

product = input('Введіть назву продукту - ')
category = input('Введіть назву категорії - ')
amount = input('Введіть кількість - ')
description = input('Введіть опис - ')
price = input('Введіть ціну товара - ')
store = input('Введіть магазин купівлі - ')
csv_columns = ['Продукт', 'Категорія', 'Кількість', 'Опис', 'Ціна', 'Магазин']

dict_data = [
    {'Продукт': product, 'Категорія': category, 'Кількість': amount,
     'Опис': description, 'Ціна': price, 'Магазин': store}
]

csv_file = "manager.csv"

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")



# with open(FILENAME, "a", newline="") as file:
#    user = ["Sam", 31]
#    writer = csv.writer(file)
#    writer.writerow(user)

# import csv

# FILENAME = "users.csv"

# with open(FILENAME, "r", newline="") as file:
#    reader = csv.reader(file)
#    for row in reader:
#        for index in range(0, len(row)):
#            print(row[index], end='\t')
#        print()
