import random

balance = 0

for i in range(100000000):

#simulating 1,000,000 rounds for i in range (1,000,000)
# weights=[0.48, 0.52] means 48% chance of heads, 52% chance of tails
# this is the house edge hidden in the math

    flip = random.choices(["H", "T"], weights=[0.48, 0.52]) [0]

if flip == "H":
    balance += 20 #the payout looks fair...
    
else:
    balance -= 20 #... but the frequency is rigged
    
    #optional: print every 100,000th game to save processing time
    if(i + 1) % 100000 == 0:
        print(f"Game {i+1}: {flip}, Current Balance: {balance}")
        
print("-" * 30)
print("Final balance:", balance)            