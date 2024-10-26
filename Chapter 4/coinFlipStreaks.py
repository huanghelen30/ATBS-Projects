# Determine how often a streak of six tails will come up out of 100 coin flips in a randomly generated list of heads and tails
import random
numberOfStreaks = 0

for experimentNumber in range(10000): 
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
       if random.randint(0,1):
        flips.append('H')
       else:
        flips.append('T')
    
    print(''.join(flips))
    

    # Code that checks if there is a streak of 6 heads or tails in a row 
    for i in range(100 - 6):
        if flips[i] == flips[i+1] == flips[i+2] == flips[i+3] == flips[i+4] == flips[i+5]:
            numberOfStreaks += 1
            break

print('Change of streak: %.2f%%' % (numberOfStreaks / 100))
