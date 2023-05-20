import bluetooth

# Set the Bluetooth address of the HC-06 module
address = "00:22:09:01:29:5c" # replace with your module's address

# create a Bluetooth socket and connect to the Arduino
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((address, 1))

# send a string of text to the Arduino
text = "Code: example. RUN*"
sock.send(text)

# wait for a response from the Arduino
response = ""
data = sock.recv(1024)
response += data.decode()

# print the response from the Arduino
print("Received: " + response)
if response == "200":
    print("Code is executing")
# close the Bluetooth socket
sock.close()
