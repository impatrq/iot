"""
Micropython MQTT publisher implementation
""" 
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

# Nombre de la red a conectarse
ssid = 'SSID'
# Password de la red
password = 'PASS'
# IP del broker al que se va a conectar
mqtt_server = 'BROKER_IP'
# ID del cliente
client_id = ubinascii.hexlify(machine.unique_id())

# Configuracion de la red  
station = network.WLAN(network.STA_IF)
# Conexion
station.active(True)
station.connect(ssid, password)
# Espera a que el dispositivo se conecte a la red
while station.isconnected() == False:
    pass

# Mensajes de ayuda por consola
print('Connection successful')
print(station.ifconfig())
print('-' * 60)