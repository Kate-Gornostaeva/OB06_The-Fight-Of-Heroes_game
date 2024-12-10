# Попытка добавить орудие, но ак себе...

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None

    def choose_weapon(self):
        weapons = ["Меч", "Лук", "Щит"]
        print(f"{self.name} выбирает оружие ... {weapons}")
        while True:
            choice = input("Введите название оружия: ")
            if choice in weapons:
                self.weapon = choice
                print(f"{self.name} выбрал оружие {self.weapon}\n")
                break
            else:
                print("Неверный выбор. Меч, Лук или Щит?")

    def attack_damage(self, other):
        # Случайный урон от 5 до 20
        damage = random.randint(5, 20)

        if self.weapon == other.weapon:
            # Если оружие одинаковое, урон равен разнице сил удара
            damage = other.attack_damage - self.attack_damage  # Сила удара фиксирована на уровне 20
            return damage  # Убедимся, что урон не отрицательный
        elif (self.weapon == "Меч" and other.weapon == "Лук") or \
                (self.weapon == "Лук" and other.weapon == "Щит") or \
                (self.weapon == "Щит" and other.weapon == "Меч"):
            return damage  # Урон противнику
        else:
            return 0  # Если проиграл по типу оружия

    def attack(self, other):
        damage = self.attack_damage(other)
        other.health -= damage
        print(f"{self.name} атакует {other.name} с помощью {self.weapon}!\n" +
              f"Нанесен урон: {damage}. Остаток здоровья {other.name}: {other.health:.1f}\n")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def computer_choose_weapon(self):
        weapons = ['Меч', 'Лук', 'Щит']
        self.computer.weapon = random.choice(weapons)
        print(f"{self.computer.name} выбрал {self.computer.weapon}.\n")

    def start(self):
        print("Игра началась!")

        while self.player.is_alive() and self.computer.is_alive():
            # Игрок выбирает оружие
            self.player.choose_weapon()

            # Компьютер выбирает оружие
            self.computer_choose_weapon()

            # Игрок атакует компьютер
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Компьютер выбирает оружие для следующей атаки
            self.computer_choose_weapon()

            # Компьютер атакует игрока
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()