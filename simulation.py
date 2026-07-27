#so in this code i am trying to simulate an environment where i am using quant in finance, buying and selling
# almost like the casino simulations from before

import random

# Parameters
ticket_cost = 20
payout = 35
p = 0.5

num_simulations = 15        #number of blocks
plays_per_sim = 1000        #plays per block

initial_balance = 0

balance = initial_balance
results = []

for sim in range(num_simulations):
    for _ in range(plays_per_sim):
        if random.random() < p:     #head(win)
            balance += (payout - ticket_cost)
        else:       #loss
            balance -= ticket_cost
            
    results.append(balance)
    
# output results
for i, bal in enumerate(results):
    print(f"After simulation {i+1}: {bal}")
    
print("\nFinal balance:", balance)            