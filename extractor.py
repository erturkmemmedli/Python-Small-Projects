# Hello World program in Python
import csv      
import serial
import argparse

parser = argparse.ArgumentParser(description='Imei And Mac Extractor')
parser.add_argument('-p', '--port', help="'Serial port device' Com5", default='COM5')
args = parser.parse_args()
ser = serial.Serial(args.port, 115200)
imei="IMEI:"
mac="Mac:"


def format_fix(string,endline):
    string=string.replace("b'IMEI: ", "").replace("b'Mac: ", "").replace(r"\r\n'", r"")  
    print(string)
    with open('imei_mac.csv','a') as fd:
     if endline is True: 
      fd.write(string + '\r')
     elif endline is False:
      fd.write(string+",")    



while True:
 cc=str(ser.readline())
 print(cc)
 if mac in cc:
    format_fix(cc,False)
 if imei in cc:
    format_fix(cc,True)
    break
