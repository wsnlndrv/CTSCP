#!/usr/bin/python
# -*- coding: utf-8; -*-

from evdev import InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/by-id/usb-CHESEN_USB_Keyboard-event-kbd') # Ruta absoluta y nombre del teclado secundario
dev.capabilities(verbose=True)
dev.leds(verbose=True)
dev.active_keys(verbose=True)
dev.grab()

dev.set_led(ecodes.LED_NUML, 1) # Activamos el led block num, ¿por qué no?

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        #print(categorize(event))
        key = categorize(event)
    if event.type == ecodes.EV_KEY:        
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_ESC':
                print("Escape!")
