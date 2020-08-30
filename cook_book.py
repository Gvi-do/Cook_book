def book_processing():
  cook_book = {}
  all_ingredients = []
  
  with open('recipes.txt') as f:
    name_of_dish = f.readline()
    number_of_ingredients = int(f.readline())
    i = 0
    while i < number_of_ingredients:
      ingredient = {}
      string = f.readline()
      ingredient['ingredient_name'] = string.split('|')[0]
      ingredient['quantity'] = string.split('|')[1]
      ingredient['measure'] = string.split('|')[2]
      
      i += 1
      all_ingredients.append(ingredient)
        
  cook_book[name_of_dish] = all_ingredients
  return cook_book
print(book_processing())



