import serial
import csv
import os
from datetime import datetime


ser = serial.Serial('/dev/ttyACM0', 9600)


def get_data_from_arduino():
    data = ser.readline().decode().strip()
    d = data.split('\t')
    return d


def serial_to_csv():
    with open('home_data.csv', 'a') as f:
        writer = csv.writer(f)
        if os.path.getsize('home_data.csv') == 0:
            field = ['time', 'temperature', 'humidity',
                'pressure', 'sound', 'distance', 'light']
            writer.writerow(field)
        else:
            data = list()
            while len(data) != 6 :
                data = get_data_from_arduino()
                now = datetime.utcnow()
                f_now = now.strftime('%Y-%m-%d %H:%M:%S')

            values = [str(d) for d in data]
            writer.writerow([f_now] + values)