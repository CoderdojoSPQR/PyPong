import pygame
import sys

pygame.init()

# Dimensioni della finestra e colori
L_SCHERMO, A_SCHERMO = 800, 600
BIANCO = (255, 255, 255)

# Inizializzazione della finestra
schermo = pygame.display.set_mode((L_SCHERMO, A_SCHERMO))

# Posizione e velocità della pallina
x_pallina, y_pallina = L_SCHERMO // 2, A_SCHERMO // 2
dx_pallina, dy_pallina = 5, 5
grandezza_pallina = 10

paddle1_y, paddle2_y = A_SCHERMO // 2, A_SCHERMO // 2
paddle_larghezza, paddle_altezza = 10, 100
velocita_paddle = 7

# Loop principale del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controlli paddle
    # ...

    # Movimento della pallina
    # ...

    # COLLISIONI
    # =======
    # Collisione con il bordo superiore e inferiore
    # ...


    # Collisione con il paddle sinistro
    # ...


    # Collisione con il paddle destro
    # ...


    # Reset della pallina se va oltre i bordi
    # ...



    # Disegno di tutto 
    schermo.fill((0, 0, 0))
    pygame.draw.circle(schermo, BIANCO, (x_pallina, y_pallina), grandezza_pallina)
    pygame.draw.rect(schermo, BIANCO, (0, paddle1_y, paddle_larghezza, paddle_altezza))
    pygame.draw.rect(schermo, BIANCO, (L_SCHERMO - paddle_larghezza, paddle2_y, paddle_larghezza, paddle_altezza))
    pygame.display.update()
    pygame.time.delay(30)
