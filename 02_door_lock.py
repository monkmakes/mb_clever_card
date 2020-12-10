from microbit import *
import time

uart.init(baudrate=9600, tx=pin8, rx=pin1)

def read_card():
    card_code = None
    while not card_code:
        if uart.any():
            msg_bytes = uart.read()
            msg_str = str(msg_bytes, 'UTF-8')[:8]
            if msg_str[0] >= '0': # ignore \r\n which arrives as separate serial packet
                card_code = msg_str
    return card_code

def allow_entry():
    display.show(Image.YES)
    pin0.write_digital(0)
    pin2.write_digital(1)
    time.sleep(2)
    pin2.write_digital(0)
    display.clear()

def deny_entry():
    display.show(Image.NO)
    pin0.write_digital(1)
    pin2.write_digital(0)
    time.sleep(2)
    pin0.write_digital(0)
    display.clear()

while True:
    card = read_card()
    if card == "903F9775":   # change me
        allow_entry()
    elif card == "8063995E": # change me
        allow_entry()
    else:
        deny_entry()