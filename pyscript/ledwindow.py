import json
import paho.mqtt.client as mqtt
from websocket import create_connection

# IP адрес ленты
led_lamps_ip = ["10.1.30.40"]
# Название ленты
led_lamps_name = ["LedWiFiWindow"]

mqtt_username = "mqtt_user" # Имя пользователя MQTT
mqtt_password =  "pass" # Пароль пользователя MQTT

# Дальше лучше ничего не менять
mqtt_host = "127.0.0.1"
mqtt_port = 1883

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
client.connect(mqtt_host, mqtt_port)

@service
def get_params():
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        ws = create_connection("ws://"+led_lamp_ip+"/ws")
        params = ["VR", "HN", "BR", "PS", "DM", "RM", "EF", "SM", "EN", "UP", "FM", "IP"]

        for param in params:
            command = json.dumps({'e': 'cmd', 'd': '$6 7|'+param})
            ws.send(command)
            result =  ws.recv()
            x = json.loads(result)
            y = json.loads(x["d"])
            client.publish(led_lamps_name[idx]+'/'+param, payload=str(y[param]), qos=0, retain=False)
    ws.close()


@service
def LedWindow_on_off(led_ip=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            ws = create_connection("ws://"+led_lamp_ip+"/ws")
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state = state.get(cmd_ps)
            if sensor_state == "on":
                command = json.dumps({'e': 'cmd', 'd': '$1 0'})
            else:
                command = json.dumps({'e': 'cmd', 'd': '$1 1'})
            ws.send(command)
            get_params()
            ws.close()        

@service
def LedWindow_brightness(led_ip=None, brightness=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd_br = "light."+led_lamps_name[idx].lower()+"_br"
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state = state.get(cmd_ps)
            if sensor_state == "on":
                ws = create_connection("ws://"+led_lamp_ip+"/ws")
                command = json.dumps({'e': 'cmd', 'd': '$4 0 '+str(brightness)})
                ws.send(command)
                get_params()
                ws.close()


@service
def LedWindow_random_effect(led_ip=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd_rm = "switch."+led_lamps_name[idx].lower()+"_rm"
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state_ps = state.get(cmd_ps)
            sensor_state_rm = state.get(cmd_rm)
            if sensor_state_ps == "on":
                ws = create_connection("ws://"+led_lamp_ip+"/ws")
                if sensor_state_rm == "on":
                    command = json.dumps({'e': 'cmd', 'd': '$16 5 0'})
                else:
                    command = json.dumps({'e': 'cmd', 'd': '$16 5 1'})
                ws.send(command)
                get_params()
                ws.close()


@service
def LedWindow_auto_mode(led_ip=None):
    for idx, led_lamp_ip in enumerate(led_lamps_ip):
        if led_ip==led_lamp_ip:
            cmd_dm = "switch."+led_lamps_name[idx].lower()+"_dm"
            cmd_ps = "switch."+led_lamps_name[idx].lower()+"_ps"
            sensor_state_ps = state.get(cmd_ps)
            sensor_state_dm = state.get(cmd_dm)
            if sensor_state_ps == "on":
                ws = create_connection("ws://"+led_lamp_ip+"/ws")
                if sensor_state_dm == "on":
                    command = json.dumps({'e': 'cmd', 'd': '$16 0'})
                else:
                    command = json.dumps({'e': 'cmd', 'd': '$16 1'})
                ws.send(command)
                get_params()
                ws.close()
