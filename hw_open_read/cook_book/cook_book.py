import os

FILENAME = os.path.join(os.getcwd() + '/recipes.txt')

def get_cook_dict(filename):
    cook_book = {}
    with open(FILENAME) as file_obj:
        for line in file_obj:
            key = line.strip()
            counter = int(file_obj.readline())
            tmp_list = []
            for item in range(counter):
                l = file_obj.readline().strip().split('|')
                tmp_list.append(dict(ingredient_name = l[0], quantity = int(l[1]), measure = l[2]))
                cook_book[key] = tmp_list
            file_obj.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_dict = {}
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            ingredient_name = cook_book[dish][i]['ingredient_name']
            quantity = cook_book[dish][i]['quantity']
            measure = cook_book[dish][i]['measure']
            if ingredient_name in shop_dict:
                shop_dict[ingredient_name]['quantity'] += quantity * person_count
            else:
                shop_dict[ingredient_name] = dict(quantity = quantity * person_count, measure = measure)
    for key in shop_dict.keys():
        print(f'{key}: {shop_dict[key]}')