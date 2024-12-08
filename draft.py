# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.weapon = None


    def choose_weapon(self):
        weapons = ["Меч", "Лук", "Щит"]
        print(f"{self.name} выбирает оружие ... {weapons}")
        while True:
            choice = input("  ")
            if choice in weapons:
                self.weapon = choice
                print(f"{self.name} выбрал оружие {self.weapon}\n")
                break
            else:
                print("Неверный выбор. Меч, Лук или Щит?")

    def attack_damage(self, other):
        if self.weapon == other.weapon:
            damage = self.attack_power - other.attack_power
            return damage
        elif self.weapon == "Меч" and other.weapon == "Лук":
            damage = self.attack_power
            print(f"Меч побеждает Лук. Урон {damage}")
            return damage
        elif self.weapon == "Лук" and other.weapon == "Щит":
            damage = self.attack_power
            print(f"Лук побеждает Щит. Урон {damage}")
            return damage
        elif self.weapon == "Щит" and other.weapon == "Меч":
            damage = self.attack_power
            print(f"Щит защитил от Меча. Урон {damage}")
            return damage
        else:
            damage = 0
            return damage


    def attack(self, other):
        self.attack_power = random.randint(5, 20)
        damage = self.attack_damage(other)
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name}!\n {other.name} нанесен урон {self.attack_power}.\nОстаток здоровья {other.health}\n")


    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def computer_choose_weapon(self):
        weapons = ['Меч', 'Лук', 'Щит']
        self.computer.weapon = random.choice(weapons)
        print(f"{self.computer.name} выбрал {self.computer.weapon}.")

    def start(self):
        print("Игра началась!")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.choose_weapon()
            self.computer_choose_weapon()
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"{self.computer.name} осталось здоровья: {self.computer.health:.1f}")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"{self.player.name} осталось здоровья: {self.player.health:.1f}")



player_name = input("Введите имя вашего героя: ")
game = Game(player_name)
game.start()





