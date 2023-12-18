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
_ENEMY_START_Y_POSITION = 200
_ENEMY_CURRENT_Y_POSITION = 0

# randomize this number later
_ENEMY_START_X_POSITION = 0

class Enemy_body():

    # later add a list of enemys
    enemys = []
    enemy_body = Turtle
    
    def __init__(self,shape,color,starting_position_x,starting_position_y) -> None:
        self.shape = shape
        self.color = color
        self.starting_position_y = starting_position_y
        self.starting_position_x = starting_position_x
        self.generate_body(shape,color)
        self.get_enemy_position()
        
    def __del__(self):
        print("DESTROYED")
        
    def generate_body(self, shape, color):
        self.enemy_body = Turtle(shape)
        self.enemy_body.hideturtle()
        self.enemy_body.penup()
        self.enemy_body.color(color)
        self.enemy_body.setheading(_SET_ENEMY_HEAD_SOUTH)
        
        # randomize this later
        self.enemy_body.setposition(self.starting_position_x,self.starting_position_y)
        self.enemy_body.showturtle()        
        
    def get_enemy_position(self):
        return self.enemy_body.pos()
    
    def hide_enemy_turtle(self):
        self.enemy_body.hideturtle()


class User_body():
    
    user_game_body = Turtle

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
       
    def user_shoot(self, enemy_location:tuple):
        return Projectile(self.user_game_body, enemy_location)
   
    
class Projectile():
    
    new_shooting_projectile = Turtle
    enemy_hit = False
    hit_state = False
    
    def __init__(self,starting_location:Turtle, enemy) -> None:
        self.starting_location = starting_location
        self.enemy = enemy
        self.generate_projectile()
    
    def __del__(self):
        print("DESTROYED PROJECTILE")
    
    
    def generate_projectile(self):
        self.new_shooting_projectile = self.starting_location.clone()
        self.new_shooting_projectile.shape("circle")
        self.new_shooting_projectile.color("red")
        self.new_shooting_projectile.setheading(_SET_HEAD_NORTH)
        
        for _ in range(16):
            self.new_shooting_projectile.forward(50)
            projectile_position =  self.new_shooting_projectile.pos()    
            
            if abs(projectile_position[-1] - self.enemy[-1]) < 3 and abs(projectile_position[0] - self.enemy[0]) < 3:
                self.new_shooting_projectile.hideturtle()
                self.killed_enemy(hit_status=True)
                break
            elif projectile_position[-1] > 350.00:
                print("ABOVE")
                self.new_shooting_projectile.hideturtle()
                self.killed_enemy(hit_status=False)
                break
            else:
                pass
                  
    def killed_enemy(self, hit_status):
        if hit_status:
            self.hit_state = True
        else:
            self.hit_state = False
            
   