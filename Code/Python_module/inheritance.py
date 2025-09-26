import datetime


class player:
    def __init__(self,fname,lname,birthyear):
        self.fname = fname
        self.lname = lname
        self.birthyear = birthyear

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birthyear

class TennisPlayer(player):
    def __init__(self,fname,lname,team,score,birthyear,runs,balls):
        super().__init__(fname,lname,birthyear)
        self.runs = runs
        self.balls = balls
        self.team = team
        self.score=score

class CricketPlayer(player):
    def __init__(self,fname,lname,team,score,birthyear):
        super().__init__(fname,lname,birthyear)
        self.team = team
        self.score=score

virat = CricketPlayer('Virat','Kohli','RCB',12000,1988)
print(f"Player: {virat.fname} {virat.lname}, Team: {virat.team}, Score: {virat.score}, Age: {virat.get_age()}")