# Copyright (c) BrandonPacewic
# SPDX-License-Identifier: MIT

# Not really needed, but I'm keeping it here for now
def clear_console() -> None:
    import os
    os.system('clear')


# Class for handling a percentage
class Percentage:
    # Expects a '%' symbol at the end of the string
    def __init__(self, percentage: str) -> None:
        self.percentage = percentage
        self.percentage_float = float(percentage[:-1]) / 100

    # Returns the percentage as a float
    def get_percentage_float(self) -> float:
        return self.percentage_float

    # Returns the percentage as a string
    def get_percentage_string(self) -> str:
        return self.percentage


# Class that contains all the different nutrition facts for a drink
class Nutrition_facts:
    def __init__(self, 
        calories: str, total_fat: str, saturated_fat: str, 
        trans: str, cholesterol: str, sodium: str, total_carbohydrate: str, 
        dietary_fiber: str, sugars: str, protein: str) -> None:
        try:
            self.calories = float(calories)
            self.total_fat = float(total_fat)
            self.trans = float(trans)
            self.saturated_fat = float(saturated_fat)
            self.cholesterol = float(cholesterol)
            self.sodium = float(sodium)
            self.total_carbohydrate = float(total_carbohydrate)
            self.dietary_fiber = float(dietary_fiber)
            self.sugars = float(sugars)
            self.protein = float(protein)
        except ValueError:
            print(f'Error: Could not convert str to float, check the nutrition facts data for whitespace.')
            exit(1)

    # Take a drink object and create a Nutrition_facts object from it
    def __init__(self, drink: object) -> None:
        self.calories = drink.calories
        self.total_fat = drink.total_fat
        self.trans = drink.trans
        


# Basic starbucks drink class
class Drink(Nutrition_facts):
    def __init__(self,
        category: str, beverage: str, prep: str, 
        calories: str, total_fat: str, trans: str, 
        saturated: str, sodium: str, total_carbohydrates: str, 
        cholesterol: str, fibre: str, sugars: str, 
        protein: str, vitamin_a: str, vitamin_c: str, 
        calcium: str, iron: str, caffeine: str) -> None:
        self.category = category
        self.beverage = beverage
        self.prep = prep
        self.caffeine = caffeine

        # Super refers to the parent class
        super().__init__(calories, total_fat, saturated, trans, 
                         cholesterol, sodium, total_carbohydrates, 
                         fibre, sugars, protein)

        # Stores the vitamin A, C, calcium, and iron amounts as a percentage
        self.vitamin_a = Percentage(vitamin_a)
        self.vitamin_c = Percentage(vitamin_c)
        self.calcium = Percentage(calcium)
        self.iron = Percentage(iron)


    # Returns the max amounts of vitamins and minerals
    # contained between the two drinks
    def max_nutrition_facts(self, other: 'Nutrition_facts') -> Nutrition_facts:
        max_calories = max(self.calories, other.calories)
        max_saturated_fat = max(self.saturated, other.saturated)
        max_trans_fat = max(self.trans, other.trans)
        max_cholesterol = max(self.cholesterol, other.cholesterol)
        max_sodium = max(self.sodium, other.sodium)
        max_fibre = max(self.fibre, other.fibre)
        max_sugars = max(self.sugars, other.sugars)
        max_protein = max(self.protein, other.protein)

        # Returns a new nutrition facts object with the max values
        return Nutrition_facts(
            str(max_calories), str(max_saturated_fat),
            str(max_trans_fat), str(max_cholesterol),
            str(max_sodium), str(max_fibre),
            str(max_sugars), str(max_protein))


def main() -> None:
    # Clear the console
    clear_console()

    # Import the data
    with open('data.lst', 'r') as file:
        starbucks_data = file.readlines()

    print(f'Total menu items: {len(starbucks_data) - 1}\n')

    # List all the categories stored on the first line
    categories = starbucks_data[0].split(',')
    print(f'There are {len(categories)} categories:')

    for i, category in enumerate(categories):
        print(f'{i + 1}. {category}')

    drinks = []

    # Create a list of all the drinks
    for i, drink in enumerate(starbucks_data):
        # Skip the first line, does not contain a drink
        if i == 0:
            continue

        drink = drink.split(',')
        drinks.append(Drink(
            drink[0], drink[1], drink[2],
            drink[3], drink[4], drink[5],
            drink[6], drink[7], drink[8],
            drink[9], drink[10], drink[11],
            drink[12], drink[13], drink[14],
            drink[15], drink[16], drink[17]))

    # Create a set of all the drink categories
    unique_categories = set([drink.category for drink in drinks])

    # Print the total number of unique drink categories
    print(f'There are {len(unique_categories)} unique drink categories:')

    # Run the program multiple time to observe how the order of a set is
    # not guaranteed
    for i, category in enumerate(unique_categories):
        print(f'{i + 1}. {category}')

    # Create a set for all the beverages
    unique_beverages = set([drink.beverage for drink in drinks])

    # Print the total number of unique beverages
    print(f'\nThere are {len(unique_beverages)} unique beverages:')

    # Run the program multiple time to observe how the order of a set is
    # not guaranteed
    for i, beverage in enumerate(unique_beverages):
        print(f'{i + 1}. {beverage}')

    # Create a set for all the prep methods
    unique_prep = set([drink.prep for drink in drinks])

    # Print the total number of unique prep methods
    print(f'\nThere are {len(unique_prep)} unique prep methods:')

    # Run the program multiple time to observe how the order of a set is
    # not guaranteed
    for i, prep in enumerate(unique_prep):
        print(f'{i + 1}. {prep}')

    # Find the max values for each nutrition fact and print them
    


if __name__ == '__main__':
    main()