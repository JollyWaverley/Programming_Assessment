def not_blank(question):
    """checks that the user responce is not blank"""


    while True:
        response = input(question)

        if response !="":
            return response

        print("please fill this in. \n to try again")


def food_units(unit_type, valid_answer_list=('ml','kg','l','g','w')):
 #comment later !!!!

    while True:

        response = input(unit_type).lower()

        for option in valid_answer_list:

            if response == option:
                return option

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
        else:
            print(f"please try {valid_answer_list}")
            return response

#main routine starts here
name = food_units(f"what measurement is this ingredient in: ")
print(f"you chose {name}")