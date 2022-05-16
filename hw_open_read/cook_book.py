import os
from pprint import pprint

FILENAME = os.path.join(os.getcwd() + '/hw_open_read/recipes.txt')


def get_cook_dict(filename):
    cook_book = {}
    with open(FILENAME) as file_obj:
        for line in file_obj:
            key = line.strip()
            counter = int(file_obj.readline())
            tmp_list = []
            for item in range(counter):
                l = file_obj.readline().strip().split('|')
                tmp_list.append(dict(ingredient_name = l[0], quantity = l[1], measure = l[2]))
                cook_book[key] = tmp_list
            file_obj.readline()
    return cook_book



def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_dict = {}
    print(person_count)
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            if cook_book[dish][i]['ingredient_name'] in shop_dict:
                print(cook_book[dish][i]['ingredient_name'])
                print(type(cook_book[dish][i]['quantity']))
                tmp_quantity = int(cook_book[dish][i]['quantity'])
                # поамдоры не считаются!!!
                
            else:
                shop_dict[cook_book[dish][i]['ingredient_name']] = dict(quantity = int(cook_book[dish][i]['quantity']) * person_count, measure = cook_book[dish][i]['measure'])
    pprint(shop_dict)
    
    
    
dishes = ['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос']
get_shop_list_by_dishes(dishes, 5, get_cook_dict(FILENAME))