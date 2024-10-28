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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y = paddle1_y - velocita_paddle
    if keys[pygame.K_s] and paddle1_y < A_SCHERMO - paddle_altezza:
        paddle1_y = paddle1_y + velocita_paddle
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y = paddle2_y - velocita_paddle
    if keys[pygame.K_DOWN] and paddle2_y < A_SCHERMO - paddle_altezza:
        paddle2_y = paddle2_y + velocita_paddle

    # Movimento della pallina
    x_pallina = x_pallina + dx_pallina
    y_pallina = y_pallina + dy_pallina


    # COLLISIONI
    # =======
    # Collisione con il bordo superiore e inferiore
    if y_pallina <= grandezza_pallina or y_pallina >= A_SCHERMO - grandezza_pallina:
        dy_pallina = dy_pallina * -1


    # Collisione con il paddle sinistro
    if (x_pallina - grandezza_pallina <= paddle_larghezza and
        paddle1_y < y_pallina < paddle1_y + paddle_altezza):
        dx_pallina = dx_pallina * -1
        x_pallina = paddle_larghezza + grandezza_pallina 


    # Collisione con il paddle destro
    if (x_pallina + grandezza_pallina >= L_SCHERMO - paddle_larghezza and
    paddle2_y < y_pallina < paddle2_y + paddle_altezza):
        dx_pallina = dx_pallina * -1
        x_pallina = L_SCHERMO - paddle_larghezza - grandezza_pallina 

    # Reset della pallina se va oltre i bordi
    if x_pallina < 0 or x_pallina > L_SCHERMO:
        x_pallina, y_pallina = L_SCHERMO // 2, A_SCHERMO // 2
        dx_pallina = -dx_pallina



    # Disegno di tutto 
    schermo.fill((0, 0, 0))
    pygame.draw.circle(schermo, BIANCO, (x_pallina, y_pallina), grandezza_pallina)
    pygame.draw.rect(schermo, BIANCO, (0, paddle1_y, paddle_larghezza, paddle_altezza))
    pygame.draw.rect(schermo, BIANCO, (L_SCHERMO - paddle_larghezza, paddle2_y, paddle_larghezza, paddle_altezza))
    pygame.display.update()
    pygame.time.delay(30)
