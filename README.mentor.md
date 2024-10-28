# Pypong
Pypong è un progetto per insegnare ai ragazzi a programmare in Python, usando il modulo Pygame.

Il progetto è diviso in 4 attività, ognuna delle quali aggiunge nuove funzionalità al gioco Pong. 

Le attività sono:

1. Grafica base e movimento
2. Collisioni e reset
3. Punteggio
4. Avanzate, personalizzazioni

## Struttura della repo
- `code`: questa cartella contiene tutti i sorgenti del progetto. Nello specifico:
  - `pong_0_template`: template per l'attività Pong che i ragazzi devono scaricare e mettere sul desktop
  - `pong_1_gfx_base`: ha solo la grafica di base del gioco, senza alcuna interazione
  - `pong_1_gfx_e_movimento`: ha la grafica di base e il movimento della pallina e delle racchette
  - `pong_2_collisioni`: le collisioni sono state implmentate, sia delle racchette che della pallina che dei muri
  - `pong_2_reset_e_base`: aggiunto il reset del gioco. La versione base termina qui
  - `pong_3_completa_con_punteggio`: aggiunto il punteggio

- `docs`: contiene la documentazione sia interna che esterna, rispettivamente:
    - [`guida-mentor`](docs/guida-mentor.md): guida per i mentor che spiega come fare le attività ai ragazzi. I frammenti di codice non sono inclusi, poiché i file sono già presenti nella cartella `code` e nella guida per i ragazzi
    - [`guida-ragazzi`](docs/guida-utente.md): guida per i ragazzi passo passo, con immagini e frammenti di codice da copiare
    - `img`: immagini per la guida dei ragazzi


## Troubleshooting
- Q. Il gioco non parte, cosa posso fare?
  - A. Assicurati di avere installato Pygame. Se non l'hai fatto, puoi installarlo con `pip install pygame`.

- Q. Il gioco si blocca o non risponde, cosa posso fare?
  - A. Assicurati di aver chiuso eventuali finestre di Pygame aperte.

- Q. Il gioco non funziona come dovrebbe, cosa posso fare?
  - A. Controlla il codice e assicurati di aver seguito tutti i passaggi della guida.


## Personalizzazioni
A fine della guida mentor, è presente una parte dedicata alle personalizzazioni, dove si spiegano alcune idee per migliorare il gioco e renderlo più interessante.

Per ulteriori riferimenti, vedere la documentazione di [Pygame](https://www.pygame.org/docs/).