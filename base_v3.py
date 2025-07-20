import pandas

# functions here
def yes_no(question):
    """checks if input is yes or no and asks again if anything else is input"""
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("please fill this in.")


def instructions():
    """when called will print instructions"""
    print(''' 
====== Instructions ========

For this culculator you will

Put in the name of the recipe 

Put the amount of severing you are making

Put the amount of food you are using and the amounts (g,kg,ml)

Put the amount you paid for the food

After you have put that info in the calculator 
will tell you the cost for each severing.


    ''')
def generate_statement(statement, decoration, lines):
    """will make the headings (3 lines), subheadings(2 lines) and emphasised text / mini-heading (1 line).
       Only use emoji for single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottem = decoration * len(middle)

    if lines == 1:
        return middle
    elif lines == 2:
        two_lines = f"{middle}\n {top_bottem}"
        return two_lines

    else:
        print(top_bottem)
        print(middle)
        print(top_bottem)
        three_lines = f"{top_bottem}\n{middle}\n{top_bottem}"
        return three_lines

def num_check(question, num_type, exit_code=None):
    """checks the users enter an integer / float that is more than zero
    (or the optional exit code)"""

    if num_type == "int":
        error = "oops - please enter an number more than zero."
        change_to = int
    else:
        error = "oops - please enter an number more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0.9:
                return response
            else:
                print(error)

        except ValueError:
            print(error)




def food_units(unit_type, valid_answer_list=('milliliters','kilograms','liter','grams','whole')):
    """asks user for what unit and attaches it to the ingredient it was assigned with"""
    error = f"Please enter m,k,l,g or w"

    while True:

        response = input(unit_type).lower()


        for item in valid_answer_list:

            if response == item[0] or response == item:
                return item

        print(error)

# Lists to hold info to append for pandas
total_price = 0
servings = 0
ingredient_list = []
weight_list = []
amount_unit_list = []
price_list = []
# ingredient dict for the pandas to print well
ingredient_dict = {
    'ingredient': ingredient_list,
    'weight': weight_list,
    'unit' : amount_unit_list,
    'price($)': price_list,

}

# Main routine here

# asks if they want instructions
want_instruction = yes_no("do you want to see instructions?")
print()
# decides if you want_instruction it will print them
if want_instruction == "yes":
    generate_statement(instructions(),"😊",2)

# Checks that servings is a float response is then in the list
servings = num_check("How many severing will this make?: ",int)
# Asks for recipe name
recipe = not_blank("Whats the name of your recipe?:  ")
print(f"your making {recipe}")

print()
while True:
    ingredient = not_blank("Ingredient: ")
    # once user is done putting in info the "xxx" will end the loop showing the calculations
    if ingredient == "xxx":
        break

    ingredient_list.append(ingredient)

    # checks weight is a float and appends weight list
    weight = num_check("weight: ",float)
    weight_list.append(weight)

    # finds what unit users is looking for and assignees that value to the ingredient
    unit = food_units("g,ml,kg,l if a whole object type whole?")
    amount_unit_list.append(unit)

    # checks that price is a float and appends price list
    price = num_check("Price for the ingredient:$",float)
    price_list.append(price)

    # adds all prices for total price
    total_price += price

    # works out cost per serving by dividing total price by servings
    servings_cost = total_price / servings


# End of loop
# Prints all data that the user gives us from appended list
ingredient_frame = pandas.DataFrame(ingredient_dict)

print()
print(ingredient_frame)
print(f"""\n
This recipe makes {int(servings)} 

this recipe cost ${servings_cost:.2f} per severing

The total cost is ${total_price:.2f}
    """)

