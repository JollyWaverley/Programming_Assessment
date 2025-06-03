def string_checker(question, valid_ans_list=('ml','kg','g'), num_letters=1):
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

string_checker("20g")