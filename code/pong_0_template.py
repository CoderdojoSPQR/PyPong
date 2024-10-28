import pygame
import sys

pygame.init()

# Dimensioni della finestra e colori
L_SCHERMO, A_SCHERMO = 800, 600
BIANCO = (255, 255, 255)

# Inizializzazione della finestra
schermo = pygame.display.set_mode((L_SCHERMO, A_SCHERMO))

# Posizione e velocità della pallina
# ...

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
    # ...
    pygame.display.update()
    pygame.time.delay(30)
