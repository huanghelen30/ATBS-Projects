# Write some bots who play the game of Zombie Dice to see how they compare against other bots
import zombiedice, random

# Bot that randomly decides if it will continue or stop after the first roll
class RandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if random.randint(0,1) == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# Bot that stops rolling after it has two brains
class TwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else: 
                break

# Bot that stops rolling after it has two shotguns
class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()        
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['brains']
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# Bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns:
class RandomOneToFourZombie:
       def __init__(self, name):
           self.name = name
        
       def turn(self, gameState):
           rollMax = random.randint(0,3)
           rollNumber = 0
           diceRollResults = zombiedice.roll()
           shotguns = 0
           while diceRollResults is not None:
            rollNumber += 1
            shotguns += diceRollResults['shotgun']
            if rollNumber == rollMax or shotguns < 2:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

# Bot that stops rolling after it has rolled more shotguns than brains
class MoreShotgunsThanBrainsZombie:
        def __init__(self, name):
            self.name = name
        
        def turn(self, gameState):
            diceRollResults = zombiedice.roll()
            shotguns = 0
            brains = 0
            while diceRollResults is not None:
                shotguns += diceRollResults['shotgun']
                brains += diceRollResults['brains']
                if shotguns > brains:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    RandomZombie(name='Random'),
    TwoBrainsZombie(name='Two Brains Zombie'),
    TwoShotgunsZombie(name='Two Shotguns Zombie'),
    RandomOneToFourZombie(name='Random Roll from 1 to 4 Zombie'),
    MoreShotgunsThanBrainsZombie(name='More Shotguns Than Brains Zombie'),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)