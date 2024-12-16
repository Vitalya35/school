class Character:
    """Родительсктй класс"""
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} attacks {other.name} и наносит {damage}")

class Hero(Character):
    def __init__(self, name, health, attack_power, special_power):
        super().__init__(name, health, attack_power)
        self.special_power = special_power
        self.special_used = False

    def special_attack(self, other):
        if self.special_used == False:
            other.health -= self.attack_power + self.special_power
            self.special_used = True
            print(f"!!!!!!!{self.name} attacks специальной аттакой {other.name}")
        else:
            print(f"!!!!!!!!!!!!{self.name} уже использовал специальную аттаку")

class Monster(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def roar(self):
        print(f"{self.name} издаёт страшные звуки")

def game():
    hero = Hero("Name",100,15,30)
    monster = Monster("Utopec",100,15)

    print("!!Игра началась!!")

    monster.roar()

    while hero.is_alive() and monster.is_alive():
        print("\nВыберите действие:")
        print("1. Аттака")
        print("2. Супер Аттака")

        action = input("Ваш выбор: ")

        if action == "1":
            hero.attack(monster)
        elif action == "2":
            hero.special_attack(monster)
        else:
            print("Не удачное движение")

        if monster.is_alive():
            monster.attack(hero)
        else:
            print(f"{monster.name} повержен!")
        print(f"Здоровье {hero.name} {hero.health}")
        print(f"Здоровье {monster.name} {monster.health}")

    if hero.is_alive():
        print("Поздравляем!")
    else:
        print("вы проиграли:(")


if __name__ == "__main__":
    game()