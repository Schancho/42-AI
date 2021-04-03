
cookbook = {}
recipe = {}

def     add_recipe(recipe_name, ingredients, meal_type, prep_time):
    ingredient = ingredients.split(", ")
    recipe = {'ingredients' : ingredient, 'meal type' : meal_type, 'preparation time' : prep_time}
    cookbook[recipe_name] = recipe

add_recipe("Sandwich", "ham, bread, cheese, tomatoes", "lunch", 10)
add_recipe("Cake", "flour, sugar, eggs", "dessert", 60)
add_recipe("Salad","avocado, argula, tomatoes, spinach", "lunch", 15)
print(cookbook)

