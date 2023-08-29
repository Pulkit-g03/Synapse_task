import random

class ChessPlayer:
    def __init__(self, player, age, elo, tenacity, isboring):
        self.player = player
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.isboring = isboring
        self.score = 0

    def __str__(self):
        return f"Player Name :{self.player}, Age:{self.age}, ELO:{self.elo}, Tenacity:{self.tenacity}, IsBoring:{self.isboring}"
    
players = [ChessPlayer("Courage the Cowardly Dog", 25,1000.39,1000,False), ChessPlayer("Princess Peach", 23, 945.65, 50, True),ChessPlayer("Walter White", 50, 1650.73, 750, False) ,ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False) ,ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True), ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)]


def simulateMatch(player_1,player_2): 
    
    elo_difference = abs(player_1.elo - player_2.elo)
    if elo_difference > 100:
        player_1.score += 1
    else:
        player_2.score +=1

    if elo_difference>=50 and elo_difference<=100:
        random_factor = int(random.randint(1,10)) 
        Lower_elo= player_1.tenacity if player_1.elo < player_2.elo else player_2.tenacity
        Higher_elo = player_1.tenacity if player_1.elo > player_2.elo else player_2.tenacity

        win = random_factor*Lower_elo

        if win>Higher_elo:
            Lower_elo +=1
        else:
           Higher_elo +=1

    elif elo_difference < 50:
        if player_1.tenacity > player_1.tenacity:
            player_1.score +=1
        else:
            player_2.score +=1
    if player_1.isboring =='True' or player_2.isboring == 'True' and elo_difference<100 :
        player_1.score +=0.5
        player_2.score +=0.5

for i in range (0,5):
    for j in range (i+1,5):
        simulateMatch(players[i], players[j])
        simulateMatch(players[j], players[i])

for p in players:
    print(p.player,p.score)
