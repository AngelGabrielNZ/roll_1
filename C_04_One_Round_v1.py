import random

# Intialise rounds points
user_points = 0
comp_points = 0
double_user = "no"

# Roll the dice for the user and note if they got double
user_one = random.randint(1, 6)
user_two = random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"


# roll the dice for the computer
comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)

# Update the user / computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two

# Output the results
print("\nintial Points")
print(f"User     - Roll 1: {user_one} \t| Roll 2: {user_two} \t| Total: {user_points} ")
print(f"Computer - Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Total: {comp_points} ")

# let the user know if they qualify for the double points
if double_user == "yes":
    print("great news - if you win, you wil earn double points!")





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


# main routine starts here
game_goal = int_check()
print(game_goal)
