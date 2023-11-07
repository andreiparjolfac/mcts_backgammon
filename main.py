import State
import Dice
import Backgammon
import json 
import numpy as np
import Node 
import MCTS


state = State.State()
dice = Dice.Dice()
bg = Backgammon.Backgammon()


# node = Node.Node(None,state,dice,bg,1,1)

# mcts = MCTS.MCTS(node,3,2000)
# print(state)
# print(dice)
# mcts.generate_distribution()
# print(mcts.generate_distribution())
# for nd in node.children:
#     print(nd.wins,nd.visits)


# for new_state,move in bg.valid_move_generator(state,player_points,player,5):
#     print(new_state)
#     print(move)
# dice.roll()
# dice.result = [6,6,6,6]

# print(bg.get_all_valid_moves(state,-1,dice))



# simulare mai jos


human_player = int(input("Select player "))
player = None 
dice.roll()
rollWhite = list(dice.result)
dice.roll()
rollBlack = list(dice.result)

while sum(rollBlack) == sum(rollWhite):
    dice.roll()
    rollWhite = list(dice.result)
    dice.roll()
    rollBlack = list(dice.result)

if sum(rollBlack) > sum(rollWhite):
    player = 1 
else:
    player = -1

if player==human_player:
    print("\nYOU START")
else:
    print("\nOPPONENT START")

while not state.game_is_finished():
    if human_player*player==1:
        dice.roll()
        print("YOUR PLAYER ROLLS : ",dice.result,"\n")
        valid_moves = bg.get_all_valid_moves(state,player,dice)
        if not valid_moves == []:
            print(state)
            move = json.loads(input("Enter Your move!\n"))
            print("YOUR PLAYER MOVES : ",move)
            state = bg.make_move(state,player,[move])
        else:
            print("NO MOVE AVAILABLE!")
    elif human_player*player==-1:
        bot_dice = Dice.Dice()
        node = Node.Node(None,state,bot_dice,bg,player,player)
        mcts = MCTS.MCTS(node,3,2000)
        valid_moves,distribution = mcts.generate_distribution()
        if not valid_moves == []:
            selected_move = None
            best_score = 0 
            for i in range(len(distribution)):
                if distribution[i]>best_score:
                    best_score=distribution[i]
                    selected_move=valid_moves[i]
            print("OPPONENT MOVES : ",selected_move)
            state = bg.make_move(state,player,[selected_move])
        else:
            print("NO MOVE AVAILABLE!")
    print(state)
    player*=-1

if -1*player == 1:
    print("BLACK WON!")
else:
    print("White WON!")