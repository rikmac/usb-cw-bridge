#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CW Bridge - USB CW Trainer Interface
# Copyright (C) 2026 Riccardo Casa (IW5DGQ)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
