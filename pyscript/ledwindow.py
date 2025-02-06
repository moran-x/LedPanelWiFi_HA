led_lamps_ip = ["10.1.30.40"]
led_lamps_name = ["LedWiFiWindow"]

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
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state = state.get(cmd_ps)
            if sensor_state == "on":
                command = json.dumps({'e': 'cmd', 'd': '$1 0'})
            else:
                command = json.dumps({'e': 'cmd', 'd': '$1 1'})
            command_ws = 'echo \''+command+'\' | /config/websocat -n1 ws://'+led_lamp_ip+'/ws'
            #log.info(command_ws)
            subprocess.Popen(command_ws, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            get_params()

@service
def LedWindow_brightness(led_ip=None, brightness=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd_br = "light."+led_lamps_name[idx].lower()+"_br"
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state = state.get(cmd_ps)
            if sensor_state == "on":
                command = json.dumps({'e': 'cmd', 'd': '$4 0 '+str(brightness)})
                command_ws = 'echo \''+command+'\' | /config/websocat -n1 ws://'+led_lamp_ip+'/ws'
                subprocess.Popen(command_ws, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
                get_params()


@service
def LedWindow_random_effect(led_ip=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd_rm = "switch."+led_lamps_name[idx].lower()+"_rm"
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state_ps = state.get(cmd_ps)
            sensor_state_rm = state.get(cmd_rm)
            if sensor_state_ps == "on":
                if sensor_state_rm == "on":
                    command = json.dumps({'e': 'cmd', 'd': '$16 5 0'})
                else:
                    command = json.dumps({'e': 'cmd', 'd': '$16 5 1'})
                command_ws = 'echo \''+command+'\' | /config/websocat -n1 ws://'+led_lamp_ip+'/ws'
                subprocess.Popen(command_ws, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
                get_params()


@service
def LedWindow_auto_mode(led_ip=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd_dm = "switch."+led_lamps_name[idx].lower()+"_dm"
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state_ps = state.get(cmd_ps)
            sensor_state_dm = state.get(cmd_dm)
            if sensor_state_ps == "on":
                if sensor_state_dm == "on":
                    command = json.dumps({'e': 'cmd', 'd': '$16 0'})
                else:
                    command = json.dumps({'e': 'cmd', 'd': '$16 1'})
                command_ws = 'echo \''+command+'\' | /config/websocat -n1 ws://'+led_lamp_ip+'/ws'
                subprocess.Popen(command_ws, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
                get_params()
