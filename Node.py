import State
import Dice 
import Backgammon
import numpy as np
import math

class Node:
    def __init__(self,parent,state:State.State,dice:Dice.Dice,bg:Backgammon.Backgammon,player:int,root_player:int) -> None:
        self.parent = parent
        self.state = state
        self.dice = dice 
        self.dice.roll()
        self.bg = bg 
        self.player = player 
        self.children = [] 
        self.children_moves = []
        self.valid_moves = self.bg.get_all_valid_moves(self.state,self.player,self.dice)
        self.children_moves = list(self.valid_moves)
        self.root_player = root_player
        self.wins = 0
        self.visits =0

    def get_root(self):
        if self.parent is None:
            return self 
        else:
            return self.parent.get_root()

    def compute_UCB(self,c:int):
        return self.wins/self.visits + c * math.sqrt(math.log(self.get_root().visits)/self.visits)

    def select(self,c:int):
        if not self.is_fully_expanded():
            return self
        else:
            max_ucb = 0
            max_index = 0
            changed = False 
            for i in range(len(self.children)):
                ucb = self.children[i].compute_UCB(c)
                if ucb>max_ucb:
                    max_ucb=ucb 
                    max_index=i
                    changed=True 
            if not changed:
                return self
            return self.children[max_index].select(c)

    def expand(self):
        if not self.valid_moves == []:
            move = self.valid_moves[0]
            self.valid_moves = self.valid_moves[1:]
            new_dice = Dice.Dice()
            new_node = Node(self,self.bg.make_move(self.state,self.player,[move]),new_dice,self.bg,-1*self.player,self.root_player)
            self.children.append(new_node)

    def is_leaf_node(self):
        return self.children == []

    def is_fully_expanded(self):
        return self.valid_moves == []

    def backprop(self,increment:int):
        if self.parent is not None:
            self.parent.wins +=increment
            self.parent.visits +=1
            self.parent.backprop(increment)

    def simulate(self):

        player = self.player
        while not self.state.game_is_finished():
            if self.player*player==1:
                valid_moves = self.bg.get_all_valid_moves(self.state,player,self.dice)
                if not valid_moves == []:
                    random_choice = np.random.choice(len(valid_moves))
                    move = valid_moves[random_choice]
                    self.state = self.bg.make_move(self.state,player,[move])
            elif self.player*player==-1:
                valid_moves = self.bg.get_all_valid_moves(self.state,player,self.dice)
                if not valid_moves == []:
                    random_choice = np.random.choice(len(valid_moves))
                    move = valid_moves[random_choice]
                    self.state = self.bg.make_move(self.state,player,[move])
            self.dice.roll()
            player*=-1
        if -1*player == self.root_player:
            self.wins +=1
            self.visits +=1
            self.backprop(1)
        else:
            self.visits +=1
            self.backprop(0)

