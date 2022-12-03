import csv
accountfile = 'account.csv'
login = input('enter your login->')
password = input('enter your password->')
path = input('enter path of file->')

data = [
    {'login': login},
    {'password': password},
    {'path': path}
]
columns = ['login', 'password', 'path']
# data_str = f'login: {login},password: {password},path: {path}'
# data_str = data_str.split(',')
# for key in data_str:
#     print(key, end='\n')
with open(accountfile, 'w', newline='') as csvfile:
    columns = ["login", "password", "path"]
    writer = csv.DictWriter(csvfile, delimiter =';', fieldnames=columns)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

# import csv
# csv_columns = ['No','Name','Country']
# dict_data = [
# {'No': 1, 'Name': 'Alex', 'Country': 'India'},
# {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
# {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
# {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
# {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
# ]
# csv_file = "Names.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, delimiter = ';', fieldnames=csv_columns)
#         writer.writeheader()
#         for data in dict_data:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")