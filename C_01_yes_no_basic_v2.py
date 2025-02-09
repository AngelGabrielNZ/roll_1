# functions go here


def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


# Main routine

want_instructions = yes_no("Do you want to see the instructions? ")
want_coffee = yes_no("Do you want coffee? ")

print("we done")
