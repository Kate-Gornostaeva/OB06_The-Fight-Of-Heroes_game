#Как бы непллохо, но нет класса Game, поэтому смотри в main.py!!!

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.special_ability_used = False

    def attack(self, other):
        damage = random.randint(5, self.attack_power)  # Random damage from 5 to attack_power (20)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")


    def use_special_ability(self):
        if not self.special_ability_used:
            heal_amount = random.randint(5, 15)
            self.health += heal_amount
            self.special_ability_used = True
            print(f"{self.name} использует лечение и восстанавливает {heal_amount} здоровья!")
        else:
            print(f"{self.name} уже использовал лечение!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} ед.здоровья"


def player_turn(player, enemy):
    action = input("Выберите действие: 1 - Атаковать, 2 - Использовать лечение: ")
    if action == "1":
        player.attack(enemy)
    elif action == "2":
        player.use_special_ability()
    else:
        print("Неверный ввод. Попробуйте еще раз.")


def computer_turn(computer, player):
    if random.choice([True, False]) and not computer.special_ability_used:
        computer.use_special_ability()
    else:
        computer.attack(player)


def running_game():
    player_name = input("Введите имя вашего героя: ")
    print('Ваш герой может использовать лечение и восстановить часть своего здоровья. \nНо воспользоваться этой возможностью можно только один раз!')
    player = Hero(player_name)
    computer = Hero("Компьютер")

    while player.is_alive() and computer.is_alive():
        print("\nСтатусы:")
        print(player)
        print(computer)

        player_turn(player, computer)
        if computer.is_alive():
            computer_turn(computer, player)

    if player.is_alive():
        print(f"{player.name} победил!")
    else:
        print(f"{computer.name} победил!")


running_game()