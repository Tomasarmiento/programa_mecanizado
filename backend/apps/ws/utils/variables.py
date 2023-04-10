from opcua import Client, ua
class frontState:
    #Leds
    led_on = False

    #Msges
    log_messages    = []
    err_messages    = []

class OPC_variables:
    HOST = '192.168.3.150:'
    PORT = '4840'
    URI = "opc.tcp://"
    REFRESH_REQUESTPLC_TIME = 0.02 # Time to refresh request to plc in seconds
    REFRESH_SENDFRONTDATA_TIME = 0.02 # Time to refresh states on frontend in seconds
    CLIENT = Client(URI+HOST+PORT)
    
    
# CLIENT = Client(OPC_variables.URI+OPC_variables.HOST+OPC_variables.PORT)
front_channel_name = ''
back_channel_name = ''

WEBSOCKET = True
WEBSOCKET_front = True

