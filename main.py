from turtle import Turtle, Screen
import body_generation
import game_score

# TODO:
# 1. Create a window of the game
# 2. Make the user move left and right
# 3. "Shoot" out arrow 
# 4. If arrows shoot out and they hit the target x times, "kill" the target
# 5. Add to the score
# 6. If the enemy goes behind the user or get to the x,y coordinates the user looses lifes
# 7. End game after the user looses x lifes

# Game window

# create user player
user_body = body_generation.User_body()
user_body.generate_body("turtle", "red")

# create enemy body - comment out for now
# enemy_body = body_generation.Enemy_body()
# enemy_body.generate_body("circle", "blue")


# create window
scree_of_the_game = Screen()

# Exit the game window
scree_of_the_game.exitonclick()