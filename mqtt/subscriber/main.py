"""
Micropython MQTT subscriber implementation
""" 

# Topic del que se va a pedir datos
topic_sub = b'apellido/magnitud/sensor'

# Funciones

def sub_callback(topic, msg):
    """
    Funcion de callback llamada cada vez que se
    encuentren mensajes por leer del broker.
    """
    # Topic de interes
    global topic_sub
    # Conversoin a string
    topic = topic.decode('utf-8')
    # Obtengo el mensaje del broker
    msg = msg.decode('utf-8')
    # Imprimo mensaje con topic
    print((topic, msg))
    print("-" * 60)
 
def connect_and_subscribe():
    """
    Funcion que se encarga de conectar el cliente
    al broker apropiado y luego hacer las suscripciones
    a los topics necesarios.

    return: objeto del tipo MQTTClient asociado al
    id del ESP32 y conectado al broker.
    """
    # Variables globales importadas desde el boot
    global client_id, mqtt_server, topic_sub
    # Creo una instancia del MQTT CLient
    client = MQTTClient(client_id, mqtt_server)
    # Configuro el callback para cuando llega un mensaje del broker
    client.set_callback(sub_callback)
    # Conecto al broker
    client.connect()
    # Subscripcion a topic
    client.subscribe(topic_sub)
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
        # Revisa si hay un nuevo mensaje
        new_message = client.check_msg()
    except OSError as e:
        # Reinicia si hay un error
        restart_and_reconnect()
