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

# Objects
home_img = pg.image.load('src/home.png')
home_width, home_height = home_img.get_size()
home_gap = 10
home_velocity = 10
# home_dx = 0
home_x = screen_width / 2 - home_width / 2
home_y = screen_height - home_height - home_gap

ball_img = pg.image.load('src/ball.png')
ball_width, ball_height = ball_img.get_size()
ball_gap = 10
ball_velocity = 10
ball_dx = 0
ball_x = screen_width / 2 - ball_width / 2
ball_y = screen_height - ball_height - ball_gap

butterfly_img = pg.image.load('src/butterfly.png')
butterfly_width, butterfly_height = butterfly_img.get_size()
butterfly_gap = 10
butterfly_velocity = 10
butterfly_dx = 0
butterfly_x = screen_width / 2 - butterfly_width / 2
butterfly_y = screen_height - butterfly_height - butterfly_gap

cup_img = pg.image.load('src/cup.png')
cup_width, cup_height = cup_img.get_size()
cup_gap = 10
cup_velocity = 10
cup_dx = 0
cup_x = screen_width / 2 - cup_width / 2
cup_y = screen_height - cup_height - cup_gap

pillow_img = pg.image.load('src/pillow.png')
pillow_width, pillow_height = pillow_img.get_size()
pillow_gap = 10
pillow_velocity = 10
pillow_dx = 0
pillow_x = screen_width / 2 - pillow_width / 2
pillow_y = screen_height - pillow_height - pillow_gap

mouse_img = pg.image.load('src/mouse.png')
mouse_width, mouse_height = mouse_img.get_size()
mouse_gap = 10
mouse_velocity = 10
mouse_dx = 0
mouse_x = screen_width / 2 - mouse_width / 2
mouse_y = screen_height - mouse_height - mouse_gap
