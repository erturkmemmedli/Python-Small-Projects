import paho.mqtt.client as mqtt
from datetime import datetime
import csv  

header = ['Vaxt',
          'Mexaniki göstərici - VmT(m3)',
          'VmD - VmD(m3)',
          'Elektron göstərici - VbT(m3)',
          'VbD - VbD(m3)',
          'Ölçmə şəraitində sərfiyyat - Qm(m3/h)',
          'Baza şəraitində sərfiyyat - Qb(m3/h)',
          'Təzyiq - p(bar)',
          'Temperatur - T(C)',
          'Korreksiya əmsalı - C',
          'Qazın sıxılma əmsalı - K',
          'Baza şəraitində xüsusi çəki - Rhob(kg/m3)']

with open('C:/Users/HP/Documents/Nərimanov EK-220.csv', mode='w', encoding='utf-16', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe('ek220', qos = 0)

def on_log(client, userdata, level, buff):
    print(buff)
    
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    data = []
    string = str(msg.payload)
    string = string[3:len(string)-2]   
    my_list = string.split(',')  
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    data.append(time)
    for i in range(len(my_list)):
        if i in [1, 2, 3, 4, 6, 7, 8]:
            if my_list[i][5:len(my_list[i])-1] == '':
                data.append(None)
            else:
                data.append(float(my_list[i][5:len(my_list[i])-1]))
        elif i in [9, 10, 11, 12]:
            if my_list[i][6:len(my_list[i])-1] == '':
                data.append(None)
            else:
                data.append(float(my_list[i][6:len(my_list[i])-1]))
    with open('C:/Users/HP/Documents/Nərimanov EK-220.csv', mode='a', encoding='utf-16', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
client = mqtt.Client("Erturk")
client.username_pw_set(username = "***", password = "***")
client.on_log = on_log
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker.")
try:
    client.connect(host = "***.***.***.***", port = 1883, keepalive = 60, bind_address = "")
except:
    print("Connection failed!")
    exit(1)

client.loop_forever()
