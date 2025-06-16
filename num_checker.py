def num_check(question):
    error = "oops - please enter an integer."
    """Checks if its a number and asks to input one if the answer is not one"""
    while True:

        try:

            response = float(input(question))

            return response

        except ValueError:
            print(error)