import random

balance = 0
results = []

for i in range(30):
    flip = random.choice(['H', 'T'])
    
    if flip == 'H':
    balance += 10
    else:
    balance -= 1
    
    results.append(balance)

print(results)
print("Final balance:", balance)