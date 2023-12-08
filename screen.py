from turtle import Screen

class Screen_of_the_game():

    new_screen = None
    
    def __init__(self) -> None:
        self.create_screen()
        self.create_title()
        self.screen_size()
        
    def create_screen(self):
        self.new_screen = Screen()
        self.new_screen.bgcolor("black")
        
    def create_title(self):
        self.new_screen.title("Space invaders by Zerko3")
      
    def create_score(self):
        pass
      
    def score_counter(self):
        pass
        
    def screen_size(self):
        self.new_screen.setup(width=800, height=1000, startx=0, starty=0)
        
        # this needs to be the last thing PYTHON read for now. Since its read top down, if Python comes to this method it will "wait" till its finishes (the user clicks) so than the setup method wont run. If this is the last thing on here for now, the setup method will run normally!        
      
        self.new_screen.exitonclick()


    