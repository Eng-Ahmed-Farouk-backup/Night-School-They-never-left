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
    pygame.mixer.music.load("assets/"+"bg sound.mp3")
    pygame.mixer.music.play()
    s = scenes(screen)
    s.scene(screen,background_image="main menu.png",sound_effect="main menu music.mp3",skip=True)
    s.jumpscare(screen,"jumpscare.png","jumpscare music.mp3")
    s.scene(screen,"The story with Max Ran a teenager who is a high school, his life was average, until two angels falled from the heavens named alaska and anabelle to give him a specific mission, His mission was to be a therapist for the dead ones.",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"Max was in a high school that seems normal but in nighttime it turns into a school for the dead ones including teachers and students, dead ones are humans that died before the 13th century, they think they are alive but they are actually dead, Max`s mission is to try to solve thier problems and cure them to run in peace",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"You are Max Ran, Running for your life",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"When anabelle and alaska falled to give you the mission, they falled from heavens to tell you that you are the only one who can do this mission and that if you do not do this mission, the world order would collapse and the underworld will merge witht heavens and destroy the human race including deven and euan who are your managers",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"Note: You could destroy the human race to get rid of them (wink), But you are a good person and you will never do this (wink)",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"Your first mission is for you to join the dead ones night school as a normal student and act like them",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"this is your first day in this mission, when you entered your school at night you found a security guard that his face looks like it was melting, you suddenly started screaming, but he told you, 'HEY BOY! WHY ARE YOU SCREAMING' (in all caps), you said sorry and started running",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"While you are running you saw natasa durk, your high school crush",(255,0,0),"main bg.png","bg sound.mp3",True)
    first_choice = s.choice_scene(screen,"What do you do?",(255,0,0),["Stalk her","Talk to her"],"main bg.png","bg sound.mp3")
    if first_choice == 0:
        s.scene(screen,"You stalked her and saw her acting like the dead until you realized she is not her, she is her grandma, you got scared and ran away",(255,0,0),"main bg.png","bg sound.mp3",True)
        s.jumpscare(screen,"jumpscare.png","jumpscare music.mp3")
        s.scene(screen,"'YOU ARE STALKING ME YOU PERVERT' said natasa, You ran as max ran haha (cheap joke)",(255,0,0),"main bg.png","bg sound.mp3",True)
    elif first_choice == 1:
        s.scene(screen,"You talk to her and she screams in your face, and she told you she is not natasa he is durk, you realized he is natasa`s grandma, you got scared and ran as max ran haha (cheap joke)",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"You remembered your mission: the first dead one you should cure is salah the security guard like anabelle and alaska told me. I have to go back to this melted face, you said",(255,0,0),"main bg.png","bg sound.mp3",True)
    s.scene(screen,"There is a sound behind you",(255,0,0),"main bg.png","satan voice.mp3",True)
    s.scene(screen,"You cant look back! this is a rule if you heard a sound you cant look back",(255,0,0),"main bg.png","satan voice.mp3",True)
    s.scene(screen,"(Foot steps sound)...",(255,0,0),"main bg.png","satan voice.mp3",True)
    s.scene(screen,"You are getting closer to the sound",(255,0,0),"main bg.png","satan voice.mp3",True)
    s.jumpscare(screen,"jumpscare.png","jumpscare music.mp3")
    s.scene(screen,"You can not resist and you look back",(255,0,0),"main bg.png","scary moments.mp3",True)
    s.scene(screen,"IT IS SATAN, YOU FREEZE AND DO NOT KNOW WHAT TO DO",(255,0,0),"main bg.png","scary moments.mp3",True)
    s.scene(screen,"YOU HEAR A SOUND....................",(255,0,0),"main bg.png","run run sound.mp3",False)
    s.jumpscare(screen,"jumpscare.png","jumpscare music.mp3")
    primary_choice = s.choice_scene(screen,"What do you do?",(255,0,0),["Run as the voice told you","See who is talking","Freeze and do not move","Hide in the classroom"],"main bg.png","scary moments.mp3")
    #path 1 here
    if primary_choice == 0:
        pass
    #path 2 here
    elif primary_choice == 1:
        pass
    #path 3 here
    elif primary_choice == 2:
        pass
    #path 4 here
    elif primary_choice == 3:
        pass
    

   

        




    pygame.display.flip()
    clock.tick(FPS)
