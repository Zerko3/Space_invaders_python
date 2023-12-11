# from turtle import Turtle, Screen
import body_generation
import screen



# TODO:

# 2. Make the user move left and right
# 3. "Shoot" out arrow aa
# 4. If arrows shoot out and they hit the target x times, "kill" the target
# 5. Add to the score
# 6. If the enemy goes behind the user or get to the x,y coordinates the user looses lifes
# 7. End game after the user looses x lifes
# 8. Make it so that the user cannot go beyond the walls

# Game window


# create user player




GAME_MODE = True
  


# create window

# create enemy body - comment out for now
# enemy_body = body_generation.Enemy_body()
# enemy_body.generate_body("circle", "blue")

while GAME_MODE:
  
    user_body = body_generation.User_body("triangle", "white")
    enemy_body = body_generation.Enemy_body("turtle", "orange")

 
    screen_of_the_game = screen.Screen_of_the_game()
    screen_of_the_game.new_screen.onkeypress(user_body.user_movment_left, "a")
    screen_of_the_game.new_screen.onkeypress(user_body.user_movment_right, "d")
    screen_of_the_game.new_screen.onkeypress(user_body.user_shoot, "space")
    # we need this to register click events
    screen_of_the_game.new_screen.listen()
    
    # call this when we exit the game
    screen_of_the_game.exit_screen()
    
    
    
    
    
    
  








