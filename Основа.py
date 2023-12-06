import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name, sheet):  # конструктор класса для создания игрока
        self.name = name  # имя игрока
        self.sheet = sheet  # лист для отметок игрока
        self.paws = 0  # количество пропущенных ходов игрока

    def draw(self, item, floor):  # метод для отметки на листе игрока
        if self.sheet[floor][item] == ".":
            self.sheet[floor][item] = str(item + 1)  # отмечаем предмет на листе игрока

    def skip_turn(self):  # метод для пропуска хода игрока
        self.paws += 1  # увеличиваем количество пропущенных ходов игрока

    def __repr__(self):  # метод для представления объекта класса в виде строки
        return f"Player({self.name})"

class CatCafeGame:
    def __init__(self, players):  # конструктор класса для создания игры
        self.players = players  # список игроков
        self.dice = Dice()  # начальный набор игральных костей
        self.central_dice = None  # центральная кость, которую можно выбрать
        self.turn = 0  # номер текущего хода

        self.sheet = [["." for _ in range(6)] for _ in range(6)]  # игровое поле каждого игрока

    def next_turn(self):  # метод для выполнения следующего хода в игре
        current_player = self.players[self.turn]  # текущий игрок
        print("Ход игрока:", current_player.name)  # отображаем имя текущего игрока

        next_dice = self.Dice.pop(0)  # вытаскиваем следующий случайный кубик из общего пула
        current_dice = self.dice.roll()  # выбираем центральный кубик
        self.central_dice = current_dice  # записываем в центральный кубик

        print("Выбранный игроком кубик:", current_dice)  # отображаем выбранный игроком кубик
        print("Случайный кубик:", next_dice)  # отображаем случайный кубик
        print("Центральный кубик:", self.central_dice)  # отображаем центральный кубик

        # Игрок вводит номер предмета и этажа
        item_choice = input("Введите номер предмета (1-6) для отметки на своем листе: ")
        floor_choice = input("Введите номер этажа (1-6): ")

        # Обработка ввода игрока
        if item_choice.isdigit() and floor_choice.isdigit():
            item_choice = int(item_choice)
            floor_choice = int(floor_choice)

            # Если введены корректные значения
            if 1 <= item_choice <= 6 and 1 <= floor_choice <= 6:
                current_player.draw(item_choice - 1, floor_choice - 1)  # отмечаем предмет на листе игрока
                self.dice.append(next_dice)  # добавляем следующий кубик обратно в пул
                self.turn = (self.turn + 1) % len(self.players)  # переходим к следующему игроку

                print("Ход передан следующему игроку.\n")
                self.print_sheet()  # отображаем игровое поле
                return

        current_player.skip_turn()  # игрок пропускает ход
        self.dice.append(next_dice)  # добавляем следующий кубик обратно в пул
        self.turn = (self.turn + 1) % len(self.players)  # переходим к следующему игроку

        print("Некорректный ввод или выбрана занятая ячейка. Пропуск хода.\n")
        self.print_sheet()  # отображаем игровое поле

    def print_sheet(self):  # метод для отображения игрового поля
        print("{:<10}{}".format("", " ".join(str(i + 1) for i in range(6))))
        for i, row in enumerate(self.sheet):
            items = " ".join([str(item) for item in row])
            print("{:<10}{}".format(i + 1, items))
        print()

    def __repr__(self):  # метод для представления объекта класса в виде строки
        return f"CatCafeGame({self.players})"


# Создание игроков и начало игрового сеанса
player1 = Player("Игрок 1", [["." for _ in range(6)] for _ in range(6)])
player2 = Player("Игрок 2", [["." for _ in range(6)] for _ in range(6)])
players = [player1, player2]

game = CatCafeGame(players)

# Игровой цикл
while True:
    game.next_turn()  # выполнение следующего хода
