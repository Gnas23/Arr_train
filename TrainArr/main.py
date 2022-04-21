import pygame
import button
import time

#pygame setup
pygame.init()
white = (255, 255, 255)
X = 1000
Y = 500
screen = pygame.display.set_mode((X, Y ))
pygame.display.set_caption("ARR DEMO")

#background
background = pygame.image.load(r'assets\background.png').convert()
bg = pygame.transform.scale(background, (1000, 500)), (0, 0)


#load button image
add_img = pygame.image.load(r'assets\add.jpg').convert_alpha()
remove_img = pygame.image.load(r'assets\remove .jpg').convert_alpha()
right_img = pygame.image.load(r'assets\right.png').convert_alpha()
left_img = pygame.image.load(r'assets\left.png').convert_alpha()
check_img = pygame.image.load(r'assets\check.png').convert_alpha()
#creat button image
add_button = button.Button(330, 50, add_img, 0.06)
remove_button = button.Button(510,50, remove_img, 0.06)
right_button = button.Button(675, 45, right_img, 0.09)
left_button = button.Button(230, 45, left_img, 0.09)
check_button = button.Button(465, 150, check_img, 0.09)

#Load_image_train
train_Image = pygame.image.load(r'assets\train.png')

#build_backgound
screen.fill(white)
screen.blit(background,(0,0))
screen.blit(pygame.transform.scale(background, (1000, 500)), (0, 0))

def carriageImage(X, Y):
    screen.blit(carriage_Image, (X_carriage, Y_carriage))
def trainImage(X,Y):
    screen.blit(train_Image,(X_train, Y_train))

#Carriage_array
array_carriage = []
pos_array_carriage = []

count = 0

X_train = 0
Y_train = 300

X_carriage = 145
Y_carriage = 330

moving = 0
trainImage(X_train,Y_train)

running = True

# def add_carriage():



#main loop
while running:

    if add_button.draw(screen):
        screen.fill(white)
        screen.blit(background, (0, 0))
        screen.blit(pygame.transform.scale(background, (1000, 500)), (0, 0))
        array_carriage.append('.')
        if len(array_carriage) == 1:
            if count != 0:
                X_carriage = 145 + count * 40
                pos_array_carriage.append(X_carriage)
            else:
                X_carriage = 145
                pos_array_carriage.append(X_carriage)
        else:
            X_carriage = 130 + (pos_array_carriage[len(pos_array_carriage) - 1] )
            pos_array_carriage.append(X_carriage)
        for i in range(0,len(array_carriage)):
            carriage_Image = pygame.image.load(r'assets\carriage0.png')
            X_carriage = pos_array_carriage[i]
            Y_carriage = 330
            if len(array_carriage) != 0:
                carriageImage(X_carriage,Y_carriage)
        print(len(array_carriage))




    elif remove_button.draw(screen):
        if len(array_carriage) == 0:
            pass
        else:
            screen.fill(white)
            screen.blit(background, (0, 0))
            screen.blit(pygame.transform.scale(background, (1000, 500)), (0, 0))
            array_carriage.remove(array_carriage[len(array_carriage) - 1])
            pos_array_carriage.remove(pos_array_carriage[len(pos_array_carriage) - 1])
            for i in range(0, len(array_carriage)):
                carriage_Image = pygame.image.load(r'assets\carriage0.png')
                X_carriage = pos_array_carriage[i]
                Y_carriage = 330
                if len(array_carriage) != 0:
                    carriageImage(X_carriage, Y_carriage)




    elif right_button.draw(screen):
        X_train += 40
        count += 1
        screen.blit(pygame.transform.scale(background, (1000, 500)), (moving, 0))
        for i in range(len(array_carriage)):
            pos_array_carriage[i] += 40
            X_carriage = pos_array_carriage[i]
            Y_carriage = 330

            if len(array_carriage) != 0:
                carriageImage(X_carriage,Y_carriage)




    elif left_button.draw(screen):
        X_train -= 40
        count -= 1
        screen.blit(pygame.transform.scale(background, (1000, 500)), (moving, 0))
        for i in range(len(array_carriage)):
            pos_array_carriage[i] -= 40
            X_carriage = pos_array_carriage[i]
            Y_carriage = 330

            if len(array_carriage) != 0:
                carriageImage(X_carriage, Y_carriage)




    elif check_button.draw(screen):
        while True:
            if pos_array_carriage[len(pos_array_carriage) - 1] < 0:
                X_train += 1300
                for change_pos in range(len(pos_array_carriage)):
                    pos_array_carriage[change_pos] += 1300
            else:
                X_train -= 15
                Y_train = 300
                screen.blit(pygame.transform.scale(background, (1000, 500)), (moving, 0))
                for i in range(len(array_carriage)):
                    pos_array_carriage[i] -= 15
                    X_carriage = pos_array_carriage[i]
                    Y_carriage = 330

                    if len(array_carriage) != 0:
                        carriageImage(X_carriage, Y_carriage)
                trainImage(X_train, Y_train)
                time.sleep(0.09)
                pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    trainImage(X_train, Y_train)
    pygame.display.update()


