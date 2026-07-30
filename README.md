# USB CW Key Adapter Bridge for Linux
*(Scroll down for English version)*

🇮🇹 ITALIANO

Questo script Python risolve un problema comune per i radioamatori che utilizzano adattatori USB economici per tasti telegrafici (CW) su Linux. Molti di questi moduli hardware vengono riconosciuti dal sistema operativo come un mouse (inviando clic del tasto destro e sinistro) anziché come una tastiera. Questo impedisce di usarli con software di allenamento come "wr-cw-trainer", che si aspettano l'input da tastiera (es. tasti Z e X per i paddle).

Lo script intercetta i "clic" dell'adattatore prima che muovano il puntatore del mouse e li trasforma nella pressione dei tasti "Z" (punti) e "X" (linee) su una tastiera virtuale.

## 1. Requisiti di sistema
È necessario installare la libreria "evdev" per permettere a Python di dialogare con le porte USB. Apri il terminale e digita:

    sudo apt update
    sudo apt install python3-evdev

## 2. Identificare e configurare il proprio Adattatore (FONDAMENTALE)
Per funzionare, lo script deve conoscere il codice identificativo esatto del tuo adattatore USB. All'interno del file "cw_bridge.py", la variabile è impostata in questo modo:
TARGET_DEVICE_NAME = "HID [INSERT_YOUR_CODE_HERE]"

Devi trovare il tuo codice e sostituirlo:
1. Collega il tuo adattatore USB al computer.
2. Apri il terminale e digita: lsusb
3. Cerca nell'elenco la riga del tuo dispositivo (spesso indicato come HID generico o simile). Annota il codice di 8 caratteri separati da due punti (ad esempio 413d:2107 o 1a86:7523).
4. Apri il file cw_bridge.py con un editor di testo e sostituisci [INSERT_YOUR_CODE_HERE] con il tuo codice. 
   Esempio: se il tuo codice è 413d:2107, la riga dovrà diventare esattamente:
   TARGET_DEVICE_NAME = "HID 423d:2105"
5. Salva il file.

## 3. Avvio da Terminale
Per poter leggere i segnali USB, lo script ha bisogno dei permessi di amministratore (sudo). Apri il terminale nella cartella in cui hai salvato il file e digita:

    sudo python3 cw_bridge.py

Per spegnere il programma e ripristinare il normale funzionamento del mouse, premi CTRL+C nel terminale.

## 4. Creare un Lanciatore sul Desktop (Consigliato per Linux Mint / Ubuntu)
Per evitare di aprire il terminale a mano ogni volta, puoi creare una comoda icona sul desktop:
1. Fai clic col tasto destro sul Desktop e scegli "Crea un nuovo lanciatore qui...".
2. Compila i campi in questo modo:
   * Tipo: Applicazione nel terminale (oppure spunta "Esegui nel terminale"). Questo è obbligatorio per poter inserire la password.
   * Nome: Ponte CW
   * Comando: sudo python3 /percorso/completo/della/tua/cartella/cw_bridge.py
3. Salva e fai doppio clic sull'icona. Si aprirà una finestrella in cui inserire la tua password. Lasciala aperta mentre ti alleni in CW e chiudila cliccando sulla "X" quando hai finito!

---

🇬🇧 ENGLISH

This Python script solves a common issue for Ham Radio operators using inexpensive USB CW key adapters on Linux. Many of these hardware modules are recognized by the operating system as a mouse (sending left and right clicks) rather than a keyboard. This prevents them from being used with Morse code training software like "wr-cw-trainer", which expect keyboard inputs (e.g., Z and X keys for paddles).

The script intercepts the adapter's "clicks" before they move the mouse pointer and translates them into "Z" (dit) and "X" (dah) keystrokes on a virtual keyboard.

## 1. System Requirements
You need to install the "evdev" library to allow Python to interact with USB input devices. Open your terminal and run:

    sudo apt update
    sudo apt install python3-evdev

## 2. Identify and Configure Your Adapter (IMPORTANT)
To work properly, the script needs to know the exact hardware ID of your USB adapter. Inside the "cw_bridge.py" file, the variable is set as follows:
TARGET_DEVICE_NAME = "HID [INSERT_YOUR_CODE_HERE]"

You must find your code and replace the placeholder:
1. Plug your USB adapter into the computer.
2. Open the terminal and type: lsusb
3. Find your device in the list (often labeled as a generic HID device). Note the 8-character code separated by a colon (e.g., 413d:2107 or 1a86:7523).
4. Open the cw_bridge.py file with a text editor and replace [INSERT_YOUR_CODE_HERE] with your code. 
   Example: if your code is 413d:2107, the line must become exactly:
   TARGET_DEVICE_NAME = "HID 413d:2107"
5. Save the file.

## 3. Running from Terminal
To read raw USB signals, the script requires root privileges (sudo). Open the terminal in the folder where you saved the script and run:

    sudo python3 cw_bridge.py

To stop the program and restore normal mouse functionality, press CTRL+C in the terminal.

## 4. Creating a Desktop Launcher (Recommended for Linux Mint / Ubuntu)
To avoid opening the terminal manually every time, you can create a handy desktop shortcut:
1. Right-click on your Desktop and select "Create a new launcher here...".
2. Fill in the fields as follows:
   * Type: Application in Terminal (or check "Run in terminal"). This is required so you can type your password.
   * Name: CW Bridge
   * Command: sudo python3 /full/path/to/your/folder/cw_bridge.py
3. Save and double-click the icon. A small terminal window will open asking for your password. Leave it open while you practice CW, and simply close the window when you are done!

---
73 de IW5DGQ, Ricky
