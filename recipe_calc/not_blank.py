def not_blank(question):
    """checks that the user responce is not blank"""


    while True:
        response = input(question)

        if response !="":
            return response

        print("please fill this in. \n to try again")


#main rouetine starts here
who = not_blank("Whats the name of your recipe:  ")
print(f"you chose {who}")






