from microbit import *

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

while True:
    display.scroll(read_card())
