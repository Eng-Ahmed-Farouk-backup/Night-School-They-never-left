import pygame
pygame.mixer.init()
pygame.init()
def scene(surface,text="",color=(0,0,0),background_image=None,sound_effect=None):
    if background_image:
        background = pygame.image.load("assets/"+background_image)
        surface.blit(background, (0, 0))
    #display image at bottom right corner of top half of screen
    if sound_effect:
        pygame.mixer.music.load("assets/"+sound_effect)
        pygame.mixer.music.play()
    if text:
        print(text)
        font = pygame.font.Font("BRADHITC.TTF", 24)
        text_surface = font.render(text, True, color, (255, 255, 255))
        surface.blit(text_surface, (20, surface.get_height()/2 - 50))

    while pygame.mixer.music.get_busy():
        pass
    #continue button
    button_font = pygame.font.Font("BRADHITC.TTF", 32)
    button_surface = button_font.render("Continue", True, (255, 0, 0), (255, 255, 255))
    button_rect = button_surface.get_rect()
    button_rect.center = (surface.get_width()/2, surface.get_height()/2 + 150)
    surface.blit(button_surface, button_rect)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return


def choice_scene(surface,header,color,choices,background_image=None,sound_effect=None):
    if background_image:
        background = pygame.image.load("assets/"+background_image)
        surface.blit(background, (0, 0))
    if sound_effect:
        pygame.mixer.music.load("assets/"+sound_effect)
        pygame.mixer.music.play()
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
    

    