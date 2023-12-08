# from turtle import Turtle, Screen
import body_generation
import screen
from turtle import Screen


# TODO:

# 2. Make the user move left and right
# 3. "Shoot" out arrow 
# 4. If arrows shoot out and they hit the target x times, "kill" the target
# 5. Add to the score
# 6. If the enemy goes behind the user or get to the x,y coordinates the user looses lifes
# 7. End game after the user looses x lifes
# 8. Make it so that the user cannot go beyond the walls

# Game window


# create user player
s = Screen()
user_body = body_generation.User_body()
user_body.generate_body("triangle", "white")



s.onkeypress(user_body.user_movment_left, "a")
s.onkeypress(user_body.user_movment_right, "d")
# we need this to register click events
s.listen()
  


# create window
screen_of_the_game = screen.Screen_of_the_game()

# create enemy body - comment out for now
# enemy_body = body_generation.Enemy_body()
# enemy_body.generate_body("circle", "blue")








