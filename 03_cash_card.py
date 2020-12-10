from microbit import *
import time

cards = {
  "903F9775": { "name": "Simon", "balance": 0 },
  "8063995E": { "name": "Linda", "balance": 0 },
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
    uart.init(115200)
    return card_code

def save_cards():
    with open('cards.txt', 'w') as file:
        for key, person in cards.items():
            file.write(key + ',' + person['name'] + ',' + str(person['balance']) + '\n')

def load_cards():
    try:
        with open('cards.txt', 'r') as file:
            contents = file.read()
            lines = contents.split('\n')
            for line in lines:
                parts = line.split(',')
                if parts and len(parts) >= 3:
                    card_id, name, balance = parts
                    cards[card_id] = { 'name': name, 'balance': int(balance)}
    except Exception as e:
        print("Couldn't load cards - may be first run")
        print(e)

load_cards()

while True:
    display.show(Image.ARROW_S)
    id = read_card()
    if id in cards:
        details = cards[id]
        display.scroll(details['name'] + " " + str(details['balance']))
        display.show("?")
        while True:
            if (button_a.is_pressed() and button_b.is_pressed()):
                save_cards()
                display.show(Image.YES)
                time.sleep(0.5)
                break
            elif button_a.is_pressed():
                time.sleep(0.3)
                if not button_b.is_pressed():
                    details['balance'] -= 1
                    display.scroll(str(details['balance']))
            elif button_b.is_pressed():
                time.sleep(0.3)
                if not button_a.is_pressed():
                    details['balance'] += 1
                    display.scroll(str(details['balance']))
    else:
        display.scroll("??? " + id)