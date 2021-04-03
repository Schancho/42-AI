
cookbook = {}
recipe = {}

def     add_recipe(recipe_name, ingredients, meal_type, preparation_time):

    recipe = {'ingredients' : ingredients, 'meal type' : meal_type, 'preparation type' : preparation_time}
    cookbook[recipe_name] = recipe

add_recipe("Sandwich", "", "tawajba", 10)
add_recipe()
print(cookbook)