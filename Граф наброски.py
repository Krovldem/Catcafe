import pygame
import random

class Dice:
    def __init__(self, quantity):
        self.quantity = quantity
        self.dice_images = [pygame.image.load('dice1.png'), pygame.image.load('dice2.png'), pygame.image.load('dice3.png'),
                            pygame.image.load('dice4.png'), pygame.image.load('dice5.png'), pygame.image.load('dice6.png')]
        self.dice_values = [1, 2, 3, 4, 5, 6]
        self.dice_positions = [(100, 100), (200, 100), (300, 100), (400, 100), (500, 100)]

    def roll(self):
        result = []
        for i in range(self.quantity):
            result.append(random.choice(self.dice_values))
        return result

    def increase_quantity(self, additional):
        self.quantity += additional

    def __repr__(self):
        return f"Dice(quantity={self.quantity})"


class GameSheet:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[' ' for _ in range(width)] for _ in range(height)]

    def draw_item(self, row, column, item):
        self.matrix[row][column] = item

    def display_sheet(self):
        for row in self.matrix:
            print(''.join(row))

class DrawingAction:
    def __init__(self, game_sheet, dice_values):
        self.game_sheet = game_sheet
        self.dice_values = dice_values

    def draw_item(self, item, tower_index):
        dice_value = self.dice_values[0]
        central_value = self.dice_values[1]

        position = (dice_value, tower_index)

        self.game_sheet.draw_item(position, item)

    def display_game_sheet(self):
        pass

    def check_cat_towers(self, players):
        cat_tower_indices = []  # Индексы башен, заполненные предметами
        for i in range(self.game_sheet.height):
            items_in_tower = [self.game_sheet.grid[j][i] for j in range(self.game_sheet.width)]
            if all(items_in_tower):  # Если все ячейки башни заполнены
                cat_tower_indices.append(i)

        for player in players:
            tower_values = [self.game_sheet.grid[j][i] for j in cat_tower_indices]  # Значения в заполненных башнях
            if 'КД' in tower_values:  # Если есть кошачий домик в башне
                max_value = max(tower_values)
                player.circle_number(max_value)  # Обводим большее число
            else:
                min_value = min(tower_values)
                player.circle_number(min_value)  # Обводим меньшее число

class Player:
    def __init__(self, name):
        self.name = name
        self.game_sheet = GameSheet()  # Создание игрового листа для каждого игрока
        self.points = 0

    def draw_item(self, row, column, item):
        self.game_sheet.place_item(row, column, item)  # Метод для размещения предмета на игровом листе

    def circle_number(self, number):
        self.game_sheet.circle_number(number)  # Метод для обводки числа на игровом листе

    def update_points(self, points):
        self.points += points  # Метод для обновления общего количества очков у игрока


# Example usage
pygame.init()
game_sheet = GameSheet(10, 10)  # Create a game sheet
dice_values = (3, 2)  # Example dice values
action = DrawingAction(game_sheet, dice_values)
action.draw_item('КД', 1)  # Draw a "Cat House" on the tower 1
action.draw_item('КН', 2)  # Draw a "Ball of Yarn" on the tower 2
action.display_game_sheet()  # Display the updated game sheet using pygame
