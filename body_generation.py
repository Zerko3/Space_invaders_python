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

    
    def __init__(self,shape,color) -> None:
        self.shape = shape
        self.color = color
        self.generate_body(shape,color)
        self.get_enemy_position()
        
    def generate_body(self, shape, color):
        self.enemy_body = Turtle(shape)
        self.enemy_body.hideturtle()
        self.enemy_body.penup()
        self.enemy_body.color(color)
        self.enemy_body.setheading(_SET_ENEMY_HEAD_SOUTH)
        
        # randomize this later
        self.enemy_body.setposition(_ENEMY_START_X_POSITION,_ENEMY_START_Y_POSITION)
        self.enemy_body.showturtle()        
        
    def get_enemy_position(self):
        return self.enemy_body.pos()


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
       
    
    # feed in projectile the location of the enemy
    # 2. Make a class method for shooting
    def user_shoot(self, enemy:tuple):
        print(enemy) 
        return Projectile(self.user_game_body, enemy)
   
    
class Projectile():
    
    new_shooting_projectile = Turtle
    enemy_hit = False
    
    def __init__(self,starting_location:Turtle, enemy) -> None:
        self.starting_location = starting_location
        self.enemy = enemy
        print("FROM PROJECTILE", enemy)
        self.generate_projectile()
    
    def generate_projectile(self):
        self.new_shooting_projectile = self.starting_location.clone()
        self.new_shooting_projectile.shape("circle")
        self.new_shooting_projectile.color("red")
        self.new_shooting_projectile.setheading(_SET_HEAD_NORTH)
        
        # shooting logic, getting y cor logic. GOTO is not the best solution to getting updated Y cor!
        for _ in range(14):
            self.new_shooting_projectile.forward(50)
            projectile_position =  self.new_shooting_projectile.pos()    
            
            if abs(projectile_position[-1] - self.enemy[-1]) < 3 and abs(projectile_position[0] - self.enemy[0]) < 3:
                print("HIIIIIIIIIIIT")
                self.player_hit_enemy(True)
            # self.get_projectile_position()
         
            
    def get_projectile_position(self):
        return self.new_shooting_projectile.pos()
    
    
    # get the input from main pass it in here return true or false, then give this method to for loop to brake it
    def player_hit_enemy(self, status_of_hit:bool):
        print(status_of_hit)
        if status_of_hit:
            self.new_shooting_projectile.hideturtle()
        else:
            self.enemy_hit = False
      
