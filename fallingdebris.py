import pygame as pg
import random, time
pg.init()
clock = pg.time.Clock()

white = (255, 255, 255)

win_width = 800
win_height = 600
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('Falling Debris')

font = pg.font.Font(None, 30)
speed = 10
score = 0
lives=3
player_size = 80
player_pos = [win_width / 2, win_height - player_size]  # 400, 600-40
player_image = pg.image.load('C:/MyFiles/pyproj/pygame_env/TNS/TNS-02/jar')
player_image = pg.transform.scale(player_image, (player_size, player_size))  # 40,40

obj_size = 40
obj_data = []     # List to store object positions and their images
obj = pg.image.load('C:/MyFiles/pyproj/pygame_env/TNS/TNS-02/star')
obj = pg.transform.scale(obj, (obj_size, obj_size))

enemy_size = 50
enemy_data = []     # List to store object positions and their images
enemy = pg.image.load('C:/MyFiles/pyproj/pygame_env/TNS/TNS-02/ice')
enemy = pg.transform.scale(enemy, (enemy_size, enemy_size))

bg_image = pg.image.load('C:/MyFiles/pyproj/pygame_env/TNS/TNS-02/images.jfif')
bg_image = pg.transform.scale(bg_image, (win_width, win_height))


def create_object(obj_data):
    if len(obj_data) < 10 and random.random() < 0.1:    
        x = random.randint(300, 410)
        y = 0                                         
        obj_data.append([x, y, obj])


def update_objects(obj_data):
    global score, lives

    for object in obj_data:
        x, y, image_data = object
        if y < win_height:
            y += speed
            object[1] = y
            screen.blit(image_data, (x, y))
        else:
            obj_data.remove(object)
            lives -= 1

def create_enemy(obj_data):
    if len(obj_data) < 10 and random.random() < 0.05:    
        x = random.randint(100, 500)
        y = 0                                         
        obj_data.append([x, y, enemy])


def update_enemy(obj_data):
    global score, lives

    for object in obj_data:
        x, y, image_data = object
        if y < win_height:
            y += speed
            object[1] = y
            screen.blit(image_data, (x, y))
        else:
            obj_data.remove(object)
            score += 1


def collision_check(obj_data, enemy_data, player_pos):
    global running,lives, score
    for object in obj_data:
        x, y, image_data = object
        player_x, player_y = player_pos[0], player_pos[1]
        obj_rect = pg.Rect(x, y, obj_size, obj_size)
        player_rect = pg.Rect(player_x, player_y, player_size, player_size)
        if player_rect.colliderect(obj_rect):
            obj_data.remove(object)
            score += 1
            
    for object in enemy_data:
        x, y, image_data = object
        player_x, player_y = player_pos[0], player_pos[1]
        obj_rect = pg.Rect(x, y, enemy_size, enemy_size)
        player_rect = pg.Rect(player_x, player_y, player_size, player_size)
        if player_rect.colliderect(obj_rect):
            enemy_data.remove(object)
            score -= 1
              
def main():

    global player_pos

    running = True      
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                x, y = player_pos[0], player_pos[1]
                if event.key == pg.K_LEFT:
                    x -= 20
                elif event.key == pg.K_RIGHT:
                    x += 20
                player_pos = [x, y]

        screen.blit(bg_image, (0, 0))
        screen.blit(player_image, (player_pos[0], player_pos[1]))

        text = f'Score: {score}'
        text = font.render(text, 10, white)
        screen.blit(text, (win_width - 200, win_height - 40))

        text = f'Lives: {lives}'
        text = font.render(text, 10, white)
        screen.blit(text, (win_width - 200, win_height - 20))

        create_object(obj_data)
        create_enemy(enemy_data)
        update_objects(obj_data)
        update_enemy(enemy_data)
        collision_check(obj_data, enemy_data, player_pos)

        if lives == 0:
            text = 'Game over!'
            text = font.render(text, 10, white)
            screen.blit(text, (win_width // 2, win_height // 2))
            pg.display.update()
            time.sleep(2)
            running = False
            break

        clock.tick(35)
        pg.display.update()

main()