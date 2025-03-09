
stuff = {'rope': 1, 'torch': 6,
         'gold coin': 42, 'dagger': 1,
         'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    d=dict(sorted(inventory.items()))
    #is this cheating?
    for k, v in d.items():
        print(v, k)
        item_total+=v
    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory: dict, loot: list):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item]+=1
    return inventory


displayInventory(stuff)
add_to_inventory(stuff, dragonLoot)
displayInventory(stuff)