from turtle import Turtle, Screen

_WINDOW_HEIGHT = 1000
_WINDOW_WIDTH = 800

class Screen_of_the_game():

    new_screen = None
    game_score = 0
    
    
    def __init__(self) -> None:
        self.create_screen()
        self.create_title()
        self.create_score_counter_text()
        self.exit_screen()
        
    def create_screen(self):
        self.new_screen = Screen()
        self.new_screen.setup(width=_WINDOW_WIDTH, height=_WINDOW_HEIGHT, startx=0, starty=0)
        self.new_screen.bgcolor("black")
        
    def create_title(self):
        self.new_screen.title("Space invaders by Zerko3")
        
    def create_score_counter_text(self):
        new_score_text = Turtle()
        new_score_text.color("white")
        new_score_text.penup()
        new_score_text.hideturtle()
        new_score_text.setposition(0,400)
        new_score_text.write(arg=f"SCORE: {self.game_score}", move=False, align='center', font=('Arial', 20, 'normal'))
       
     
    def score_counter(self):
        pass
      
    def exit_screen(self):
        # this needs to be the last thing PYTHON read for now. Since its read top down, if Python comes to this method it will "wait" till its finishes (the user clicks) so than the setup method wont run. If this is the last thing on here for now, the setup method will run normally!        
        self.new_screen.exitonclick()


    