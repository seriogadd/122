import os
import time
from pprint import pprint


# Задача №1
def create_cook_book(input_file_name):
    cook_book = {}

    try:

        with open(input_file_name, encoding='utf-8') as f:
            lst = [line.strip() for line in f]


        for i, c in enumerate(lst):
            if c.isdigit():

                cook_book[lst[i-1]] = []

                for slice in lst[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]

                    cook_book[lst[i-1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {input_file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'


# Задача №2
def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    ing_dict = {}

    for key in cooking_book.keys():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:

                    ing_name = dictionary['ingredient_name']

                    try:
                        ing_dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ing_dict[ing_name] = {'measure': dictionary['measure'],
                                              'quantity': dictionary['quantity'] * person_count}

    return ing_dict

def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        os.chdir('sorted')
        outout_file = "result.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(outout_file, 'w', encoding='utf-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Давай лучше без параметров')
    return

# Задача №1
print('Задача №1:\n')
pprint(create_cook_book('recipes.txt'))
print('\n' * 3)


# Задача №2
print('Задача №2:\n')
pprint(get_shop_list_by_dishes(['Фахитос', 'Запеченный картофель', 'Омлет'], create_cook_book('recipes.txt'), 2))

time.sleep(2)
print('Задание 3')
rewrite_file()