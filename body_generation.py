from turtle import Turtle

_PLAYER_MOVE_AMOUNT = 100
_ENEMY_MOVE_AMOUNT = 50


class Game_body():
  
    new_body = None
    
    def __init__(self) -> None:
            # self.shape = shape
            # self.color = color
            # self.generate_body(shape, color)
            pass
       

      
    # TODO:
    # 1. Make a class method for body
    def generate_body(self,shape,color):
            self.new_body = Turtle(shape)
            self.new_body.color(color) 
           
          
    # 2. Make a class method for color
    # 3. Make a class method for size
    
    
    
    
    
class User_body(Game_body):
    
    user_game_body = None
    
    def __init__(self) -> None:
        super().__init__()
    
    # def generate_body(self, shape, color):
    #      return super().generate_body(shape, color)
    
    # TODO:
    # 1. Fix the movement
    # 2. Make the only posible movement left and right for now
    
    def user_movment_left(self):
        print("d")
        self.new_body.left(180)
        self.new_body.forward(100)
    
    def user_movment_right(self):
        self.new_body.right(180)
        self.new_body.forward(100)
       
    
    # 2. Make a class method for shooting
    def user_shoot(self):
        pass

class Enemy_body(Game_body):

    def __init__(self) -> None:
        super().__init__()
        
    # TODO:
    # 1. Make a class method for movment