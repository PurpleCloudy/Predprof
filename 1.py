'''
функция читает csv файл и дает нам данные в виде списка
path - путь к файлу csv
'''
def readfile(path):
    with open(path) as file:
        f = [c.split(';') for c in file.readlines()][1::]
        '''
        достать из файла все строки и разложить их в виде списков
        '''
        return f
readfile('/home/student/Загрузки/products.csv')

'''
функция принимает список товаров и считает полную стоимость категории закуски
умножая количество на цену
'''

def total_cost(lister):
    [c.append(float(c[3])*float(c[4])) for c in lister]
    writeln = [f'{c[1]}, {c[2]}, {c[3]}, {c[4]}, {c[5]}, {c[0]};' for c in lister]
    with open('/home/student/Загрузки/products_new.csv', 'w+') as file:
        for i in writeln:
            file.write(i)
    costs_zak = sum([float(c[3])*float(c[4]) if c[0] == 'Закуски' else 0 for c in lister])
    return lister, costs_zak

print(total_cost(readfile('/home/student/Загрузки/products.csv')))