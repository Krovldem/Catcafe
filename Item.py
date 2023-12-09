class Item:

    def scores(self):
        if self.name == 'Дом':
            return 1
        elif self.name == 'Клубочек':
            return 2
        elif self.name == 'Бабочка':
            return 3
        elif self.name == 'Корм':
            return 4
        elif self.name == 'Подушка':
            return 5
        elif self.name == 'Мышка':
            return 6

    def __init__(self, name: str):
        self.name = name


dice={
        1: Item('Дом'),
        2: Item('Клубочек'),
        3: Item('Бабочка'),
        4: Item('Корм'),
        5: Item('Подушка'),
        6: Item('Мышка')
        }