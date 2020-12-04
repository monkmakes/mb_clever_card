import serial
import serial.tools.list_ports
import webbrowser

print("Select the port to use.")
ports = sorted(serial.tools.list_ports.comports())
i = 1
for port in ports:
    print("[{}]: {}".format(i, port))
    i += 1
port_num_str = input("Enter number for port:")
try:
    port_num = int(port_num_str) - 1
    print(port_num)
    interface = ports[port_num].device
    print("Connecting to: " + str(interface))
    ser = serial.Serial(interface, 115200)
    print("Connected to: " + interface)
except:
    print("Connection failed. Quitting.")
    exit()

while True:
    url = ser.readline()[:-2].decode("utf-8")  # remove LF, CR turn into string
    if url:
        print("URL: " + str(url))
        webbrowser.open(url, new=1)
        