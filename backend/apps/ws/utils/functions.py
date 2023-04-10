from time import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from apps.ws.utils import variables as ws_vars
import time


def init_channel_info(ch_model):
    chs = ch_model.objects.filter(source='front')
    for ch in chs:
        ch.delete()
    
def get_ch_info(ch_model, source):
    try:
        return ch_model.objects.filter(source=source).get(log=0)
    
    except ch_model.DoesNotExist:
        return False
    

def send_front_message(data):
    # print(data)
    # print("se mando data al front")
    ch_name = ws_vars.front_channel_name
    if ch_name:
        # print("entro al if de channel name")
        ch_layer = get_channel_layer()
        # print("channel layer", ch_layer)
        payload = {
            'type': 'front.message',
            'data': data
        }
        async_to_sync(ch_layer.send)(
            ch_name,
            payload
        )
    
    else:
        # print("Front not connected")
        pass


def get_front_states():
    data = {
        '2' : 2,
        '1' : 1
    }
    return data
