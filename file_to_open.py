from pprint import pprint


def cb_make(dish, ingredients):
    products = []
    for ingredient in ingredients:
        product = {}
        product['ingredient_name'] = ingredient[0]
        product['quantity'] = ingredient[1]
        product['measure'] = ingredient[2]
        products.append(product)
    cook_book.setdefault(dish, products)
    ingredients.clear()


def get_shop_list_by_dishes(dishes, person_count):
    ingr_temp_list = []
    for dish in cook_book:
        if dish in dishes:
            ingr_temp_list += cook_book[dish]

    ingr_temp_dict = {}
    for ingr in ingr_temp_list:
        if ingr['ingredient_name'] in ingr_temp_dict:
            ingr_temp_dict[ingr['ingredient_name']] ['quantity'] += ingr_temp_dict[ingr['ingredient_name']] ['quantity']
        else:
            ingr_temp_dict[ingr['ingredient_name']] = {'quantity': int(ingr['quantity'])*person_count, 'measure': ingr['measure']}

    return ingr_temp_dict


with open('recipes.txt', encoding='UTF-8') as f:
    cook_book = {}
    ingr_list = []
    while True:
        dish_name = f.readline().rstrip()
        if dish_name == "":
            break
        ingr_cnt = int(f.readline().rstrip())
        for i in range(ingr_cnt):
            ingr_list.append(f.readline().replace('\n', '').split(' | '))
        f.readline()
        cb_make(dish_name, ingr_list)

pprint(cook_book, width=100)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))