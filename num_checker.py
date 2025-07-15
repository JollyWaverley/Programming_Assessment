def num_check(question):
    error = "oops - please enter an integer."
    """Checks if its a number and asks to input one if the answer is not one"""
    while True:

        try:

            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)
            return response

        except ValueError:
            print(error)

number = num_check("choose a number ")
print(f"you choose {number}")

