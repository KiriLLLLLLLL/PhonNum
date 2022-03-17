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

def type_get_data():
    return int(input('Что Вы хотите сделать?\n1. Записать новый контакт;\n2. Вывести контакт в одну строку;\n3. Вывести контакт в несколько строк\n'))



