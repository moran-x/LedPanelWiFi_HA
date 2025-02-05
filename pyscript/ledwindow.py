led_lamps_ip = ["10.1.30.44", "10.1.30.40"]
led_lamps_name = ["LedWiFiTree", "LedWiFiWindow"]

import json
import subprocess
import paho.mqtt.client as mqtt

mqtt_username = "mqtt_user"
mqtt_password =  "pass"
mqtt_host = "127.0.0.1"
mqtt_port = 1883

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
client.connect(mqtt_host, mqtt_port)

@service
def get_params():
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        
        params = ["VR", "HN", "BR", "PS", "DM", "RM", "EF", "SM", "EN", "UP", "FM", "IP"]

        for param in params:
            command = json.dumps({'e': 'cmd', 'd': '$6 7|'+param})
            command_ws = 'echo \''+command+'\' | /config/websocat -n1 ws://'+led_lamp_ip+'/ws'
            result = subprocess.Popen(command_ws, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            line = result.stdout.readline()
            x = json.loads(line)
            y = json.loads(x["d"])
            client.publish(led_lamps_name[idx]+'/'+param, payload=str(y[param]), qos=0, retain=False)


@service
def LedWindow_on_off(led_ip=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd = "binary_sensor."+led_lamps_name[idx].lower()+"_ps"
            sensor_state = state.get(cmd)
            if sensor_state == "on":
                command = json.dumps({'e': 'cmd', 'd': '$1 0'})
            else:
                command = json.dumps({'e': 'cmd', 'd': '$1 1'})
            command_ws = 'echo \''+command+'\' | /config/websocat -n1 ws://'+led_lamp_ip+'/ws'
            subprocess.Popen(command_ws, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            get_params()

