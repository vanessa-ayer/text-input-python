import pygame, sys 

# General Setup 
pygame.init()
clock = pygame.time.Clock()

# Main Screen 
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Text Input')
main_font = pygame.font.Font('_decterm.ttf', 20)
user_text = ''

# Variables 
input_rect = pygame.Rect(5, 5, 50, 30)
color_active = (74,246,38)
color_inactive = (211,211,211)
color = color_inactive

active = False 

# Loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else: 
                active = False
        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1] 
                else:      
                    user_text += event.unicode 
    
    if active: 
        color = color_active
    else:
        color = color_inactive

    # Visuals 

    screen.fill((30, 44, 38))
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = main_font.render(user_text, True, (74,246,38))
    screen.blit(text_surface, (input_rect.x + 3, input_rect.y + 5)) 
    input_rect.w = max(50,text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)


