def food_units(unit_type, valid_answer_list=('milliliters','kilograms','liter','grams','whole')):
    error = f"Please enter from {valid_answer_list}"
    while True:

        response = input(unit_type).lower()


        for item in valid_answer_list:

            if response == item[0] or response == item:
                return item

        print(error)
