#import math
import pandas

from frc.P_play_area import response


# function here

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

        if response !="":
            return response

        print("please fill this in. \n to try again")

# when called will print instructions
def instructions():
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
    error = "oops - please enter an integer."
    """Checks if its a number and asks to input one if the answer is not one"""
    while True:

        try:

            response = float(input(question))

            return response

        except ValueError:
            print(error)

def string_checker(question, valid_ans_list=('ml','kg','g','l','whole'), num_letters=1):
    """checks for users answer and checks it against a walid response list"""

    while True:

        response = input(question).lower()

        for option in valid_ans_list:

            if response == option:
                return option

            # check if it's the first letter
            elif response == option[:num_letters]:
                return option

        print(f"please choose an option from {valid_ans_list}")



# makes a statement that looks nice and is a good way to display the answers

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



def food_units(unit_type):

    error = "please enter this list (g,kg,ml,l,whole)"

    response = input("what is the measurement is the item whole")

    if response[0] == "kg":
        unit_type = "kg"


























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


# Main routine here

# asks if they want instructions
want_instruction = yes_no("do you want to see instructions?")
print()

if want_instruction == "yes":
    instructions()
#comment later !!!!
num_check("How many severing will this make?: ")

# Asks for recipe name
recipe = not_blank("Whats the name of your recipe?:  ")
print(f"your making {recipe}")


print()
while True:
    ingredient = not_blank("Ingredient: ")
    # once user is done putting in info the "xxx" will end the loop showing the calculations
    if ingredient == "xxx":
        break
    num_check("Amount: ")

    amount_unit = string_checker("g,ml,kg,l if a whole object type whole?")


    price = num_check("Price for the ingredient:$")
    continue

# End of loop

recipe_info = pandas.DataFrame(recipe)







