def not_blank(question):
    """checks that the user responce is not blank"""


    while True:
        response = input(question)

        if response !="":
            return response

        print("please fill this in. \n to try again")


#main routine starts here
name = not_blank("Whats the name of your recipe:  ")
print(f"you chose {name}")






