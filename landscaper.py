## Array of Tools
tools = [
    {"name": "Teeth", "income":1, "price": 0},
    {"name": "Rusty Scissors", "income":5, "price": 5},
    {"name": "Push Mower", "income":50, "price": 25},
    {"name": "Fancy Mower", "income":100, "price": 250},
    {"name": "Starving Students", "income":250, "price": 500},
]

## Game State
current_tool = 0
money = 0


## start function should
# - print a message introducing the game and options
# - take input from the user (1 = mow 2 = buy)
# - return that input
# This function does NOT have a test
def start():
    return 0

## selection function should
# - if user input is 1, run the mow function
# - if user input is 2, run the upgrade function
# - if anything else, text warning
def selection(select):
   return 0


## mow function
# to refer to global variables look up global keyword
# - should up income based on current_tool & tools list
# - print message
def mow():
    return 0

## upgrade function
# - check to see if money is enough to buy the next tool
# - if so upgrades tool by incrementing current_tool
# - if not, print message saying money isn't enough
def upgrade():
    return 0



## the win_conditions functions
# check if the current tool is the team and money is 1000
# If true, print a win message then return true
# If false, print the players money total and tool and run game_loop()
def win_conditions():
    return 0





## GAME LOOP

def game_loop():
    ## get users input
    select = start()
    ## run a particular action
    selection(select)
    ## check win conditions and start again
    win_conditions()