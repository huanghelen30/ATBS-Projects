# Display a fantasy game inventory detailing how many of that item the player has
import pprint

stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, amount in inventory.items():
        print(str(amount) + ' ' + item) # Print the item and its amount
        item_total += amount
            
    print("Total number of items:" + str(item_total))

displayInventory(stuff)


#Add a function that returns a dictionary that represents the updated inventory from dragonLoot

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)