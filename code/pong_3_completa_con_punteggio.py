import pygame
import sys

pygame.init()

# Dimensioni della finestra e colori
L_schermo, A_schermo = 800, 600
bianco = (255, 255, 255)

# Inizializzazione della finestra
schermo = pygame.display.set_mode((L_schermo, A_schermo))

# Posizione e velocità della pallina
x_pallina, y_pallina = L_schermo // 2, A_schermo // 2
dx_pallina, dy_pallina = 5, 5
grandezza_pallina = 10

paddle1_y, paddle2_y = A_schermo // 2, A_schermo // 2
paddle_larghezza, paddle_altezza = 10, 100
velocita_paddle = 7

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
        paddle1_y = paddle1_y - velocita_paddle
    if keys[pygame.K_s] and paddle1_y < A_schermo - paddle_altezza:
        paddle1_y = paddle1_y + velocita_paddle
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y = paddle2_y - velocita_paddle
    if keys[pygame.K_DOWN] and paddle2_y < A_schermo - paddle_altezza:
        paddle2_y = paddle2_y + velocita_paddle

    # Movimento della pallina
    x_pallina = x_pallina + dx_pallina
    y_pallina = y_pallina + dy_pallina

    # COLLISIONI
    # =======
    # Collisione con il bordo superiore e inferiore
    if y_pallina <= grandezza_pallina or y_pallina >= A_schermo - grandezza_pallina:
        dy_pallina = dy_pallina * -1

    # Collisione con il paddle sinistro
    if (x_pallina - grandezza_pallina <= paddle_larghezza and
        paddle1_y < y_pallina < paddle1_y + paddle_altezza):
        dx_pallina = dx_pallina * -1
        x_pallina = paddle_larghezza + grandezza_pallina 

    # Collisione con il paddle destro
    if (x_pallina + grandezza_pallina >= L_schermo - paddle_larghezza and
        paddle2_y < y_pallina < paddle2_y + paddle_altezza):
        dx_pallina = dx_pallina * -1
        x_pallina = L_schermo - paddle_larghezza - grandezza_pallina 

    # Reset della pallina se va oltre i bordi
    if x_pallina < 0 or x_pallina > L_schermo:
        x_pallina, y_pallina = L_schermo // 2, A_schermo // 2
        dx_pallina = -dx_pallina

        if x_pallina < 0:
            punti_giocatore_2 = punti_giocatore_2 + 1

        if x_pallina > L_schermo: 
            punti_giocatore_1 = punti_giocatore_1 + 1


    # Disegno di tutto 
    schermo.fill((0, 0, 0))
    pygame.draw.circle(schermo, bianco, (x_pallina, y_pallina), grandezza_pallina)
    pygame.draw.rect(schermo, bianco, (0, paddle1_y, paddle_larghezza, paddle_altezza))
    pygame.draw.rect(schermo, bianco, (L_schermo - paddle_larghezza, paddle2_y, paddle_larghezza, paddle_altezza))
    font = pygame.font.Font(None, 36)
    testo_punti = font.render(f"{punti_giocatore_1} - {punti_giocatore_2}", True, bianco)
    schermo.blit(testo_punti, (L_schermo // 2 - 20, 20))
    pygame.display.update()
    pygame.time.delay(30)
