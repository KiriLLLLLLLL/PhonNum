import csv
import os



def row_imp(dictionary):
    with open("phonNum.csv", mode="a", encoding='utf-8') as f:
        file_is_empty = os.stat('phonNum.csv').st_size == 0
        fieldnames = ['first_name', 'last_name', 'phone_num', 'description']
        file_writer = csv.DictWriter(f, fieldnames=fieldnames)
        if file_is_empty:
            file_writer.writeheader()
        file_writer.writerow(dictionary)

def rows_imp(dictionary):
    with open("phonNum2.csv", mode="a", newline='', encoding='utf-8') as f:
        file_writer = csv.writer(f, delimiter='-')
        for key, value in dictionary.items():
            list1 = [key, value]
            file_writer.writerow(list1)
        file_writer.writerow([])

def import_data_controller(data):
    row_imp(data)
    rows_imp(data)


