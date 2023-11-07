import numpy as np
import random

class State:
    def __init__(self) -> None:
        self.PointsContent = np.zeros((1,26)).astype(np.int32)[0]
        self.BlackCheckers = []
        self.WhiteCheckers = [] 
        self.BlackCheckersTaken = 0
        self.WhiteCheckersTaken = 0

        self.PointsContent[1] = +2
        self.PointsContent[12] = +5
        self.PointsContent[17] = +3 
        self.PointsContent[19] = +5

        self.PointsContent[6] = -5
        self.PointsContent[8] = -3
        self.PointsContent[13] = -5 
        self.PointsContent[24] = -2
        self.update_point_vectors()

    def is_pip_state(self):
        return self.BlackCheckers[1]>self.WhiteCheckers[1] and self.BlackCheckersTaken==0 and self.WhiteCheckersTaken==0

    def game_is_finished(self):
        self.update_point_vectors()

        if self.get_player_points(-1) ==[] or self.get_player_points(1) == []:
            return True 
        
        return False

    def can_take_off(self,player):
        if self.get_player_points(player) == []:
            return False

        if player>0:
            if self.BlackCheckersTaken==0 and self.get_player_points(player)[0]>18:
                return True
            else:
                return False
            
        if player<0:
            if self.WhiteCheckersTaken==0 and self.get_player_points(player)[0]<7:
                return True
            else:
                return False

    def get_points_taken(self,player):
        if player<0:
            return self.WhiteCheckersTaken
        else:
            return self.BlackCheckersTaken

    def get_player_points(self,player:int):
        self.update_point_vectors()
        player_points = []
        if player<0:
            if self.get_points_taken(player)==0:
                player_points=self.WhiteCheckers[1:]
            else:
                player_points = [25]
        else:
            if self.get_points_taken(player)==0:
                player_points=self.BlackCheckers[1:]
            else:
                player_points = [0]
        return player_points
    
    def get_randomized_player_points(self,player:int):
        player_points = self.get_player_points(player)
        if not player_points == []:
            random.shuffle(player_points)
        return player_points
    
    def copy(self):
        newState = State()
        newState.PointsContent = np.copy(self.PointsContent)
        newState.WhiteCheckers=[]
        newState.BlackCheckers=[]
        newState.update_point_vectors()
        newState.BlackCheckersTaken = self.BlackCheckersTaken
        newState.WhiteCheckersTaken = self.WhiteCheckersTaken
        return newState


    def update_point_vectors(self):
        self.BlackCheckers=[]
        self.WhiteCheckers=[]
        for i in range(1,25):
            if self.PointsContent[i]>0:
                self.BlackCheckers.append(i)
            if self.PointsContent[i]<0:
                self.WhiteCheckers.append(i)
        self.BlackCheckers = [len(self.BlackCheckers)] + sorted(self.BlackCheckers)
        self.WhiteCheckers = [len(self.WhiteCheckers)] + sorted(self.WhiteCheckers,reverse=True)



    def __eq__(self,other) -> bool:
        result = True
        if not (np.all(self.PointsContent == other.PointsContent) and self.BlackCheckersTaken==other.BlackCheckersTaken and self.WhiteCheckersTaken==other.WhiteCheckersTaken):
            result = False
        return result


    def __str__(self):
        result =  "_"*(13*3)+'\n'
        for i in  range(12,6,-1):
            result+=f"{i:^3}"
        result+='   '
        for i in range(6,0,-1):
            result+=f"{i:^3}"
        result+='\n'
        for i in range(5):
            for j in range(12,6,-1):
                if abs(self.PointsContent[j])>i:
                    if self.PointsContent[j]>0:
                        result+=' B '
                    else:
                        result+=' W '
                else:
                    result+='   '
            if self.WhiteCheckersTaken>i:
                result+='|W|'
            else:
                result+='| |'
            for j in range(6,0,-1):
                if abs(self.PointsContent[j])>i:
                    if self.PointsContent[j]>0:
                        result+=' B '
                    else:
                        result+=' W '
                else:
                    result+='   '
            result+='\n'
        for i in range(1):
            for j in range(12,6,-1):
                if abs(self.PointsContent[j])>5:
                    result+=f"+{abs(self.PointsContent[j])-5:^3}"
                else:
                    result+='   '
            if self.WhiteCheckersTaken>5:
                result+=f"{self.WhiteCheckersTaken-5:<2}"
            else:
                result+='  '
            for j in range(6,0,-1):
                if abs(self.PointsContent[j])>5:
                    result+=f"+{abs(self.PointsContent[j])-5:^3}"
                else:
                    result+='   '
            result+='\n'
        result +=  " "*(13*3)+'\n'
        result +=  " "*(13*3)+'\n'
        for i in range(1):
            for j in range(13,19):
                if abs(self.PointsContent[j])>5:
                    result+=f"+{abs(self.PointsContent[j])-5:^3}"
                else:
                    result+='   '
            if self.BlackCheckersTaken>5:
                result+=f"{self.BlackCheckersTaken-5:^3}"
            else:
                result+='   '
            for j in range(19,25):
                if abs(self.PointsContent[j])>5:
                    result+=f"+{abs(self.PointsContent[j])-5:^3}"
                else:
                    result+='   '
            result+='\n'
        for i in range(5):
            for j in range(13,19):
                if abs(self.PointsContent[j])>(4-i):
                    if self.PointsContent[j]>0:
                        result+=' B '
                    else:
                        result+=' W '
                else:
                    result+='   '
            if self.BlackCheckersTaken>(4-i):
                result+='|B|'
            else:
                result+='| |'
            for j in range(19,25):
                if abs(self.PointsContent[j])>(4-i):
                    if self.PointsContent[j]>0:
                        result+=' B '
                    else:
                        result+=' W '
                else:
                    result+='   '
            result+='\n' 
        for i in  range(13,19):
            result+=f"{i:^3}"
        result+='   '
        for i in range(19,25):
            result+=f"{i:^3}"
        result+='\n'
        result+=  "_"*(13*3)+'\n'
        return result