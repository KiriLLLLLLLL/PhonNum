import csv

def row_exp():
    with open("phonNum.csv", mode="r", encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        for row in file_reader:
            print(f'Имя: {row["first_name"]}, Фамилия: {row["last_name"]}, Номер: {row["phone_num"]}, Описание: {row["description"]}')

def rows_exp():
    with open("phonNum2.csv", mode="r", encoding='utf-8') as f:
        file_reader = csv.reader(f)
        for row in file_reader:
            print(row)

