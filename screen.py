from turtle import Turtle, Screen
from body_generation import User_body, Enemy_body
from random import randint

_WINDOW_HEIGHT = 1000
_WINDOW_WIDTH = 800

class Screen_of_the_game():

    new_screen = None
    game_score = 0
    new_score_text = None
    user_body_instance = None
    enemy_body_instance = None
    new_ammo_text = None
    
    def __init__(self, user_body_instance:User_body, enemy_body_instance:Enemy_body) -> None:
        self.user_body_instance = user_body_instance
        self.enemy_body_instance = enemy_body_instance
        self.create_screen()
        self.create_title()
        self.create_score_counter_text()
        self.create_ammo_text()
        self.new_screen.update()
        self.new_screen.onkeypress(self.user_body_instance.user_movment_right, "d")
        self.new_screen.onkeypress(self.user_body_instance.user_movment_left, "a")
        self.new_screen.listen()
        self.new_screen.ontimer(self.game_loop, 1)
        
        
        
    def update_screen(self):
        self.new_screen.update()
        
    def create_screen(self):
        self.new_screen = Screen()
        self.new_screen.setup(width=_WINDOW_WIDTH, height=_WINDOW_HEIGHT, startx=0, starty=0)
        self.new_screen.bgcolor("black")
        
    def create_title(self):
        self.new_screen.title("Space invaders by Zerko3")
        
    def create_score_counter_text(self):
        self.new_score_text = Turtle()
        self.new_score_text.color("white")
        self.new_score_text.penup()
        self.new_score_text.hideturtle()
        self.new_score_text.setposition(0,400)
        self.update_score_text(self.game_score)
        
    def create_ammo_text(self):
        self.new_ammo_text = Turtle()
        self.new_ammo_text.color("white")
        self.new_ammo_text.penup()
        self.new_ammo_text.hideturtle()
        self.new_ammo_text.setposition(-300,400)
        self.new_ammo_text.write(arg=f"|", move=False, align='center', font=('Arial', 20, 'normal'))
        self.update_screen()
      
    def game_loop(self):
        
        if self.user_body_instance.player_current_position_on_x < 200.0 and self.user_body_instance.player_current_position_on_x > -200.0:
            self.new_screen.onkeypress(self.user_body_instance.user_movment_right, "d")     
            self.new_screen.onkeypress(self.user_body_instance.user_movment_left, "a")
        elif self.user_body_instance.player_current_position_on_x > 200.0:
            # Unbind the movement keys if player is outside the bounds
            self.new_screen.onkeypress(None, "d")
            self.new_screen.onkeypress(self.user_body_instance.user_movment_left, "a")
        elif self.user_body_instance.player_current_position_on_x < -200.0:
            self.new_screen.onkeypress(None, "a")
            self.new_screen.onkeypress(self.user_body_instance.user_movment_right, "d") 
   
        self.new_screen.listen()
        # get the y and x cor
        enemy_curr_pos = self.enemy_body_instance.get_enemy_position()
        
        # Capture the projectile position
        p = self.user_body_instance.user_shoot(enemy_location=enemy_curr_pos)
                        
        # logic for counter
        if p.hit_state:
            self.new_score_text.clear()
            self.game_score += 1
            self.update_score_text(self.game_score) 
            self.enemy_body_instance.hide_enemy_turtle()
            
            # delete projectile object
            del p
            
            # delete the enemy
            del self.enemy_body_instance 
            
            random_starting_location_y = randint(0,3)
            random_starting_location_x = randint(0,4)
            
            
            possible_starting_locations_y = [200,250,300,350]
            possible_starting_locations_x = [-100,0,100,200,300]
            
            starting_location_of_enemy_y = possible_starting_locations_y[random_starting_location_y]
            
            starting_location_of_enemy_x = possible_starting_locations_x[random_starting_location_x]
            
            # call the new enemy
            self.enemy_body_instance = Enemy_body("turtle", "orange", starting_location_of_enemy_x,starting_location_of_enemy_y)
            self.update_screen()
        else:
            pass
        
        # update the screen and call back the loop
        self.new_screen.ontimer(self.game_loop, 1)

    def score_counter(self):
     
        self.new_score_text.clear()
        self.game_score += 1
        self.update_score_text(self.game_score)
       
        
    def update_score_text(self,score):
        
        self.new_score_text.color("white")
        self.new_score_text.write(arg=f"SCORE: {score}", move=False, align='center', font=('Arial', 20, 'normal'))
        self.update_screen()
        
        
      
    def exit_screen(self):
        # this needs to be the last thing PYTHON read for now. Since its read top down, if Python comes to this method it will "wait" till its finishes (the user clicks) so than the setup method wont run. If this is the last thing on here for now, the setup method will run normally!        
        self.new_screen.exitonclick()


    
# 1. if player pos is < than width we can move
# 2. if player pos == widht then we cannot move 