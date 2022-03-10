# Ввод данных

def input_data():
    dictionary = \
        {
            'first_name': str(input('Введите имя: ')),
            'last_name': str(input('Введите фамилию: ')),
            'phone_num': str(input('Введите номер: ')),
            'description': str(input('Введите описание: '))
        }
    return dictionary


def get_data(data, title):
    print(f'{title} : {data}')

