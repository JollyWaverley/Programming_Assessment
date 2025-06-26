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


def num_check(question):
    """Checks that response is any number including decimal points and negatives"""
    error = "oops - please enter an integer."
    """Checks if its a number and asks to input one if the answer is not one"""
    while True:

        try:

            response = float(input(question))

            return response

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
    instructions()

# Checks that servings is a float response is then in the list
servings = num_check("How many severing will this make?: ")
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
    weight = num_check("weight: ")
    weight_list.append(weight)

    # finds what unit users is looking for and assignees that value to the ingredient
    unit = food_units("g,ml,kg,l if a whole object type whole?")
    amount_unit_list.append(unit)

    # checks that price is a float and appends price list
    price = num_check("Price for the ingredient:$")
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

