def create_cook_book(recipe_file):
    recipe_book = {}
    with open(recipe_file, encoding='utf-8') as recipe_file_obj:
        for line in recipe_file_obj:
            dish_name = line.strip()
            quantity_ingredients = int(recipe_file_obj.readline().strip())
            ingredients_list = []
            for item in range(quantity_ingredients):
                ingredient = {}
                ingredient_line = recipe_file_obj.readline().strip().split(' | ')
                ingredient['ingredient_name'] = ingredient_line[0]
                ingredient['quantity'] = int(ingredient_line[1])
                ingredient['measure'] = ingredient_line[2]
                ingredients_list.append(ingredient)
            recipe_book[dish_name] = ingredients_list
            recipe_file_obj.readline()
    return recipe_book


# Добавила на вход еще один аргумент, книгу рецептов, чтобы функция не зависела от наличия глобальной переменной
# cook_book. Так вместо cook_book в функцию можно сразу передать вызов функции create_cook_book()
def get_shop_list_by_dishes(dishes, person_count, recipe_book):
    shop_list = {}
    for dish in dishes:
        if dish not in recipe_book.keys():
            return 'В кулинарной книге нет рецепта одного или нескольких из указанных блюд, проверьте список'
        for ingredient in recipe_book[dish]:
            if ingredient['ingredient_name'] not in shop_list.keys():
                new_item = ingredient['ingredient_name']
                new_item_value = {}
                new_item_value['measure'] = ingredient['measure']
                new_item_value['quantity'] = ingredient['quantity'] * person_count
                shop_list[new_item] = new_item_value
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


cook_book = create_cook_book('recipes.txt')
my_shop_list = get_shop_list_by_dishes(["Фахитос", "Омлет"], 1, create_cook_book('recipes.txt'))

