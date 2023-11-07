import State 
import Dice 


class Backgammon:
    
    def make_move(self,original_state:State.State,player,moves):
        state = original_state.copy()
        state.update_point_vectors()
        for st in moves:
            for move in st:
                player_checkers_out = state.get_points_taken(player)
                if move == [0,0]:
                    continue
                if move[0]+player*move[1] <25 and move[0]+player*move[1] > 0 :
                    state.PointsContent[move[0]+player*move[1]]+=1*player
                    if state.PointsContent[move[0]+player*move[1]] == 0 :
                        state.PointsContent[move[0]+player*move[1]]+=1*player
                        if player>0:
                            state.WhiteCheckersTaken+=1
                        else:
                            state.BlackCheckersTaken+=1

                if player_checkers_out == 0 :
                    state.PointsContent[move[0]]+=-1*player
                else:
                    if player>0:
                        state.BlackCheckersTaken-=1
                    else:
                        state.WhiteCheckersTaken-=1
                state.update_point_vectors()
        return state    
    
    def is_valid_move(self,original_state:State.State,player,move):
        state = original_state.copy()
        opponent_points = None 
        player_points = None
        player_taken_points = state.get_points_taken(player)
        if player>0:
            player_points=state.BlackCheckers[1:]
            opponent_points=state.WhiteCheckers[1:]
        else:
            player_points=state.WhiteCheckers[1:]
            opponent_points=state.BlackCheckers[1:]
        
        if player <0 and move[0] + player*move[1] <1 and player_points[0]>6:
            return False 
        if player >0 and  move[0] + player*move[1] >24 and player_points[0]<19:
            return False
        if player_taken_points>0:
            if player>0 and move[0]!=0:
                return False 
            elif player<0 and move[0]!=25:
                return False
        if (move[0] + player*move[1] not in opponent_points or abs(state.PointsContent[move[0] + player*move[1]])==1):
            return True 
        return False
    
    def valid_move_generator(self,original_state,player_points,player,die):
        if original_state.game_is_finished():
            yield original_state,[0,0]
        for point in player_points:
            state = original_state.copy()
            if state.can_take_off(player):
                if player>0:
                    player_points = state.get_player_points(player)
                    if 25-die in player_points:
                        yield self.make_move(state,player,[[[25-die,die]]]),[25-die,die]
                    else:
                        yield self.make_move(state,player,[[[player_points[0],die]]]),[player_points[0],die]
                elif player<0:
                    player_points = state.get_player_points(player)
                    if die in player_points:
                        yield self.make_move(state,player,[[[die,die]]]),[die,die]
                    else:
                        yield self.make_move(state,player,[[[player_points[0],die]]]),[player_points[0],die]

            else:
                if self.is_valid_move(state,player,[point,die]):
                    yield self.make_move(state,player,[[(point,die)]]),[point,die]

    def get_all_valid_moves(self,original_state,player,dice):
        global line 
        global line1
        global line2
        global line3
        global line4 
        max_double_dice_length = 20
        line = []
        moves=[]
        if not dice.is_double():
            for ln in [sorted(dice.result,reverse=False) , sorted(dice.result,reverse=True)]:
                for state,move in self.valid_move_generator(original_state,original_state.get_randomized_player_points(player),player,ln[0]):
                    line = [move]
                    moves.append(line)
                    if len(moves)>max_double_dice_length:
                        break
                    for state_inner,next_move in self.valid_move_generator(state,state.get_randomized_player_points(player),player,ln[1]):
                        line.append(next_move)
                        line = [move] 
                        moves.append(line)
                        if len(moves)>max_double_dice_length:
                            break
        else:
            
            for state1,move1 in self.valid_move_generator(original_state,original_state.get_randomized_player_points(player),player,dice.result[0]):
                line1 = [move1]
                moves.append(line1)
                if len(moves)>max_double_dice_length:
                    break
                for state2,move2 in self.valid_move_generator(state1,state1.get_randomized_player_points(player),player,dice.result[1]):
                    line2 = [move1,move2]
                    moves.append(line2)
                    if len(moves)>max_double_dice_length:
                        break
                    for state3,move3 in self.valid_move_generator(state2,state2.get_randomized_player_points(player),player,dice.result[2]):
                        line3 = [move1,move2,move3]
                        moves.append(line3)
                        if len(moves)>max_double_dice_length:
                            break
                        for state4,move4 in self.valid_move_generator(state3,state3.get_randomized_player_points(player),player,dice.result[3]):
                            line4 = [move1,move2,move3,move4]
                            moves.append(line4)
                            if len(moves)>max_double_dice_length:
                                break
        max_length = 0
        result = []
        for move in moves:
            if len(move)>max_length:
                max_length = len(move)
        for move in moves:
            if len(move) == max_length:
                result.append(move)
        moves = result
        result = []
        if moves != []:
            result = [moves[0]]
            for i  in range(len(moves)):
                flag = False
                for move in result:
                    if self.make_move(original_state,player,[move]) == self.make_move(original_state,player,[moves[i]]):
                        flag=True 
                if not flag:
                    result.append(moves[i])
        return result
    
