import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f'{self.name} атакует {other.name} и наносит {damage} урона!')

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print('Игра началась!')
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                break
            self.computer_turn()

        self.display_winner()

    def player_turn(self):
        action = input('Ваш ход! Нажмите Enter, чтобы атаковать: ')
        if action == "":
            self.player.attack(self.computer)
            self.display_health()

    def computer_turn(self):
        print('Ход компьютера!')
        self.computer.attack(self.player)
        self.display_health()

    def display_health(self):
        print(f'{self.player.name} здоровье: {self.player.health}')
        print(f'{self.computer.name} здоровье: {self.computer.health}')

    def display_winner(self):
        if self.player.is_alive():
            print(f'{self.player.name} победил!')
        else:
            print(f'{self.computer.name} победил!')

if __name__ == "__main__":
    player_name = input('Введите имя вашего героя: ')
    game = Game(player_name)
    game.start()