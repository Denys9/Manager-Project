import csv
login = input("Введіть логін - ")
password = input("Введіть пароль - ")
product = input('Введіть назву продукту - ')
category = input('Введіть назву категорії - ')
amount = input('Введіть кількість - ')
csv_columns = ['Продукт', 'Категорія', 'Кількість']

dict_data = [
    {'Продукт': product, 'Категорія': category, 'Кількість': amount}
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
    csv_columns = ['login', 'password']
    dict_data = [
        {'login': login, 'password': password}
    ]
    csv_file = "user data.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
