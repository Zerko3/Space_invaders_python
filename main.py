import body_generation
import screen

# Game window
GAME_MODE = True
projectile = None

# generate the user body and the enemy body
user_body = body_generation.User_body("triangle", "white")
enemy_body = body_generation.Enemy_body("turtle", "orange", 0, 200)
screen_of_the_game = screen.Screen_of_the_game(user_body,enemy_body)

# generate the screen of the game

# call the mainloop of the game -> start the game here
screen_of_the_game.new_screen.mainloop()
screen_of_the_game.update_screen()


