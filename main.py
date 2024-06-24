import requests

def get_students():
    i = 0
    response = requests.get('http://127.0.0.1/students')
    all = response.json()
    print('Все студенты: ')
    while i < len(all):
        print(f'{i+1}-й: {all[i]} \n')
        i += 1
    return all

def new_student():
    data_ = params()
    response = requests.post('http://127.0.0.1/students', json=data_)
    if response:
        return ({"message": "Студент успешно добавлен", "student": data_}), 201
    # get_one_student(id_)

def update_students():
    print('\nОбновление информации: ')
    id_ = id_make()
    data_ = params()
    url = 'http://127.0.0.1/students/' + str(id_)
    response = requests.put(url, json=data_)
    if response:
        return ({"message": "Данные студента успешно обновлены", "student": data_}), 201

def delete_stud():
    id_ = id_make()
    url = 'http://127.0.0.1/students/' + str(id_)
    response = requests.delete(url)
    if response:
        return ({'message': 'Студент успешно удален'}), 201





# Выполнение #

get_students()
new_student()
update_students()
delete_stud()
