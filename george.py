import os
import pygame

pygame.init()

clock = pygame.time.Clock()

dp = pygame.display.set_mode((500,500))

heroes = pygame.Rect(55,55,40,40)

go_left = False
go_right = False
go_bot = False
go_top = False

# wall = 0
# floor_left_right = 1
# hero = 2
# finish = 3
# floor_right_top = 4
# floor_left_top = 5
# floor_right_bot = 6
# floor_left_bot = 7
# floor_top_bot_left = 8
# floor_top_left_right = 9
# floor_top_bot = 10

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")

wall = pygame.image.load(img_path + "/wall.png")
geroi = pygame.image.load(img_path + "/pudge.png")
finish = pygame.image.load(img_path + "/burger.png")
floor1 = pygame.image.load(img_path + "/left_right.png")
floor2 = pygame.image.load(img_path + "/right_top.png")
floor3 = pygame.image.load(img_path + "/left_top.png")
floor4 = pygame.image.load(img_path + "/right_bot.png")
floor5 = pygame.image.load(img_path + "/left_bot.png")
floor6 = pygame.image.load(img_path + "/left_top_bot.png")
floor7 = pygame.image.load(img_path + "/top_left_right.png")
floor8 = pygame.image.load(img_path + "/top_bot.png")

textures = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 0, 0, 6, 1, 7, 0, 3, 0],
    [0, 10, 0, 6, 5, 0, 10, 0, 10, 0],
    [0, 10, 0, 10, 0, 6, 5, 0, 10, 0],
    [0, 4, 1, 8, 0, 10, 0, 0, 10, 0],
    [0, 0, 0, 10, 0, 4, 1, 1, 5, 0],
    [0, 0, 0, 10, 0, 0, 0, 0, 0, 0],
    [0, 6, 1, 9, 1, 7, 0, 6, 1,0],
    [0, 10, 0, 0, 0, 4, 1, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

rects = []
rects_textures = []

bad_rects = []
good_rects = []

x = 0 
y = 0

for texture in textures:
    for i in texture:
        rect = pygame.Rect(x, y, 50, 50)
        rects.append(rect)
        rects_textures.append(i)
        if i == 0:
            bad_rects.append(rect)
        if i == 3:
            good_rects.append(rect)
        x += 50
    y += 50
    x = 0

font = pygame.font.SysFont("Verdana", 50)
text = font.render("YOU WON!", True, (0,255,0))

game_work = True

while game_work:

    dp.fill((255,255,255))

    for i in range(100):
        if rects_textures[i] == 0:
            dp.blit(wall, rects[i])
        if rects_textures[i] == 1:
            dp.blit(floor1, rects[i])
        if rects_textures[i] == 2:
            dp.blit(geroi, rects[i])
        if rects_textures[i] == 3:
            dp.blit(finish, rects[i])
        if rects_textures[i] == 4:
            dp.blit(floor2, rects[i])
        if rects_textures[i] == 5:
            dp.blit(floor3, rects[i])
        if rects_textures[i] == 6:
            dp.blit(floor4, rects[i])
        if rects_textures[i] == 7:
            dp.blit(floor5, rects[i])
        if rects_textures[i] == 8:
            dp.blit(floor6, rects[i])
        if rects_textures[i] == 9:
            dp.blit(floor7, rects[i])
        if rects_textures[i] == 10:
            dp.blit(floor8, rects[i])
    
    dp.blit(geroi, heroes)

    for bad in bad_rects:
        if heroes.colliderect(bad):
            heroes.x = 55
            heroes.y = 55

    for good in good_rects:
        if heroes.colliderect(good):
            dp.fill((0, 0, 0))
            dp.blit(text, (100,200))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_work = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_s:
                go_bot = True
            if event.key == pygame.K_w:
                go_top = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_s:
                go_bot = False
            if event.key == pygame.K_w:
                go_top = False  


    if go_right == True:
        heroes.x += 1
    if go_left == True:
        heroes.x -= 1
    if go_top == True:
        heroes.y -= 1
    if go_bot == True:
        heroes.y += 1

    pygame.display.flip()
    clock.tick(60)