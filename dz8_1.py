"""
Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
    записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл":
"""

file_n = 'input.txt'
file_out = 'output.txt'


def read_data_student(file):
    with open(file, 'r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        student_data = []
        for student in data:
            temp_dict = dict()
            temp_dict['name'] = student.split()[0]
            temp_dict['surname'] = student.split()[1]
            temp_dict['gpa'] = sum(map(int, student.split()[2:])) / len(student.split()[2:])
            student_data.append(temp_dict)
    return student_data


def gpa_less_show(data, gpa=5):
    for stud in data:
        if stud['gpa'] < gpa:
            print(stud['name'], stud['surname'])


def gpa_class(data):
    return float('{0:.2f}'.format(sum(map(lambda i: i['gpa'], student_data)) / len(data)))


def data_to_out_file(data, file_out):
    with open(file_out, 'w', encoding='utf-8') as file_object:
        for student in data:
            temp_stud = ''
            temp_stud += str(student['surname'] + ' ' + student['name'][0] + '. ').ljust(18) + \
                         str(float('{0:.2f}'.format(student['gpa']))) + '\n'
            file_object.write(temp_stud)


student_data = read_data_student(file_n)
# for now in student_data:
#     print(now)
print('Студенты, со средним балом меньше 5:')
gpa_less_show(student_data)
print('Средний бал по классу -', gpa_class(student_data))
data_to_out_file(student_data, file_out)
