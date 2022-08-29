import re
import csv
import serial

ser = serial.Serial()
ser.port = "COM4"
ser.baudrate = 115200
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.open()

while True:
    string = str(ser.readline())
    print(string)
    if "IMEI:" in string:
        imei = re.findall('[\bIMEI:] (\d+[0-9]+\d)', string)
        with open('IMEI.csv', mode='a', newline = '') as x:
            writer = csv.writer(x)
            for i in imei:
                writer.writerow([imei[0]])
        break
