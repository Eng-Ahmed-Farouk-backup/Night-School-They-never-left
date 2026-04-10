from entities import *
from items import *
from interactive_console import *
from gui import *
import sys
import pygame

pygame.mixer.init()

class Game:
    def __init__(self):
        self.settings = {
            "text_speed": "Normal"
        }
        self.current_music = None
    
    def play_sound(self, sound_effect):
        if sound_effect and (not self.current_music == sound_effect or not pygame.mixer.music.get_busy()):
            try:
                pygame.mixer.music.load("assets/" + sound_effect)
                pygame.mixer.music.play()
                self.current_music = sound_effect
            except:
                pass
    
    def menu(self):
        while True:
            options = ["Start Game in CLI","Start game in GUI", "Settings", "Exit"]
            option = interactive_menu(options, "Welcome to the RPG Game!", "yellow")
            if option == 0:
                self.start_game()
            elif option == 1:
                pass
            elif option == 2:
                self.settings_menu()
            elif option == 3:
                println("Thanks for playing!", "yellow")
                sys.exit()
    
    def settings_menu(self):
        options = ["Text Speed", "Back"]
        while True:
            option = interactive_menu(options, "Settings", "yellow")
            if option == 0:
                self.text_speed_menu()
            elif option == 1:
                return
    

    def text_speed_menu(self):
        options = ["Slow", "Normal", "Fast", "Back"]
        option = interactive_menu(options, "Select Text Speed", "yellow")
        if option == 0:
            self.settings["text_speed"] = "Slow"
        elif option == 1:
            self.settings["text_speed"] = "Normal"
        elif option == 2:
            self.settings["text_speed"] = "Fast"
        elif option == 3:
            return
    
    def start_game(self):
        # to skip press space
        println("To skip press space", "green")
        self.play_sound("bg sound.mp3")
        println("The story with Max Ran a teenager who is a high school, his life was average, until two angels falled from the heavens named alaska and anabelle to give him a specific mission, His mission was to be a therapist for the dead ones.", "white", self.settings["text_speed"])
        println("Max was in a high school that seems normal but in nighttime it turns into a school for the dead ones including teachers and students, dead ones are humans that died before the 13th century, they think they are alive but they are actually dead, Max`s mission is to try to solve thier problems and cure them to run in peace", "white", self.settings["text_speed"])
        println("You are Max Ran, Running for your life", "white", self.settings["text_speed"])
        println("When anabelle and alaska falled to give you the mission, they falled from heavens to tell you that you are the only one who can do this mission and that if you do not do this mission, the world order would collapse and the underworld will merge witht heavens and destroy the human race including deven and euan who are your managers", "white", self.settings["text_speed"])
        println("Note: You could destroy the human race to get rid of them (wink), But you are a good person and you will never do this (wink)", "white", self.settings["text_speed"])
        println("Your first mission is for you to join the dead ones night school as a normal student and act like them", "white", self.settings["text_speed"])
        println("this is your first day in this mission, when you entered your school at night you found a security guard that his face looks like it was melting, you suddenly started screaming, but he told you, 'HEY BOY! WHY ARE YOU SCREAMING' (in all caps), you said sorry and started running", "white", self.settings["text_speed"])
        println("While you are running you saw natasa durk, your high school crush", "white", self.settings["text_speed"])
        
        first_choice = interactive_menu(["Stalk her", "Talk to her"], "What do you do?", "yellow")
        if first_choice == 0:
            println("You stalked her and saw her acting like the dead until you realized she is not her, she is her grandma, you got scared and ran away", "white", self.settings["text_speed"])
            println("'YOU ARE STALKING ME YOU PERVERT' said natasa, You ran as max ran haha (cheap joke)", "white", self.settings["text_speed"])
        elif first_choice == 1:
            println("You talk to her and she screams in your face, and she told you she is not natasa he is durk, you realized he is natasa`s grandma, you got scared and ran as max ran haha (cheap joke)", "white", self.settings["text_speed"])
        println("You remembered your mission: the first dead one you should cure is salah the security guard like anabelle and alaska told me. I have to go back to this melted face, you said", "white", self.settings["text_speed"])
        self.play_sound("satan voice.mp3")
        println("There is a sound behind you", "white", self.settings["text_speed"])
        println("You cant look back! this is a rule if you heard a sound you cant look back", "white", self.settings["text_speed"])
        println("(Foot steps sound)...", "white", self.settings["text_speed"])
        println("You are getting closer to the sound", "white", self.settings["text_speed"])
    
        self.play_sound("scary moments.mp3")
        println("You can not resist and you look back", "white", self.settings["text_speed"])
        println("IT IS SATAN, YOU FREEZE AND DO NOT KNOW WHAT TO DO", "white", self.settings["text_speed"])    
        self.play_sound("run run sound.mp3")
        println("YOU HEAR A SOUND....................", "white", self.settings["text_speed"])
        self.play_sound("scary moments.mp3")
        primary_choice = interactive_menu(["Run as the voice told you", "See who is talking"], "What do you do?", "yellow")

        #path 1 here
        if primary_choice == 0:
            self.play_sound("run run sound.mp3")
            println("You run as the voice told you, You saw a classroom while you are running", "white", self.settings["text_speed"])
            sec_choice = interactive_menu(["Hide the classroom", "Keep running"], "What do you do?", "yellow")
            if sec_choice == 0:
                self.play_sound("satan voice.mp3")
                println("You hide in the classroom under a desk, you heared satan`s sound again, he is in front of your face", "white", self.settings["text_speed"])    
            elif sec_choice == 1:
                self.play_sound("satan voice.mp3")
                println("You keep running and you get lost in the school, you are in a corridor with many doors, then satan came out of one of these doors", "white", self.settings["text_speed"])
            self.play_sound("satan voice.mp3")
            println("You remebered what anabelle and alaska told you to do when you see satan", "white", self.settings["text_speed"])
            self.play_sound("scary moments.mp3")
            println("Flash back: anabelle said satan is the most dangerous ghost in the universe, no one can beat him except one, the biggest boss of good angels zach betta, and alaska said if you saw him and he wanted to eat you, you have to call zach", "white", self.settings["text_speed"])
            println("to call zach you should say the spell three times, 'Zach vocamus ut Satanam vincat, te vocamus, veni quaeso.', zach will come and when satan sees him he will run away ", "green", self.settings["text_speed"])
            println("You said the spell three times, and satan ran away immedietly when he heard you say the spell", "green", self.settings["text_speed"])
            self.play_sound("scary moments.mp3")


            println("Zach came and told 'WHY DID YOU CALL ME, HOW DARE YOU TO CALL KING OF THE KINGS', you said that you are very sorry and started to tell him your story", "white", self.settings["text_speed"])
            println("Zach told you 'boy! search for the light, search for the light' then he disappears", "blue", self.settings["text_speed"])
            println("You are confused about what zach said, until you hear the same voice who told you run", "white", self.settings["text_speed"])
            println("It was natasa`s grandma, natasa`s grandma told you 'I am not natasa`s grandmother like you think'", "white", self.settings["text_speed"])
            

            println("I am natasa durk", "white", self.settings["text_speed"])
            self.play_sound("scary moments.mp3")
            println("She told you: 'I got an order from zach, I should stop pretending and guide you to the light, Follow me'", "white", self.settings["text_speed"])
            self.play_sound("bg sound.mp3")

            println("natasa said the spell three times and you both teleported to a kids room", "white", self.settings["text_speed"])
            println("'Listen to my story well' said natasa, 'this is my room as a kid when i was 6' said natasa, one day dad told me 'don`t you want to win a prize?' i said 'yes ofcourse', he told me 'you have two mission if you do them well you will get the prize'", "white", self.settings["text_speed"])
            println("my first mission was to put the box he gave to me under the bed, i didn`t know why he made me do this but i want a prize, so i did it, then he told me there is one person you know who has your prize, this person hid it, you should find this person and take your prize", "white", self.settings["text_speed"])
            println("I kept searching for who is this person for three hours, until i tried to open the box that i put under the bed that my dad gave me, and i found that it was the prize, then i realized i was the person i was searching for", "white", self.settings["text_speed"])
            println("natasa said the spell and we retun back to the classroom, she told me you should learn from the story i told you and find your light, find the light and she disappeared", "white", self.settings["text_speed"])
            println("You are confused about what natasa said, but you have to do your first mission, you have to find salah, the security guard", "white", self.settings["text_speed"])
            println("You saw him walking near the classroom, You went to him, and said 'hey mr salah'", "white", self.settings["text_speed"])
            println("He turned his face to you and you saw his melted face, With every bit of bravery you have, you told him why do you feel sad", "white", self.settings["text_speed"])
            println("Salah told you 'I am sad because i can not see my family, i can not see my wife and my son, i can not see them for 700 years'", "white", self.settings["text_speed"])
            println("'and why do you think you can not see them? i mean you must be dead for 700 years hahaha' you said", "white", self.settings["text_speed"])
            println("'WHAT ARE YOU SAYING' he told you, you said 'I am sorry. but your family missed you too  you have to find them find the light , you said", "white", self.settings["text_speed"])
            println("Salah started crying , I have to find my family, my son , my wife, my light, hes said", "white", self.settings["text_speed"])
            println("Salah looked into the sky and started flying, thank you you made me find my family , find the light, salah said", "white", self.settings["text_speed"])
            println("you started thinking about what zach and natasa said, find the light!, it's the excactly the same word you said to salah. what is the ligth?", "white", self.settings["text_speed"])
            println("I have to find the light, you started remembring the story natasa told you, maybe the light is something I have , You started remembring your memories with your brother, it was in in 16th centuary", "white", self.settings["text_speed"])
            println("but how in the 16th century , I am in the 21 Century, you said", "white", self.settings["text_speed"])
            println("I am Dead one Max ran is a dead one, you said, You saw a path to the heaven filled of light , you relize this is the light zach and natasa were talking about , you went to heaven and ran in peace", "white", self.settings["text_speed"])
        
        #path 2 here
        elif primary_choice == 1:
            
            self.play_sound("scary moments.mp3")

            println("You see who is talking and you are shocked to see natasa`s grandma, you said 'why are you talking to me?'", "white", self.settings["text_speed"])
            println("I am tired of this I can't take it anymore!, I will tell everything!, Natasa's grandma said", "white", self.settings["text_speed"])
            println("I am not Natasa's Grandma,I am Natasa, Alaska and Annabel are EVIL. they want you to destroy the world! , Natasa said", "white", self.settings["text_speed"])
            println("They are not Angels they are Devils and work for Satan! , they believe you are the most dumb person to do this mission so they hired you to fail", "white", self.settings["text_speed"])
            println("If you fail the world will end! , You mustn't Trust them and try to save the world!", "white", self.settings["text_speed"])
            println("How did you know?, you said. It doesn't matter right now ! satan is coming! you should run ruuuuuuuuuuuuuuuuuuun RUUUUUUUUUUUN!", "white", self.settings["text_speed"])
            println("you are running from satan but you saw him eating Natasa!. she died for you!", "white", self.settings["text_speed"])
            self.play_sound("scary moments.mp3")

            trust = interactive_menu(["I will Trust Natasa", "I will Trust Annabel and Alaska"], "Will you Trust Natasa or You Will trust Annabel and Alaska?", "yellow")
            if trust == 0:
               
                self.play_sound("bg sound.mp3")
                println("You Trusted Natasa", "white", self.settings["text_speed"])

                println("I will prove that I will success and save the world ! , you said", "white", self.settings["text_speed"])
                println("you found in your bucket a massage from Natasa, you opend it", "white", self.settings["text_speed"])
                println("the Massage : \n \n HEY ADAM , IF YOU ARE READING THIS THIS MEANS I DIED \n THIS IS GUIDE TO KNOW HOW WILL YOU BEAT SATAN AND HIS TEAM \n FIRST YOU SHOULD PUT TRAPS FOR annabel AND alaska and then complete your first mission which is curing salah the security dead one to make him run in peace", "white", self.settings["text_speed"])
            elif trust == 1:
               
                self.play_sound("bg sound.mp3")
                println("You Choosed to not trust Natasa !", "white", self.settings["text_speed"])

                println("you heared a sound , it feels like annabel's sound , you went to look and you saw annabel was telling alaska 'I know this boy He will fail and we will get what we want!' you started realizing that Natasa was right ! ", "white", self.settings["text_speed"])
                println("ok , I will show you manipuliters! , you said whespering", "white", self.settings["text_speed"])
                println("you found in your bucket a massage from Natasa, you opend it", "white", self.settings["text_speed"])
                println("the Massage : \n HEY ADAM , IF YOU ARE READING THIS THIS MEANS I DIED  \nTHIS IS GUIDE TO KNOW HOW WILL YOU BEAT SATAN AND HIS TEAM, FIRST YOU SHOULD PUT TRAPS FOR annabel AND alaska and then complete your first mission which is curing salah the security dead one to make him run in peace", "white", self.settings["text_speed"])
            
            self.play_sound("bg sound.mp3")
            println("You started putting traps for annabel and alaska, you put a trap for annabel in the cafeteria and a trap for alaska in the library", "white", self.settings["text_speed"])
            println("you started screaming 'annabel annaaaaaaaaaaaaaaaaaaaabellllllll' \n I heard you screaming what do you want, Annable said. \n I want you to go to the cafeteria I have to show you something but don't tell alaska, you said \n", "white", self.settings["text_speed"])
            println("You trapped anabelle successfully, now its time to trap alaska, you screamed 'alaska alaskaaaaaaaaaaaaaa' \n I heard you screaming what do you want, Alaska said. \n I want you to go to the library I have to show you something but don't tell annabel, you said \n", "white", self.settings["text_speed"])
            println("You trapped alaska successfully, Why did you do this, alaska said, shut up you manipulators, I know you are devils and you work for satan, what do you mean? said alaska", "white", self.settings["text_speed"])
            
            self.play_sound("scary moments.mp3")
            println("You hear the sound of the doors open, natasa and satan enter, natasa are you alive? you said", "white", self.settings["text_speed"])
            println("natasa said 'Shut up you idiot, I am not natasa, I AM ASATAN(reversed)!, The daughter of satan, I manipulated you to help me get rid of them and destroy the world!'", "white", self.settings["text_speed"])
            self.play_sound("scary moments.mp3")

            println("Flashback: Alaska said 'if any emergency happened we should say the spell together to call zach the most important and powerful angel, he can beat satan himself: Zach vocamus ut Satanam vincat, te vocamus, veni quaeso.'", "white", self.settings["text_speed"])
            println("Lets go annabel and alaska, they understanded you and you said the spell together, you called zach and he came immediately, he killed satan and asatan", "white", self.settings["text_speed"])
            
            self.play_sound("bg sound.mp3")
            println("anabelle and alaska forgive you because you are a good person and asatan is a very manipulative demon, they told you go now and complete your mission", "white", self.settings["text_speed"])
            println("you have to do your first mission, you have to find salah, the security guard", "white", self.settings["text_speed"])
            println("You saw him walking near the classroom, You went to him, and said 'hey mr salah'", "white", self.settings["text_speed"])
            println("He turned his face to you and you saw his melted face, With every bit of bravery you have, you told him why do you feel sad", "white", self.settings["text_speed"])
            println("Salah told you 'I am sad because i can not see my family, i can not see my wife and my son, i can not see them for 700 years'", "white", self.settings["text_speed"])
            
            println("'and why do you think you can not see them? i mean you must be dead for 700 years hahaha' you said", "white", self.settings["text_speed"])
            println("'WHAT ARE YOU SAYING' he told you, you said 'I am sorry. but your family missed you too  you have to find them find the light , you said", "white", self.settings["text_speed"])
            println("Salah started crying , I have to find my family, my son , my wife, my light, hes said", "white", self.settings["text_speed"])
            println("Salah looked into the sky and started flying, thank you you made me find my family , find the light, salah said", "white", self.settings["text_speed"])
            println("you started thinking about what zach and natasa said, find the light!, it's the excactly the same word you said to salah. what is the ligth?", "white", self.settings["text_speed"])
            println("I have to find the light, you started remembring the story natasa told you, maybe the light is something I have , You started remembring your memories with your brother, it was in in 16th centuary", "white", self.settings["text_speed"])
            println("but how in the 16th century , I am in the 21 Century, you said", "white", self.settings["text_speed"])
            println("I am Dead one Max ran is a dead one, you said, You saw a path to the heaven filled of light , you relize this is the light zach and natasa were talking about , you went to heaven and ran in peace", "white", self.settings["text_speed"])
if __name__ == "__main__":
    game = Game()
    game.menu()
