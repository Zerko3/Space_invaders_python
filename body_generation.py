from turtle import Turtle

class Game_body():
  
    def __init__(self) -> None:
            # self.shape = shape
            # self.color = color
            # self.generate_body(shape, color)
            pass
       

      
    # TODO:
    # 1. Make a class method for body
    def generate_body(self,shape,color):
            new_body = Turtle(shape)
            new_body.color(color) 
           
          
    # 2. Make a class method for color
    # 3. Make a class method for size
    
    
    
    
    
class User_body(Game_body):

    def __init__(self) -> None:
        super().__init__()
    
    # TODO:
    # 1. Make a class method for movment
    # 2. Make a class method for shooting


class Enemy_body(Game_body):

    def __init__(self) -> None:
        super().__init__()
        
    # TODO:
    # 1. Make a class method for movment