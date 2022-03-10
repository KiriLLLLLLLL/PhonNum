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


