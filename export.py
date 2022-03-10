import csv

def row_exp():
    with open("phonNum.csv", mode="r", encoding='utf-8') as f:
        file_reader = csv.DictReader(f)
        print(list(file_reader))


row_exp()