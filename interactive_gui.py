import pygame
pygame.mixer.init()
pygame.init()
class scenes:
    def __init__(self, surface):
        self.surface = surface
        self.current_music = None
    def scene(self,surface,text="",color=(0,0,0),background_image=None,sound_effect=None,skip=True):
        if background_image:
            background = pygame.image.load("assets/"+background_image)
            surface.blit(background, (0, 0))
        if not sound_effect:
            pygame.mixer.music.stop()
            self.current_music = None
        if sound_effect and (not self.current_music == sound_effect or not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("assets/"+sound_effect)
            pygame.mixer.music.play()
            self.current_music = sound_effect
        if text:
            print(text)
            font = pygame.font.Font("BRADHITC.TTF", 24)
            text_surface = font.render(text, True, color, wraplength=700)
            surface.blit(text_surface, (20, surface.get_height()/2 - 50))

        
        #continue button
        button_font = pygame.font.Font("BRADHITC.TTF", 32)
        button_surface = button_font.render("Continue", True, (255, 0, 0))
        button_rect = button_surface.get_rect()
        button_rect.center = (surface.get_width()/2, surface.get_height()/2 + 150)
        surface.blit(button_surface, button_rect)
        while pygame.mixer.music.get_busy() and not skip:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        while True:
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return


    def choice_scene(self,surface,header,color,choices,background_image=None,sound_effect=None):
        if background_image:
            background = pygame.image.load("assets/"+background_image)
            surface.blit(background, (0, 0))
        if sound_effect and (not self.current_music == sound_effect or not pygame.mixer.music.get_busy()):
            pygame.mixer.music.load("assets/"+sound_effect)
            pygame.mixer.music.play()
            self.current_music = sound_effect
        font = pygame.font.SysFont("Arial", 24)
        header_surface = font.render(header, True, color, (0, 0, 0))
        surface.blit(header_surface, (20, surface.get_height()/2 - 100))
        choice_surfaces = []
        for choice in choices:
            choice_surface = font.render(choice, True, color, (0, 0, 0))
            choice_surfaces.append(choice_surface)
        for i, choice_surface in enumerate(choice_surfaces):
            surface.blit(choice_surface, (15, surface.get_height()/2 + i*35))
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, choice_surface in enumerate(choice_surfaces):
                        choice_rect = choice_surface.get_rect()
                        choice_rect.topleft = (15, surface.get_height()/2 + i*35)
                        if choice_rect.collidepoint(event.pos):
                            return i


    def jumpscare(self,surface,image,sound_effect):
        pygame.mixer.music.load("assets/"+sound_effect)
        pygame.mixer.music.play()
        background = pygame.image.load("assets/"+image)
        surface.blit(background, (0, 0))
        pygame.display.flip()
        while pygame.mixer.music.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        