
def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in.")

def food_units(unit_type, valid_answer_list=('milliliters','kilograms','liter','grams','whole')):
    error = f"Please enter m,k,l,g or w"
    while True:

        response = input(unit_type).lower()


        for item in valid_answer_list:

            if response == item[0] or response == item:
                return item

        print(error)
