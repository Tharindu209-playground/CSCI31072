import json

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }

class RecipeBook:
    def __init__(self, file_path="recipes.json"):
        self.file_path = file_path
        self.recipes = []
        self.load_recipes()

    def load_recipes(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.recipes = [Recipe(**recipe) for recipe in data]
        except FileNotFoundError:
            pass

    def save_recipes(self):
        with open(self.file_path, "w") as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.save_recipes()
        print(f"Added recipe: {recipe.name}")

    def search_recipe(self, name):
        try: 
            for recipe in self.recipes:
                if recipe.name == name:
                    return recipe
        except AttributeError:
            print("No recipes found.")
        return None

# Sample Usage
recipe_book = RecipeBook()
recipe_book.add_recipe(Recipe("Pancakes", ["Flour", "Eggs", "Milk"], "Mix and cook"))
recipe_book.add_recipe(Recipe("Spaghetti", ["Pasta", "Tomato Sauce", "Meat"], "Boil and cook"))
recipe_book.add_recipe(Recipe("Pizza", ["Dough", "Tomato Sauce", "Cheese"], "Bake and cook"))

searched_recipe = recipe_book.search_recipe("Tea")
print(searched_recipe.name, searched_recipe.ingredients)

searched_recipe = recipe_book.search_recipe("Pizza")
print(searched_recipe.name, searched_recipe.ingredients)
