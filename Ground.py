import sys
import pygame as pg

objects = []

pg.init()

screen_width, screen_height = 500, 730

FPS = 24 # frame per second
clock = pg.time.Clock()

# изображения
bg_img = pg.image.load('src/PlayField_cut.png')
icon_img = pg.image.load('src/icon.png')

display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('КотоКафе')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/HARLOWSI.TTF', 48)


# display.fill('blue', (0, 0, screen_width, screen_height))
display.blit(bg_img, (0, 0))  # image.tr


def display_redraw():
    display.blit(bg_img, (0, 0))
    # display.blit(player_img, (player_x, player_y))
    pg.display.update()

def item_model(player_x, player_dx, screen_width, player_width):
    player_x += player_dx
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width
    return player_x


class Button():
    def __init__(self, x, y, screen_width, screen_height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pg.Surface((self.screen_width, self.screen_height))
        self.buttonRect = pg.Rect(self.x, self.y, self.screen_width, self.screen_height)

        self.buttonSurf = font.render(buttonText, True, (8, 8, 8))
        objects.append(self)

    def process(self):
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        display.blit(self.buttonSurface, self.buttonRect)

def event_processing():
    running = True
    for event in pg.event.get():
        # нажали крестик на окне
        if event.type == pg.QUIT:
            running = False
        # тут нажимаем на клавиши
        if event.type == pg.KEYDOWN:
            # нажали на q - quit
            if event.key == pg.K_q:
                running = False        # # движение игрока
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_a or event.key == pg.K_LEFT:
        #         player_dx = -player_velocity
        #     if event.key == pg.K_d or event.key == pg.K_RIGHT:
        #         player_dx = player_velocity
        # if event.type == pg.KEYUP:
        #     player_dx = 0
    clock.tick(FPS)
    return running

def myFunction():
    print('Button Pressed')

Button(55, 550, 55, 40, 'Button One (onePress)', myFunction)


running = True
while running:
    for object in objects:
        object.process()
    pg.display.flip()
    clock.tick(FPS)
    display_redraw()
    running = event_processing()

pg.quit()
