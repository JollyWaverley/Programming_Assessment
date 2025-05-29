import math

# function here

# Checks if the user responded yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        if response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")

# checks if the users response was blank and makes them enter an answer to continue
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
# checks for an integer and if it's not one asks them to put one in
def int_check(question):
    error = "oops - please enter an integer."

    while True:

        try:

            response = int(input(question))

            return response

        except ValueError:
            print(error)

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

def currency(x):
    """formats number as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine here
# Lists to hold info on the ingredients (what it is, price, and how much they have)
ingredient = []
amount = []
price = []

ingredient_dict= {
    'ingredient': ingredient,
    'amount': amount,
    'price': price
}



# asks if they want instructions
want_instruction = yes_no("do you want to see instructions?")
print()

if want_instruction == "yes":
    instructions()
# Asks for recipe name
recipe = not_blank("Whats the name of your recipe?:  ")
print(f"your making {recipe}")


print()
while True:
    ingredient = not_blank("Ingredient: ")
    # once user is done putting in info the "xxx" will end the loop showing the calculations
    if recipe == "xxx":
        break

    amount = int_check("Amount: ")

    price = int_check("Price:$")





