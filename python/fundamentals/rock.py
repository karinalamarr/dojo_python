
import random
choices = ["scissors", "paper", "rock"]
choice = random.choice(choices)

def rps(p1, comp):
    results = {
        "rock" : {"rock" : "tie", "paper" : "lose" , "scissors" : "win"},
        "paper" : {"rock" : "win", "paper" : "tie" , "scissors" : "lose"},
        "scissors" : {"rock" : "lose", "paper" : "win" , "scissors" : "tie"},
    }
    return results[p1][comp]
print(rps("rock", choice))
    










