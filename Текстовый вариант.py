import random


class Player:
    def __init__(self, name, sheet):
        self.name = name
        self.sheet = sheet
        self.paws = 0

    def rolldice(self):
        return random.randint(1, 6)

    def choosedice(self, dice):
        chosendice = random.choice(dice)
        dice.remove(chosendice)
        return chosendice

    def draw(self, item, floor):
        if self.sheet[floor][item] == ".":
            self.sheet[floor][item] = str(item + 1)

    def skipturn(self):
        self.paws += 1

    def __repr__(self):
        return f"Player({self.name})"


class CatCafeGame:
    def __init__(self, players):
        self.players = players
        self.dice = [1, 2, 3, 4, 5]
        self.centraldice = None
        self.turn = 0

        self.sheet = [["." for _ in range(6)] for _ in range(6)]

    def nextturn(self):
        currentplayer = self.players[self.turn]
        print("Ход игрока:", currentplayer.name)

        nextdice = currentplayer.rolldice()
        currentdice = currentplayer.choosedice(self.dice)
        self.centraldice = self.dice[0]

        print("Выбранный игроком кубик:", currentdice)
        print("Случайный кубик:", nextdice)
        print("Центральный кубик:", self.centraldice)

        itemchoice = input("Введите номер предмета (1-6) для отметки на своем листе: ")
        floorchoice = input("Введите номер этажа (1-6): ")

        if itemchoice.isdigit() and floorchoice.isdigit():
            itemchoice = int(itemchoice)
            floorchoice = int(floorchoice)

            if 1 <= itemchoice <= 6 and 1 <= floorchoice <= 6:
                currentplayer.draw(itemchoice - 1, floorchoice - 1)
                self.dice.append(nextdice)
                self.turn = (self.turn + 1) % len(self.players)

                print("Ход передан следующему игроку.\n")
                self.printsheet()
                return

        currentplayer.skipturn()
        self.dice.append(nextdice)
        self.turn = (self.turn + 1) % len(self.players)

        print("Некорректный ввод или выбрана занятая ячейка. Пропуск хода.\n")
        self.printsheet()

    def printsheet(self):
        print("{:<10}{}".format("", " ".join(str(i + 1) for i in range(6))))
        for i, row in enumerate(self.sheet):
            items = " ".join([str(item) for item in row])
            print("{:<10}{}".format(i + 1, items))
        print()

    def __repr__(self):
        return f"CatCafeGame({self.players})"


# Создание игроков и игрового сеанса
player1 = Player("Игрок 1", [["." for _ in range(6)] for _ in range(6)])
player2 = Player("Игрок 2", [["." for _ in range(6)] for _ in range(6)])
players = [player1, player2]

game = CatCafeGame(players)

# Игровой цикл
while True:
    game.nextturn()