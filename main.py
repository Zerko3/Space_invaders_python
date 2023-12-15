import body_generation
import screen

# Game window
GAME_MODE = True
projectile = None

 # generate the user body and the enemy body
enemy_body = body_generation.Enemy_body("turtle", "orange")
user_body = body_generation.User_body("triangle", "white")
# W

# generate the screen of the game
screen_of_the_game = screen.Screen_of_the_game(user_body,enemy_body)

# call the mainloop of the game -> start the game here
screen_of_the_game.new_screen.mainloop()

# TODO:
# 1. Add xcor and ycor for if statement
# 2. Add more than one enemy
# 3. Kill the enemy if I hit the enemy
