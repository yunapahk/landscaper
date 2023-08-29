## Array of Tools
tools = [
    {"name": "Teeth", "income":1, "price": 0, "quantity": 1},
    {"name": "Rusty Scissors", "income":5, "price": 5, "quantity": 0},
    {"name": "Push Mower", "income":50, "price": 25, "quantity": 0},
    {"name": "Fancy Mower", "income":100, "price": 250, "quantity": 0},
    {"name": "Starving Students", "income":250, "price": 500, "quantity": 0},
]

## Game State
current_tool = 0
money = 0

def reset_game():
    global money, current_tool, tools
    money = 0
    current_tool = 0
    for tool in tools:
        if tool['name'] == "Teeth":
            tool['quantity'] = 1
        else:
            tool['quantity'] = 0
    game_loop()


## start function should
# - print a message introducing the game and options
# - take input from the user (1 = mow 2 = buy)
# - return that input
# This function does NOT have a test
def start():
    print("Welcome to Landscaper!")
    print(f"Current tool: {tools[current_tool]['name']}, Money: ${money}")
    print("1 = Mow, 2 = Buy")
    while True:
        try:
            choice = int(input("Choose an option: "))
            return choice
        except ValueError:
            print("Please enter a valid option (1 or 2).")


## selection function should
# - if user input is 1, run the mow function
# - if user input is 2, run the upgrade function
# - if anything else, text warning
def selection(select):
    if select == 1:
        mow()
    elif select == 2:
        upgrade()
    else:
        print("Invalid option!")

## mow function
# to refer to global variables look up global keyword
# - should up income based on current_tool & tools list
# - print message
def mow():
    global money 
    total_income = sum(tool['income'] * tool['quantity'] for tool in tools)
    money += total_income
    print(f"You earned ${total_income} today!")

## upgrade function
# - check to see if money is enough to buy the next tool
# - if so upgrades tool by incrementing current_tool
# - if not, print message saying money isn't enough
def upgrade():
    global money, current_tool, tools
    print("1 = Buy, 2 = Sell")
    choice = int(input("Would you like to buy or sell? "))
    if choice == 1:
        if current_tool == len(tools) - 1:  
            print("You already have the best tool!")
            return
        next_tool_price = tools[current_tool + 1]['price']
        if money >= next_tool_price:
            money -= next_tool_price
            current_tool += 1
            tools[current_tool]['quantity'] += 1
            print(f"You've bought {tools[current_tool]['name']}!")
        else:
            print(f"You don't have enough money to buy {tools[current_tool + 1]['name']}!")
    elif choice == 2:
        if current_tool == 0:
            print("You can't sell your teeth!")
            return
        sell_price = tools[current_tool]['price'] // 2
        money += sell_price
        tools[current_tool]['quantity'] -= 1
        print(f"You've sold {tools[current_tool]['name']} for ${sell_price}!")

    else:
        print("Invalid option!")


## the win_conditions functions
# check if the current tool is the team and money is 1000
# If true, print a win message then return true
# If false, print the players money total and tool and run game_loop()
def win_conditions():
    if current_tool == len(tools) - 1 and money >= 1000:
        print("Congratulations! You've won the game!")
        return True
    else:
        print(f"Current tool: {tools[current_tool]['name']}, Money: ${money}")
        return False


## GAME LOOP
def game_loop():
    while True:
        select = start()
        selection(select)
        if win_conditions():
            play_again = input("Do you want to play again? (yes/no) ").strip().lower()
            if play_again == 'yes':
                reset_game()
            else:
                break

if __name__ == "__main__":
    game_loop()
