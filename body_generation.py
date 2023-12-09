from turtle import Turtle

_PLAYER_MOVE_AMOUNT = 100
_ENEMY_MOVE_AMOUNT = 50
_MOVE_LEFT = 180
_MOVE_RIGHT = 0
_SET_HEAD_NORTH = 90
_PLAYER_STARTING_Y_POSITION = -400
_PLAYER_STARTING_X_POSITION = 0


class Game_body():
  
    new_body = None
    
    def __init__(self) -> None:
        
            pass
    
    def generate_body(self,shape,color):
            self.new_body = Turtle(shape)
            self.new_body.penup()
            self.new_body.color(color) 
            self.new_body.setheading(_SET_HEAD_NORTH)
            self.new_body.setposition(_PLAYER_STARTING_X_POSITION,_PLAYER_STARTING_Y_POSITION)
           
          
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
        
        self.new_body.setheading(_MOVE_LEFT)
        self.new_body.forward(_PLAYER_MOVE_AMOUNT)
        self.new_body.setheading(_SET_HEAD_NORTH)
    
    def user_movment_right(self):
        
        self.new_body.setheading(_MOVE_RIGHT)
        self.new_body.forward(_PLAYER_MOVE_AMOUNT)
        self.new_body.setheading(_SET_HEAD_NORTH)
       
    
    # 2. Make a class method for shooting
    def user_shoot(self):
        pass

class Enemy_body(Game_body):

    def __init__(self) -> None:
        super().__init__()
        
    # TODO:
    # 1. Make a class method for movment