"""
Micropython MQTT publisher implementation
""" 
import esp32

# Topic al que se va a publicar datos
topic_pub = b'apellido/magnitud/sensor'
# Cantidad de segundos entre mensajes
message_interval = 1

# Funciones

def connect():
    """
    Funcion que se encarga de conectar el cliente
    al broker apropiado.

    return: objeto del tipo MQTTClient asociado al
    id del ESP32 y conectado al broker.
    """
    # Variables globales importadas desde el boot
    global client_id, mqtt_server
    # Creo una instancia del MQTT CLient
    client = MQTTClient(client_id, mqtt_server)
    # Conecto al broker
    client.connect()
    # Mensajes de consola
    print('Connected to {} MQTT broker'.format(mqtt_server))
    print("-" * 60)
    print()
    # Devuelvo el client
    return client
 
def restart_and_reconnect():
    """
    Funcion que se encarga de resetear el ESP32
    si hubiese algun error al conectarse.
    """
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
 
# Programa principal

try:
    # Intenta conectar el cliente
    client = connect()
except OSError as e:
    # Reinicia si hay un error
    restart_and_reconnect()

# Bucle principal
while True:
    try:
        # Obtiene datos para publicar
        msg = b""
        # Publica mensaje con el topic solicitado
        client.publish(topic_pub, msg)
        # Ayuda visual por consola
        print("Msg published: '{}'".format(msg.decode('utf-8')))
        # Delay para mandar el proximo mensaje
        time.sleep(message_interval)

    except OSError as e:
        # Reiniciar si falla
        restart_and_reconnect()