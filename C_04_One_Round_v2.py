import random


def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = 'please enter an integer more then / equal to 13.'

    while True:
        try:
            response = int(input('what is the game goal? '))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for the user and note if they got double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double

#  main starts..

# Roll the dice know if they qualify for double points
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

# Retrieve user points (first item return from function)
user_points = initial_user[0]
# comp_points = initial_comp[0]

double_user = initial_user[1]

# let the user know if they qualify for the double points
if double_user == "yes":
    print("Great news - if you win, you wil earn double points!")

print()
# main routine starts here
game_goal = int_check()
print(game_goal)
