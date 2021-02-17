import pygame
from pathlib import Path

pygame.init()
SECREEN_RESOLUTION = (1280, 720)
FPS = 60
LIGHT_BLACK = (64, 64, 64)
IMG_KITTY_SRC = 'images/kitties'

screen = pygame.display.set_mode(SECREEN_RESOLUTION)
clock = pygame.time.Clock()


img_kitty_lst = Path(IMG_KITTY_SRC).glob('**/*')

kitty_img = []
for img in img_kitty_lst:
    kitty_img.append(pygame.image.load(str(img)))

image_left = kitty_img[0]
image_right = kitty_img[1]
left_index = 0
right_index = 1

img_left_post = (0, 0)
img_right_post = (500, 0)


def end_game():
    pygame.quit()
    quit()


while True:
    clock.tick(FPS)
    screen.fill(LIGHT_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pressed()

            if click[0]:
                print("left")
                left_index += 1
                if left_index >= len(kitty_img):
                    left_index = 0
                image_left = kitty_img[left_index]
            if click[2]:
                print("right")
                right_index += 1
                if right_index >= len(kitty_img):
                    right_index = 0
                image_right = kitty_img[right_index]

    screen.blit(image_left, img_left_post)
    screen.blit(image_right, img_right_post)
    pygame.display.update()
