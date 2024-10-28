#!/bin/bash

# Controlla se Python 3.10 è già installato
if ! command -v python3.10 &> /dev/null; then
    echo "Python 3.10 non è installato. Installazione in corso dalla chiavetta USB..."
    
    # Installa Python 3.10 dal file .pkg presente sulla chiavetta USB
    sudo installer -pkg ./installers/python-3.10.0-macosx10.9.pkg -target /
    
    echo "Python 3.10 è stato installato con successo."
else
    echo "Python 3.10 è già installato."
fi

# Installa Pygame
echo "Installazione di Pygame in corso..."
python3.10 -m pip install ./installers/pygame-2.1.2-cp310-cp310-macosx_10_9_x86_64.whl --no-index --find-links=.
echo "Installazione di Pygame completata!"

read -p "Premi Invio per terminare."
