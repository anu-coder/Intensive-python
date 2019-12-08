import random 

def monty_hall_sim(strategy, num_doors=3, n_iter=1000, prompt_user=False):
    
    # dictionary to store how many times user won
    res = {'win': 0, 'lose': 0}
    doors = range(1, num_doors + 1)
    
    for i in range(n_iter):
        user_choice = random.randint(1, num_doors)
        prize_door = random.randint(1, num_doors)
        rem_doors = [d for d in doors if d not in [user_choice, prize_door]]
        randi = random.randint(0, len(rem_doors) - 1)
        reveal_door = rem_doors[randi]
        
        if strategy == 'switch':
            del rem_doors[randi]
            rem_doors.append(prize_door)
             # Removing the revealed door from user_choices
            user_choice =  rem_doors[random.randint(0, len(rem_doors) - 1)]
            
        if user_choice == prize_door:
            res['win'] += 1
        else:
            res['lose'] += 1
            
            
    return(res['win']/n_iter)


print(monty_hall_sim('switch'))