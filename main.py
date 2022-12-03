# import csv
# accountfile = 'account.csv'
# login = input('enter your login->')
# password = input('enter your password->')
# path = input('enter path of file->')
#
# data = [
#     {'login': login},
#     {'password': password},
#     {'path': path}
# ]
# columns = ['login', 'password', 'path']
# # data_str = f'login: {login},password: {password},path: {path}'
# # data_str = data_str.split(',')
# # for key in data_str:
# #     print(key, end='\n')
# with open(accountfile, 'w', newline='') as csvfile:
#     columns = ["login", "password", "path"]
#     writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=columns)
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


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
                with open(datafile, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
            except IOError:
                print('I/P error')
except Exception as e:
    print(e)