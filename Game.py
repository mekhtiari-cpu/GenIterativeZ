import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.hp = 100
        self.xp = 0
        self.level = 1
        self.inventory = []

    def attack(self):
        return random.randint(10, 20)

    def defend(self):
        return random.randint(5, 10)

class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(20, 50)

    def attack(self):
        return random.randint(5, 15)

def create_player():
    name = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        return Player(name, 'Warrior')
    elif choice == '2':
        return Player(name, 'Mage')
    elif choice == '3':
        return Player(name, 'Rogue')
    else:
        print("Invalid choice, defaulting to Warrior.")
        return Player(name, 'Warrior')

def explore_dungeon(player):
    encounters = ["monster", "treasure", "trap"]
    encounter = random.choice(encounters)
    if encounter == "monster":
        monster = Monster("Goblin")
        print(f"A wild {monster.name} appears!")
        fight_monster(player, monster)
    elif encounter == "treasure":
        print("You found a treasure chest! +10 XP")
        player.xp += 10
    elif encounter == "trap":
        print("You fell into a trap! -10 HP")
        player.hp -= 10

def fight_monster(player, monster):
    while monster.hp > 0 and player.hp > 0:
        print(f"Your HP: {player.hp}")
        print(f"{monster.name} HP: {monster.hp}")
        print("Choose an action:")
        print("1. Attack")
        print("2. Defend")
        action = input("Enter the number of your choice: ")
        
        if action == '1':
            damage = player.attack()
            monster.hp -= damage
            print(f"You dealt {damage} damage to the {monster.name}.")
        elif action == '2':
            defense = player.defend()
            print(f"You defended, reducing damage by {defense}.")
        else:
            print("Invalid action. The monster attacks!")
        
        if monster.hp > 0:
            damage = monster.attack()
            player.hp -= damage
            print(f"The {monster.name} dealt {damage} damage to you.")
    
    if player.hp > 0:
        print(f"You defeated the {monster.name}!")
        player.xp += 20
        if player.xp >= 50:
            player.level += 1
            player.xp = 0
            print("You leveled up! Level:", player.level)
    else:
        print("You died. Game over.")

def main():
    print("Welcome to the dungeon RPG!")
    player = create_player()
    while player.hp > 0:
        explore_dungeon(player)
        if input("Continue exploring? (y/n): ").lower() != 'y':
            break
    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()
