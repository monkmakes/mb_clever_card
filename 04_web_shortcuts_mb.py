from microbit import *
import time

links = {
  "903F9775": "http://monkmakes.com",
  "C78275A6": "http://wikipedia.org"
}

def read_card():
    uart.init(baudrate=9600, tx=pin8, rx=pin1)
    time.sleep(0.1)
    card_code = None
    while not card_code:
        if uart.any():
            msg_bytes = uart.read()
            msg_str = str(msg_bytes, 'UTF-8')[:8]
            if msg_str[0] >= '0': # ignore \r\n which arrives as separate serial packet
                card_code = msg_str
    uart.init(115200) # reconnect to USB
    return card_code

while True:
    card = read_card()
    if card:
        display.show(Image.CHESSBOARD)
        time.sleep(0.5)
        display.clear()
        print(links[card])
