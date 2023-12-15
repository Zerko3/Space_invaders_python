from turtle import Turtle, Screen
from body_generation import User_body, Enemy_body

_WINDOW_HEIGHT = 1000
_WINDOW_WIDTH = 800

class Screen_of_the_game():

    new_screen = None
    game_score = 0
    new_score_text = None
    user_body_instance = None
    enemy_body_instance = None
    
    def __init__(self, user_body_instance:User_body, enemy_body_instance:Enemy_body) -> None:
        self.user_body_instance = user_body_instance
        self.enemy_body_instance = enemy_body_instance
        self.create_screen()
        self.create_title()
        self.create_score_counter_text()
        self.new_screen.ontimer(self.game_loop, 100)
        self.new_screen.listen()
        self.new_screen.onkeypress(self.user_body_instance.user_movment_left, "a")
        self.new_screen.onkeypress(self.user_body_instance.user_movment_right, "d")
       
        
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
      
    def game_loop(self):
    
        # get the y and x cor
        enemy_curr_pos = self.enemy_body_instance.get_enemy_position()
        print("ENEMY POS:", enemy_curr_pos)
        
        # Capture the projectile position
        projectile = self.user_body_instance.user_shoot(enemy=enemy_curr_pos)
        
        
        if projectile is not None:
            projectile_position = projectile.get_projectile_position()
            print("USER POS:", projectile_position)

            # here we check if the enemy is on the same Y axis and on the same X axis 
            if projectile_position[-1] > enemy_curr_pos[-1] and projectile_position[0] == enemy_curr_pos[0]:
                print("Hit!")
                self.score_counter()
                projectile.player_hit_enemy(status_of_hit=True)

        # call this method when we exit the game
        self.new_screen.ontimer(self.exit_screen, 100)
        self.new_screen.ontimer(self.game_loop, 100)
     
    def score_counter(self):
        print("score_counter")
        # self.new_score_text.clear()
        self.game_score += 1
        self.update_score_text(self.game_score)
       
        
    def update_score_text(self,score):
        print("update")
        self.new_score_text.clear()
        self.new_score_text.write(arg=f"SCORE: {score}", move=False, align='center', font=('Arial', 20, 'normal'))
        
      
    def exit_screen(self):
        # this needs to be the last thing PYTHON read for now. Since its read top down, if Python comes to this method it will "wait" till its finishes (the user clicks) so than the setup method wont run. If this is the last thing on here for now, the setup method will run normally!        
        self.new_screen.exitonclick()


    