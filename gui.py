import pygame
from interactive_gui import *
screen = pygame.display.set_mode((900, 500))

FPS = 60

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    scene(screen,background_image="main menu.png",sound_effect="main menu music.mp3",skip=True)
    scene(screen,"The story with Max Ran a teenager who is a high school, his life was average, until two angels falled from the heavens named alaska and anabelle to give him a specific mission, His mission was to be a therapist for the dead ones.",(255,0,0),"main bg.png","main menu music.mp3",True)
    scene(screen,"Max was in a high school that seems normal but in nighttime it turns into a school for the dead ones including teachers and students, dead ones are humans that died before the 13th century, they think they are alive but they are actually dead, Max`s mission is to try to solve thier problems and cure them to run in peace",(255,0,0),"main bg.png","main menu music.mp3",True)
    scene(screen,"You are Max Ran, Running for your life",(255,0,0),"main bg.png","main menu music.mp3",True)
    scene(screen,"When anabelle and alaska falled to give you the mission, they falled from heavens to tell you that you are the only one who can do this mission and that if you do not do this mission, the world order would collapse and the underworld will merge witht heavens and destroy the human race including deven and euan who are your managers",(255,0,0),"main bg.png","main menu music.mp3",True)
    scene(screen,"Note: You could destroy the human race to get rid of them (wink), But you are a good person and you will never do this (wink)",(255,0,0),"main bg.png","main menu music.mp3",True)
    scene(screen,"Your first mission is for you to join the dead ones night school as a normal student and act like them",(255,0,0),"main bg.png","main menu music.mp3",True)
    scene(screen,"this is your first day in this mission, when you entered your school at night you found a security guard that his face looks like it was melting, you suddenly started screaming, but he told you, 'HEY BOY! WHY ARE YOU SCREAMING' (in all caps), you said sorry and started running",(255,0,0),"main bg.png","main menu music.mp3",True)



    pygame.display.flip()
    clock.tick(FPS)