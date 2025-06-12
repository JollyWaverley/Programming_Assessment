def food_units(unit_type, valid_answer_list=('ml','kg','l','g','whole')):
 #comment later !!!!
    while True:

        response = input(unit_type).lower()

        for option in valid_answer_list:

            if response == option:
                return option

            # check if it's the first letter
            elif response == option[unit_type:]:
                return option

        print(f"please choose an option from {valid_answer_list}")

        response = input("what is the measurement, if a whole item such as eggs enter whole")

        if response[0] == "k":
                unit_type = 'kg'

        if response[0] == "g":
            unit_type = 'g'

        if response[0] == "m":
            unit_type = 'ml'

        if response[0] == "l":
            unit_type = 'l'

        if response[0] == "w":
            unit_type = 'whole'



servings = []
ingredient = []
amount = []
amount_unit = []
price = []
ingredient_dict = {
    'ingredient': ingredient,
    'amount': amount,
    'price': price,
    'servings': servings
}
