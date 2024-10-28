# Guida per l'attività Pong

## Obiettivi
- Familiarizzare con `pygame` e le basi della programmazione di giochi.
- Capire la struttura di un ciclo di gioco e come gestire input, logica e grafica.
- (opzionale) Implementare un contatore dei punti per aggiungere dinamica al gioco.

## Requisiti
- Python installato
- `pygame` installato: `pip install pygame`
- `IDLE` o un editor di testo per scrivere il codice.


## 0. Setup e introduzione
Prima di iniziare, assicurarsi che tutti abbiano installato `python` e `pygame` e abbiano scaricato il file `pong_0_template.py` sul desktop.

Se sono su **Linux**, **IDLE** bisogna installarlo **come pacchetto**.

È bene fare una **piccola introduzione sul piano cartesiano** nei giochi.

Il piano cartesiano è un sistema di coordinate che ci permette di posizionare oggetti nello spazio. In altre parole, è un modo per **rappresentare la posizione di un oggetto** in un gioco.

È formato da due assi: **l'asse x e l'asse y**. L'asse **x** rappresenta la **larghezza** dello schermo, mentre l'asse **y** rappresenta l'**altezza** dello schermo.

In Pygame, l'origine del piano, cioè da dove "nasce", si trova nell'**angolo in alto a sinistra dello schermo**, con l'asse y che cresce verso il basso.

Quindi, se vogliamo posizionare un oggetto al centro dello schermo, dovremo calcolare le coordinate x e y in base alla larghezza e all'altezza dello schermo.

Per muovere un oggetto **in alto** bisogna **diminuire il valore dell'asse y**, mentre per muoverlo **in basso** bisogna **aumentare il valore dell'asse y**.

Pong è un gioco molto semplice, composto da due "paddle" che sono i giocatori, e una "pallina" che rimbalza tra i paddle. Il gioco termina quando la pallina esce dai lati sinistro o destro dello schermo.

I ragazzi iniziano con il template base, gia scaricato sul desktop, che contiene:
- La struttura del ciclo principale (`while True`) in `pygame`.
- Una finestra vuota su cui costruire il gioco.
- Dei commenti e dei puntini di sospensione per aiutare a capire dove bisogna scrivere il codice.

Introduciamo anche le variabili: sono delle piccole scatole in cui è possibile mettere qualcosa, ad esempio dei numeri, delle lettere eccetera.

### Cosa devono fare i ragazzi
- Far apparire una semplice pallina (un cerchio) al centro
- Far apparire i paddle (giocatori)
- Far muovere i paddle in alto e in basso, così da introdurre la logica base del movimento.
- Far muovere la pallina.

Sulla loro guida hanno tutti i vari pezzetti di codice che devono inserire nel template.

## Fase 1: paddle e pallina
In questa fase bisogna spiegare:
1. come disegnare la pallina e i paddle sullo schermo
2. come far muovere i paddle e la pallina

Per disegnare: prima si impostano tutti i valori FUORI dal while, e alla fine del codice, si spiega COME bisonga fare per farli apparire.

Prima quindi bisogna spiegare come disegnare la pallina e i paddle sullo schermo, impostando i valori delle coordinate e delle dimensioni dei paddle e della pallina.

Alla fine del codice, bisogna fargli disegnare i paddle e la pallina sullo schermo (una pallina e due rettangoli).

Bisogna spiegare pezzetto per pezzetto come fare, e far scrivere il codice ai ragazzi.

Il codice di riferimento è in `pong_1_gfx_base.py`.

Per muovere i paddle: si spiega che bisogna usare gli eventi di `pygame` per catturare i tasti premuti e far muovere i paddle di conseguenza.

### Cosa devono fare i ragazzi
1. **Impostare** la pallina e i paddle all'inizio del codice
2. **Disegnare** la pallina e i paddle alla fine del codice
3. Far **muovere** i paddle con i tasti freccia scrivendo un semplice codice per catturare gli eventi
4. Far **muovere** la pallina

Il codice di riferimento è in `pong_2_gfx_e_movimento.py`.


## Fase 2: Collisioni, reset e versione base
La versione base include:
- Movimento della pallina e dei paddle.
- Collisione della pallina con i bordi e i paddle.
- Riposizionamento della pallina al centro quando esce dai lati.

Prima gli si spiega il concetto di **collisione e rimbalzo**: la pallina deve rimbalzare sui bordi e sui paddle, e quando esce dai lati, bisogna riposizionarla al centro.

Questo si fa controllando le coordinate della pallina e dei paddle, e facendo in modo che la pallina cambi direzione quando colpisce i bordi o i paddle.

Il codice di riferimento è in `pong_2_collisioni.py`.

Ultimo passaggio è spiegare come fare il **reset della pallina**: quando la pallina esce dai lati, bisogna riposizionarla al centro e farla ripartire.

Il codice di riferimento è in `pong_3_reset_e_base.py`.

### Cosa devono fare i ragazzi
- Aggiungere le collisioni
- Aggiungere il reset
- Giocare con le velocità della pallina e dei paddle



## Fase 3: contatore dei punti e altro
Nella versione avanzata, il codice aggiunge:
- Un contatore per tenere traccia dei punti di ciascun giocatore.
- Visualizzazione del punteggio sullo schermo.

Bisogna spiegare loro come funziona il **contatore dei punti**: ogni volta che la pallina esce dai lati, bisogna assegnare un punto al giocatore opposto.

Questo si fa controllando le coordinate della pallina e dei paddle, e assegnando un punto al giocatore opposto quando la pallina esce dai lati: quindi quando la pallina esce dal lato sinistro, il giocatore a destra guadagna un punto, e viceversa.

Il codice di riferimento è in `pong_3_avanzata_con_punteggio.py`.

### Cosa devono fare i ragazzi
- Aggiungere il contatore per assegnare i punti ai giocatori quando la pallina supera i paddle
- Gestire la visualizzazione dei punti



## Personalizzazioni
- I **colori** possono essere cambiati a piacimento, andando ovviamente a definire piu colori rispetto a BIANCO=(255,255,255). I colori sono RGB, i paddle e la pallina possono ovviamente non essere disegnati con "BIANCO" ma con altri colori.

- I paddle possono essere resi **piu lunghi o piu corti**, basta cambiare i valori delle coordinate `paddle1_y` e `paddle2_y`

- La **velocità della pallina** può essere cambiata, così come la velocità dei paddle `velocita_paddle`

- La **dimensione della pallina** può essere resa più grande o più piccola, andando a modificare `grandezza_pallina`

- Si può **modificare e definire cosa succede quando un giocatore guadagna un punto**, ad esempio cambiando il colore del paddle o della pallina o allungando / accorciando i paddle, o cambiando la dimensione della pallina.

- Si può **modificare il testo** andando a cambiare la stringa `font.render` e il colore del testo.

- **Randomicità** di **dove inizia la palla**, usare `random.randint` per generare un numero casuale tra due valori.