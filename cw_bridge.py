import evdev
from evdev import ecodes, InputDevice, UInput
import sys

# Nome esatto che Linux assegna alla parte "mouse" del tuo adattatore
TARGET_DEVICE_NAME = "HID [INSERISCI_IL_TUO_CODICE]"

def find_cw_adapter():
    """Cerca tra tutti i dispositivi collegati quello che si chiama come il tuo adattatore e che gestisce eventi del mouse (relativi o clic)"""
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        # Cerchiamo il nome giusto e ci assicuriamo che sia quello che invia i clic (BTN_LEFT)
        if TARGET_DEVICE_NAME in device.name:
            capabilities = device.capabilities()
            if ecodes.EV_KEY in capabilities and ecodes.BTN_LEFT in capabilities[ecodes.EV_KEY]:
                return device.path
    return None

DEVICE_PATH = find_cw_adapter()

if not DEVICE_PATH:
    print(f"Errore: Adattatore '{TARGET_DEVICE_NAME}' non trovato.")
    print("Assicurati che sia collegato alla porta USB.")
    sys.exit(1)

try:
    # 1. Python si collega al tuo adattatore USB usando il percorso trovato in automatico
    mouse_cw = InputDevice(DEVICE_PATH)
    
    # 2. Il comando grab() impedisce a Linux di usare i clic come vero mouse
    mouse_cw.grab() 
    
    # 3. Creiamo la tastiera virtuale
    tastiera_virtuale = UInput()
    
    print(f"Adattatore trovato su: {DEVICE_PATH}")
    print(f"Collegamento riuscito a: {mouse_cw.name}")
    print("In ascolto... (Premi CTRL+C per spegnere il programma se avviato da terminale)")

    # 4. Inizia il ciclo di ascolto
    for event in mouse_cw.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.code == ecodes.BTN_LEFT:
                tastiera_virtuale.write(ecodes.EV_KEY, ecodes.KEY_Z, event.value)
                tastiera_virtuale.syn()
            elif event.code == ecodes.BTN_RIGHT:
                tastiera_virtuale.write(ecodes.EV_KEY, ecodes.KEY_X, event.value)
                tastiera_virtuale.syn()

except PermissionError:
    print("Errore: non hai i permessi. Esegui con sudo!")
except Exception as e:
    print(f"Errore imprevisto: {e}")
finally:
    try:
        mouse_cw.ungrab()
        tastiera_virtuale.close()
    except:
        pass
    print("\nProgramma terminato.")
    sys.exit(0)
