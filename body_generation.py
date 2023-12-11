from turtle import Turtle

_PLAYER_MOVE_AMOUNT = 100
_ENEMY_MOVE_AMOUNT = 50
_MOVE_LEFT = 180
_MOVE_RIGHT = 0
_SET_HEAD_NORTH = 90
_SET_ENEMY_HEAD_SOUTH = 270
_PLAYER_STARTING_Y_POSITION = -400
_PLAYER_STARTING_X_POSITION = 0
_END_OF_THE_SCREEN_ON_Y_CORR = 500
_ENEMY_START_Y_POSITION = 400

# randomize this number later
_ENEMY_START_X_POSITION = 0

# TODO:
# 1. Refactor the classes, like this:
# a) Make the class User_body and Enemy_body standalone classes
# b) Make a subclass for the Enemy class for diferent enemys types, for startes I will make 2 types

class User_body():
    
    user_game_body = None
    
    def __init__(self,shape,color) -> None:
        self.shape = shape
        self.color = color
        self.generate_body(shape,color)
        
    def generate_body(self,shape,color):
        self.user_game_body = Turtle(shape)
        self.user_game_body.penup()
        self.user_game_body.color(color)
        self.user_game_body.setheading(_SET_HEAD_NORTH)
        self.user_game_body.setposition(_PLAYER_STARTING_X_POSITION,_PLAYER_STARTING_Y_POSITION)
           
    
    def user_movment_left(self):
        
        self.user_game_body.setheading(_MOVE_LEFT)
        self.user_game_body.forward(_PLAYER_MOVE_AMOUNT)
        self.user_game_body.setheading(_SET_HEAD_NORTH)
        self.player_current_position = self.user_game_body.pos()
        
    
    def user_movment_right(self):
        
        self.user_game_body.setheading(_MOVE_RIGHT)
        self.user_game_body.forward(_PLAYER_MOVE_AMOUNT)
        self.user_game_body.setheading(_SET_HEAD_NORTH)
        self.player_current_position = self.user_game_body.pos()
       
    
    # 2. Make a class method for shooting
    def user_shoot(self): 
        new_shooting_projectile = self.user_game_body.clone()
        new_shooting_projectile.speed(8)
        new_shooting_projectile.shape("circle")
        new_shooting_projectile.color("red")
        new_shooting_projectile.setheading(_SET_HEAD_NORTH)
        CURRENT_X_POSITION_OF_THE_PLAYER,_ = new_shooting_projectile.pos()
        new_shooting_projectile.goto(CURRENT_X_POSITION_OF_THE_PLAYER, _END_OF_THE_SCREEN_ON_Y_CORR)
        
       
        

class Enemy_body():

    # later add a list of enemys
    enemys = []
    enemy_body = None
    
    def __init__(self,shape,color) -> None:
        self.shape = shape
        self.color = color
        self.generate_body(shape,color)
        
    def generate_body(self, shape, color):
        self.enemy_body = Turtle(shape)
        self.enemy_body.hideturtle()
        self.enemy_body.penup()
        self.enemy_body.color(color)
        self.enemy_body.setheading(_SET_ENEMY_HEAD_SOUTH)
        
        # randomize this later
        self.enemy_body.setposition(_ENEMY_START_X_POSITION,_ENEMY_START_Y_POSITION)
        self.enemy_body.showturtle()        
        
        
    # TODO:
    # 1. Make a class method for movment
    
    # 2. Make a class method for "hitting" the enemy
    
    # 3. Return a score counter so I can pass it into the screen class