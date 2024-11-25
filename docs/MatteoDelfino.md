
### Eseguire l'ambiente di sviluppo Python IDLE da un ambiente virtuale

**N.B.** *La seguente guida è intesa per il partecipante (Matteo Delfino) al CoderDojo del 23/11/2024, al fine di eseguire programmi in Python che richiedono l'utilizzo della libreria **Pygame**. 
Poiché quest'ultima non supporta l'ultima versione di Python 3.13, durante la sessione di tutoraggio, è stato creato un ambiente virtuale Python 3.10 sul computer dei partecipanti. La cartella che lo contiene si trova alla destinazione **C:\CoderDojo\VENV**. 
Ma, data la natura dei computer e le differenti configurazioni dei singoli, eventuali errori sono dovuti essere trattati separatamente e con metodologie/approcci differenti. Di seguito viene trattato come eseguire l'IDLE di Python 3.10.
Questa guida è, quindi, applicabile a tutti coloro che trovano lo stesso errore. Ovvero l'errore "**pygame not found**", quando viene lanciato il programma python dall'IDLE 3.10, nonostante pygame sia installato.*

---
1. Lanciare il prompt dei comandi per eseguire dei comandi (**cmd**): Premere il tasto ***Windows (⊞) + R***;
2. Attivare l'ambiente virtuale di Python 3.10 eseguendo il seguente comando dal cmd e premendo invio: ***call C:\CoderDojo\VENV\Scripts\activate.bat***
3. Sul lato sinistro del cmd dovrebbe esserci un ***(VENV)*** ; ora l'ambiente virtuale è attivo. Eseguire, quindi, il seguente comando per lanciare l'IDLE presente nell'ambiente: ***python -m idlelib.idle***
4. Una volta apparsa la finestra dell'IDLE, aprire il file desiderato tramite: **File > Open**
5. Eseguire il programma con ***Run***, come visto durante l'evento.
6. **N.B.** Per tutta la durata che l'IDLE viene utilizzato, non cliccare ***MAI*** sulla **X** del cmd, altrimenti la finestra dell'IDLE verrà chiusa.

---

Con questo si conclude la mini-guida. 
Ci scusiamo per i disagi causati dagli errori di compatibilità tra le versioni di Python e delle librerie utilizzate. In prima battuta abbiamo menzionato sul sito di scaricare Python 3.13, data la sua natura stabile e ultima. Successivamente, però, durante la fase di testing  abbiamo notato che la libreria Pygame non supportava la versione 3.13, e ci siamo dovuti spostare sulla 3.10. Purtroppo, non è stato possibile aggiornare questa informazione in modo efficiente con le famiglie. La reinstallazione di Python e/o il cambio di configurazione del computer nuovamente, avrebbe potuto causare imprevisti scomodi per tutti. Soprattutto coloro che si affacciano per la prima volta alla programmazione e al mondo dell'informatica. Abbiamo, quindi, optato per la scrittura di un programma automatico che potesse verificare e installare la versione giusta di Python, in loco. Purtroppo, però, come detto in precedenza ogni computer ha configurazioni dell'utente differenti, il che può portare a situazioni straordinarie, che devono essere trattate individualmente.
Questo è stato momento per imparare, anche per tutti noi. 
Vi aspettiamo numerosi alle prossime edizioni del CoderDojo!

--CoderDojo SPQR 
