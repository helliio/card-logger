import datetime
import os


def logger(message):
    time = datetime.datetime.now().strftime("%d.%m.%y;%H:%M")
    message = time + ";" + message
    print(message)
    f = open("log.csv", "a+")
    f.write(message + "\n")
    f.flush()
    os.fsync(f.fileno())
    f.close()


def get_input_loop():
    while True:
        x = input()
        logger(x)


get_input_loop()
