import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)  # Метод для броска кубика

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0  # Инициализация счёта игрока

    def update_score(self, points):
        self.score += points  # Метод для обновления счёта игрока


class CatTowersGame:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [['.' for _ in range(columns)] for _ in range(rows)]  # Создание игрового поля
        self.filled_columns = 0  # Инициализация переменной для отслеживания заполненных столбцов

    def print_board(self):
        for row in self.board:
            print(" ".join(row))  # Вывод игрового поля на экран

    def place_item(self, column):
        if self.filled_columns < 3:  # Проверка, что ещё не заполнено 3 столбца
            item = self.get_input()  # Получение числа от игрока
            for i in range(self.rows - 1, -1, -1):  # Начинать с нижней строки и идти вверх
                if self.board[i][column] == '.':
                    self.board[i][column] = item  # Размещение элемента на игровом поле
                    if i == 0:  # Если элемент размещён в самом верхнем ряду
                        self.filled_columns += 1  # Увеличение счетчика заполненных столбцов
                    break
        else:
            print("Все 3 столбца уже заполнены!")

    def get_input(self):
        return input("Введите число: ")  # Запрос ввода числа у игрока

# Пример использования
game = CatTowersGame(6, 5)  # Создание игры с игровым полем 6x5

while game.filled_columns < 3:  # Цикл повторяется, пока не заполнится 3 столбца
    game.print_board()  # Вывод игрового поля на экран
    column = int(input("Выберите столбец для размещения числа (от 0 до 4): "))  # Получение выбора столбца от игрока
    if 0 <= column < 5:
        game.place_item(column)  # Размещение числа в выбранном столбце
    else:
        print("Недопустимый выбор столбца! Попробуйте ещё раз.")

game.print_board()  # Вывод окончательного состояния игрового поля на экран

# Пример использования
dice = Dice()  # Создание кубика
player1 = Player("Player 1")  # Создание игрока
player1.update_score(dice.roll())  # Обновление счёта игрока после броска кубика
print(f"{player1.name}'s score is {player1.score}")  # Вывод счёта игрока
