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
        s.scene(screen,"You run as the voice told you, You saw a classroom while you are running",(255,0,0),"main bg.png","run run sound.mp3",True)
        sec_choice = s.choice_scene(screen,"What do you do?",(255,0,0),["Hide the classroom","Keep running"],"main bg.png","run run sound.mp3")
        if sec_choice == 0:
            s.scene(screen,"You hide in the classroom under a desk, you heared satan`s sound again, he is in front of your face",(255,0,0),"main bg.png","satan voice.mp3")    
        elif sec_choice == 1:
            s.scene(screen,"You keep running and you get lost in the school, you are in a corridor with many doors, then satan came out of one of these doors",(255,0,0),"main bg.png","satan voice.mp3")
        s.jumpscare(screen,"jumpscare.png","jumpscare music.mp3")
        s.scene(screen,"You remebered what anabelle and alaska told you to do when you see satan",(255,0,0),"main bg.png","satan voice.mp3")
        s.scene(screen,"Flash back: anabelle said satan is the most dangerous ghost in the universe, no one can beat him except one, the biggest boss of good angels zach betta, and alaska said if you saw him and he wanted to eat you, you have to call zach",(255,0,0),"main bg.png","scary moments.mp3")
        s.scene(screen,"to call zach you should say the spell three times, 'Zach vocamus ut Satanam vincat, te vocamus, veni quaeso.', zach will come and when satan sees him he will run away ",(0,255,0),"main bg.png","scary moments.mp3")
        s.scene(screen,"You said the spell three times, and satan ran away immedietly when he heard you say the spell",(0,255,0),"main bg.png","scary moments.mp3")
        s.scene(screen,"Zach came and told 'WHY DID YOU CALL ME, HOW DARE YOU TO CALL KING OF THE KINGS', you said that you are very sorry and started to tell him your story",(255,0,0),"main bg.png","scary moments.mp3")
        s.scene(screen,"Zach told you 'boy! search for the light, search for the light' then he disappears",(0,0,255),"main bg.png","")
        s.scene(screen,"You are confused about what zach said, until you hear the same voice who told you run",(255,0,0),"main bg.png","")
        s.scene(screen,"It was natasa`s grandma, natasa`s grandma told you 'I am not natasa`s grandmother like you think'",(255,0,0),"main bg.png","")
        s.scene(screen,"I am natasa durk",(255,0,0),"main bg.png","jumpscare music.mp3",False)
        s.scene(screen,"She told you: 'I got an order from zach, I should stop pretending and guide you to the light, Follow me'",(255,0,0),"main bg.png","scary moments.mp3")
        s.scene(screen,"natasa said the spell three times and you both teleported to a kids room",(255,0,0),"main bg.png","main bg.mp3")
        s.scene(screen,"'Listen to my story well' said natasa, 'this is my room as a kid when i was 6' said natasa, one day dad told me 'don`t you want to win a prize?' i said 'yes ofcourse', he told me 'you have two mission if you do them well you will get the prize'",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"my first mission was to put the box he gave to me under the bed, i didn`t know why he made me do this but i want a prize, so i did it, then he told me there is one person you know who has your prize, this person hid it, you should find this person and take your prize",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"I kept searching for who is this person for three hours, until i tried to open the box that i put under the bed that my dad gave me, and i found that it was the prize, then i realized i was the person i was searching for",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"natasa said the spell and we retun back to the classroom, she told me you should learn from the story i told you and find your light, find the light and she disappeared",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"You are confused about what natasa said, but you have to do your first mission, you have to find salah, the security guard",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"You saw him walking near the classroom, You went to him, and said 'hey mr salah'",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"He turned his face to you and you saw his melted face, With every bit of bravery you have, you told him why do you feel sad",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"Salah told you 'I am sad because i can not see my family, i can not see my wife and my son, i can not see them for 700 years'",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"'and why do you think you can not see them? i mean you must be dead for 700 years hahaha' you said", (255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"'WHAT ARE YOU SAYING' he told you, you said 'I am sorry. but your family missed you too  you have to find them find the light , you said",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen, "Salah started crying , I have to find my family, my son , my wife, my light, hes said",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"Salah looked into the sky and started flying, thank you you made me find my family , find the light, salah said",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"you started thinking about what zach and natasa said, find the light!, it's the excactly the same word you said to salah. what is the ligth?",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"I have to find the light, you started remembring the story natasa told you, maybe the light is something I have , You started remembring your memories with your brother, it was in in 16th centuary",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"but how in the 16th century , I am in the 21 Century, you said",(255,0,0),"main bg.png","main bg.mp3",True)
        s.scene(screen,"I am Dead one Max ran is a dead one, you said, You saw a path to the heaven filled of light , you relize this is the light zach and natasa were talking about , you went to heaven and ran in peace",(255,0,0),"main bg.png","main bg.mp3",True)
        break

    #path 2 here
    elif primary_choice == 1:
        pass


    


    pygame.display.flip()
    clock.tick(FPS)