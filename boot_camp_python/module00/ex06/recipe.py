
cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal"       : "lunch",
        "prep_time"  : 10, 
        },
    "cake": {
        "ingredients": ["flour", "sugar","eggs"],
        "meal"       : "dessert",
        "prep_time"  : 10,
        },
    "salad": {
        "ingredients": ["avocado", "argula", "tomatoes", "spinach"],
        "meal"       : "lunch",
        "prep_time"  : 15,
        }
    }
def     print_cookbook(cookbook):
    for element in cookbook.keys():
        print(element)

def     delet_recipe(name):
    del cookbook[name]
def     print_recipe(name):
    if not (name in cookbook):
        """print("this recipe doesn't exist, please enter an existed one")
        test = input("print yes to print the cookbook or the recipe name to print a recipe otherwise print quit to exit: ")
        if test == "yes":
            print(cookbook)
            print_recipe(name)
        elif test == quit:
            print("cookbook closed.")
            exit(0)
        else:
            print_recipe(name)"""
        return
    recipe = cookbook[name]
    
    print("recipe for {name}:".format(name=name))
    print("ingredients list: {list}".format(list=recipe["ingredients"]))
    print("to be eaten for {type}.".format(type=recipe["meal"]))
    print("Takes {time} minutes of cooking.".format(time=recipe["prep_time"]))

def     add_recipe(recipe_name, ingredients, meal_type, prep_time):
    recipe = {'ingredients' : ingredients, 'meal' : meal_type, 'prep_time' : prep_time}
    cookbook[recipe_name] = recipe
def     option(number):
    if number == 1:
        ingredients = []
        recipe_name = input("Please enter recipe name:\n>> ")
        print("please enter recipe's engridients, tap Enter after each. tap F to finish:")
        while True:
            ingredients.append(input("-  "))
            if ingredients[-1] == '':
                ingredients.pop()
                break
        meal = input("please enter recipe's meal type: ")
        time = int(input("please enter reciepe's preparation time: "))
        add_recipe(recipe_name,ingredients,meal,time)
    elif number == 2:
        delet_recipe(input("please enter recipe's name to delete:\n>> "))
    elif number == 3:
        print_recipe(input("Please enter recipe's name to print\n>> "))
    elif number == 4:
        print_cookbook(cookbook)
    elif number == 5:
        print("Cookbook closed.")
        exit(0)
    else:
        print("This option does not exist, please type the corresponding number. To exit, enter 5.")
    
while True:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    try:
        try:
            number = int(input())
        except ValueError:
            number = 0
    except EOFError:
        break
    if option(number) == -1:
        print("This option does not exist, please type the corresponding number.")
        print("to exit, enter 5")
        n = int(input(">>"))
        if n == 5:
            print("quit!")
            exit(0)


print(name)

