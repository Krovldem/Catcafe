import pygame as pg

pg.init()

screen_width, screen_height = 500,800

FPS = 24    # frame per second
clock = pg.time.Clock()

# изображения
bg_img = pg.image.load('PlayField.png')
icon_img = pg.image.load('icon.png')

display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('КотоКафе')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('HARLOWSI.TTF', 48)

# display.fill('blue', (0, 0, screen_width, screen_height))
display.blit(bg_img, (0, 0))        # image.tr

text_img = sys_font.render('Score 123', True, 'white')
# display.blit(text_img, (100, 50))

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()
# display.blit(game_over_text, (screen_width/2 - w/2, screen_height / 2 - h/2))

def display_redraw():
    display.blit(bg_img, (0, 0))
    pg.display.update()

def event_processing():
    running = True
    clock.tick(FPS)
    return running


running = True
while running:
    display_redraw()
    running = event_processing()

pg.quit()

