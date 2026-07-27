import random

balance = 0

for i in range(1000000):
    flip = random.choice(["H", "T"])
    
    if flip == "H": 
        balance +=30
    else:
        balance -=20
        
    print(f"Game {i+1}: {flip}, Balance: {balance}")
    
print("Final balance:", balance)        
    
    
    
    

    
    
    
