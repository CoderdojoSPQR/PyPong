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
PADDLE_LARGHEZZA, PADDLE_ALTEZZA = 10, 100
VELOCITA_PADDLE = 7

punti_giocatore_1 = 0
punti_giocatore_2 = 0

# Loop principale del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controlli paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= VELOCITA_PADDLE
    if keys[pygame.K_s] and paddle1_y < A_SCHERMO - PADDLE_ALTEZZA:
        paddle1_y += VELOCITA_PADDLE
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= VELOCITA_PADDLE
    if keys[pygame.K_DOWN] and paddle2_y < A_SCHERMO - PADDLE_ALTEZZA:
        paddle2_y += VELOCITA_PADDLE

    # Movimento della pallina
    x_pallina += dx_pallina
    y_pallina += dy_pallina

    # COLLISIONI
    # =======
    # Collisione con il bordo superiore e inferiore
    if y_pallina <= grandezza_pallina or y_pallina >= A_SCHERMO - grandezza_pallina:
        dy_pallina *= -1

    # Collisione con il paddle sinistro
    if (x_pallina - grandezza_pallina <= PADDLE_LARGHEZZA and
        paddle1_y < y_pallina < paddle1_y + PADDLE_ALTEZZA):
        dx_pallina *= -1
        x_pallina = PADDLE_LARGHEZZA + grandezza_pallina 

    # Collisione con il paddle destro
    if (x_pallina + grandezza_pallina >= L_SCHERMO - PADDLE_LARGHEZZA and
        paddle2_y < y_pallina < paddle2_y + PADDLE_ALTEZZA):
        dx_pallina *= -1
        x_pallina = L_SCHERMO - PADDLE_LARGHEZZA - grandezza_pallina 

    # Reset della pallina se va oltre i bordi
    if x_pallina < 0 or x_pallina > L_SCHERMO:

        if x_pallina < 0:  # Punto per il giocatore di destra
            punti_giocatore_2 += 1
            x_pallina, y_pallina = L_SCHERMO // 2, A_SCHERMO // 2
            dx_pallina = -dx_pallina

        if x_pallina > L_SCHERMO:  # Punto per il giocatore di sinistra
            punti_giocatore_1 += 1
            x_pallina, y_pallina = L_SCHERMO // 2, A_SCHERMO // 2
            dx_pallina = -dx_pallina

        # x_pallina, y_pallina = L_SCHERMO // 2, A_SCHERMO // 2
        # dx_pallina = -dx_pallina



    # Disegno di tutto 
    schermo.fill((0, 0, 0))
    pygame.draw.circle(schermo, BIANCO, (x_pallina, y_pallina), grandezza_pallina)
    pygame.draw.rect(schermo, BIANCO, (0, paddle1_y, PADDLE_LARGHEZZA, PADDLE_ALTEZZA))
    pygame.draw.rect(schermo, BIANCO, (L_SCHERMO - PADDLE_LARGHEZZA, paddle2_y, PADDLE_LARGHEZZA, PADDLE_ALTEZZA))
    font = pygame.font.Font(None, 36)
    testo_punti = font.render(f"{punti_giocatore_1} - {punti_giocatore_2}", True, BIANCO)
    schermo.blit(testo_punti, (L_SCHERMO // 2 - 20, 20))
    pygame.display.update()
    pygame.time.delay(30)
