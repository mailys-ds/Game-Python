import pygame
from game import Game

pygame.init()


pygame.display.set_caption("Hey")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load("assets/bg.jpg")

game=Game()

#upload our player
#player=Player()

running = True

while running:

    # display background
    screen.blit(background, (0, -200))

    # display player image
    screen.blit(game.player.image,game.player.rect)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # display all images of the projectiles
    game.player.all_projectiles.draw(screen)

    game.all_monsters.draw(screen)
    for monster in game.all_monsters:
        monster.forward()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    #update screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        #Detect if a player press a key of the keyboard
        elif event.type == pygame.KEYDOWN:

            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                print('Projectile launched')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



