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

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


while True:
    print()

    my_num = num_check("Choose a number : ", 1, 10)
    print(f"You chose {my_num}")
