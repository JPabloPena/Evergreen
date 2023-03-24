# -*- coding: utf-8 -*-
class DisplayScoreResult:
    NULL: str = ""
    SEPARATOR: str = "-"
    LOVE: str = "Love"
    FIFTEEN: str = "Fifteen"
    THIRTY: str = "Thirty"
    FORTY: str = "Forty"
    DEUCE: str = "Deuce"
    ADVANTAGE: str = "Advantage "
    WIN: str = "Win for "
    TIE: dict = {
        0: LOVE+"-All",
        1: FIFTEEN+"-All",
        2: THIRTY+"-All",
    }
    NOT_TIE: dict = {
        0: LOVE,
        1: FIFTEEN,
        2: THIRTY,
        3: FORTY,
    }


class TennisGame1:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0
        self.result = DisplayScoreResult.NULL

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if (self.p1points == self.p2points):
            self.result = DisplayScoreResult.TIE.get(self.p1points, DisplayScoreResult.DEUCE)
        elif (self.p1points >= 4 or self.p2points >= 4):
            minus_result = self.p1points-self.p2points
            self.score_greater_than_4(minus_result)
        else:
            self.score_two_different_results()
        return self.result
    
    def score_two_different_results(self):
        result_p1 = DisplayScoreResult.NOT_TIE[self.p1points]
        result_p2 = DisplayScoreResult.NOT_TIE[self.p2points]
        self.result = result_p1 + DisplayScoreResult.SEPARATOR + result_p2

    def score_greater_than_4(self, minus_result):
        if (minus_result == 1):
            self.result = DisplayScoreResult.ADVANTAGE + self.player1_name
        elif (minus_result == -1):
            self.result = DisplayScoreResult.ADVANTAGE + self.player2_name
        elif (minus_result >= 2):
            self.result = DisplayScoreResult.WIN + self.player1_name
        else:
            self.result = DisplayScoreResult.WIN + self.player2_name


# class TennisGame2:
#     def __init__(self, player1_name, player2_name):
#         self.player1_name = player1_name
#         self.player2_name = player2_name
#         self.p1points = 0
#         self.p2points = 0

#     def won_point(self, player_name):
#         if player_name == self.player1_name:
#             self.P1Score()
#         else:
#             self.P2Score()

#     def score(self):
#         self.result = ""
#         if (self.p1points == self.p2points and self.p1points < 3):
#             if (self.p1points==0):
#                 self.result = "Love"
#             if (self.p1points==1):
#                 self.result = "Fifteen"
#             if (self.p1points==2):
#                 self.result = "Thirty"
#             self.result += "-All"
#         if (self.p1points==self.p2points and self.p1points>2):
#             self.result = "Deuce"

#         P1res = ""
#         P2res = ""
#         if (self.p1points > 0 and self.p2points==0):
#             if (self.p1points==1):
#                 P1res = "Fifteen"
#             if (self.p1points==2):
#                 P1res = "Thirty"
#             if (self.p1points==3):
#                 P1res = "Forty"

#             P2res = "Love"
#             self.result = P1res + "-" + P2res
#         if (self.p2points > 0 and self.p1points==0):
#             if (self.p2points==1):
#                 P2res = "Fifteen"
#             if (self.p2points==2):
#                 P2res = "Thirty"
#             if (self.p2points==3):
#                 P2res = "Forty"

#             P1res = "Love"
#             self.result = P1res + "-" + P2res


#         if (self.p1points>self.p2points and self.p1points < 4):
#             if (self.p1points==2):
#                 P1res="Thirty"
#             if (self.p1points==3):
#                 P1res="Forty"
#             if (self.p2points==1):
#                 P2res="Fifteen"
#             if (self.p2points==2):
#                 P2res="Thirty"
#             self.result = P1res + "-" + P2res
#         if (self.p2points>self.p1points and self.p2points < 4):
#             if (self.p2points==2):
#                 P2res="Thirty"
#             if (self.p2points==3):
#                 P2res="Forty"
#             if (self.p1points==1):
#                 P1res="Fifteen"
#             if (self.p1points==2):
#                 P1res="Thirty"
#             self.result = P1res + "-" + P2res

#         if (self.p1points > self.p2points and self.p2points >= 3):
#             self.result = "Advantage " + self.player1_name

#         if (self.p2points > self.p1points and self.p1points >= 3):
#             self.result = "Advantage " + self.player2_name

#         if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
#             self.result = "Win for " + self.player1_name
#         if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
#             self.result = "Win for " + self.player2_name
#         return self.result

#     def SetP1Score(self, number):
#         for i in range(number):
#             self.P1Score()

#     def SetP2Score(self, number):
#         for i in range(number):
#             self.P2Score()

#     def P1Score(self):
#         self.p1points +=1


#     def P2Score(self):
#         self.p2points +=1

# class TennisGame3:
#     def __init__(self, player1_name, player2_name):
#         self.p1N = player1_name
#         self.p2N = player2_name
#         self.p1 = 0
#         self.p2 = 0

#     def won_point(self, n):
#         if n == self.p1N:
#             self.p1 += 1
#         else:
#             self.p2 += 1

#     def score(self):
#         if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
#             p = ["Love", "Fifteen", "Thirty", "Forty"]
#             s = p[self.p1]
#             return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
#         else:
#             if (self.p1 == self.p2):
#                 return "Deuce"
#             s = self.p1N if self.p1 > self.p2 else self.p2N
#             return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
