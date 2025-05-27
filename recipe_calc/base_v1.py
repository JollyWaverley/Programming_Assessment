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




# Main routine here
# loop for testing
want_instruction = yes_no("do you want to see instructions?")
print()

if want_instruction == "yes":
    instructions()

who = not_blank("Whats the name of your recipe:  ")
print(f"your making {who}")


