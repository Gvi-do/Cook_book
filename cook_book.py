def book_processing():
  cook_book = {}
  with open('recipes.txt') as f:
    for line in f:
      all_ingredients = []
      name_of_dish = line.strip()
      number_of_ingredients = int(f.readline())
      i = 0
      while i < number_of_ingredients:
        
        ingredient = {}
        string = f.readline()
        ingredient['ingredient_name'] = string.split('|')[0].strip()
        ingredient['quantity'] = int(string.split('|')[1].strip())
        ingredient['measure'] = string.split('|')[2].strip()
      
        i += 1
        all_ingredients.append(ingredient)
      f.readline() 
      cook_book[name_of_dish] = all_ingredients    
  return cook_book
print(book_processing())

def get_shop_list_by_dishes(dishes = '', person_count = 0):
  shop_list = {}
  dishes = []
  while True:
    dish = input('Введите блюдо, введите в для выхода: ')
    if dish != 'в':
      dishes.append(dish)
    else:
      person_count = int(input('Введите количество гостей: '))
      break
  cook_book = book_processing()
  for name_of_dish in dishes:
    for ingredient in cook_book[name_of_dish]:
      the_amount_of_ingredient = {}
      the_amount_of_ingredient['measure'] = ingredient['measure']
      the_amount_of_ingredient['quantity'] = ingredient['quantity'] * person_count
      if ingredient['ingredient_name'] in shop_list.keys():
        the_amount_of_ingredient['quantity'] += shop_list[ingredient['ingredient_name']]['quantity']
        shop_list[ingredient['ingredient_name']] = the_amount_of_ingredient
      else:    
        shop_list[ingredient['ingredient_name']] = the_amount_of_ingredient
      
  return print(shop_list)

get_shop_list_by_dishes()  




