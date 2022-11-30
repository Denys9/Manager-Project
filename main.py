import csv
login = input("Введіть логін - ")
password = input("Введіть пароль - ")
product = input('Введіть назву продукту - ')
category = input('Введіть назву категорії - ')
amount = input('Введіть кількість - ')
csv_columns = ['Продукт', 'Категорія', 'Кількість']
csv_columns1 = ['login', 'password']
dict_data = [
    {'Продукт': product, 'Категорія': category, 'Кількість': amount}
]
dict_data1 = [
    {'login': login, 'password': password}
]
csv_file = "manager.csv"
csv_file = "user data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns1)
            writer.writeheader()
            for data in dict_data1:
                writer.writerow(data)
    except IOError:
        print("I/O error")
