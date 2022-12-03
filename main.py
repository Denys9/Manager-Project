import csv
try:
    while True:
        begin = input('Ви маєте акаунт?(y/n)')
        datafile = 'data.txt'
        if begin == 'n':
            print('Створення акаунту')
            loginc = input('Придумайте логін - ')
            passwordc = input('Придумайте пароль - ')
            csv_columns = [loginc, passwordc]
            try:
                with open(datafile, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
            except IOError:
                print('I/O error')
            continue
        if begin == 'y':
            print('Вхід в акаунт')
            loginw = input('Логін - ')
            passwordw = input('Пароль - ')
            with open(datafile, 'r') as csvfile:
                write = csvfile.readline().split(',')
            print(bool(loginw==write[0]))
            product = input('Введіть назву продукту - ')
            category = input('Введіть назву категорії - ')
            amount = input('Введіть кількість - ')
            description = input('Введіть опис - ')
            price = input('Введіть ціну товара - ')
            store = input('Введіть магазин купівлі - ')
            csv_columns1 = ['Продукт', 'Категорія', 'Кількість', 'Опис', 'Ціна', 'Магазин']
            dict_data = [
                {'Продукт': product, 'Категорія': category, 'Кількість': amount,
                 'Опис': description, 'Ціна': price, 'Магазин': store}
            ]
            csv_file = "manager.csv"
            try:
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns1)
                    writer.writeheader()
                    for data in dict_data:
                        writer.writerow(data)
            except IOError:
                print('I/O error')
        else:
            print('Перевірте ввод символів!')
except Exception as e:
    print(e)
