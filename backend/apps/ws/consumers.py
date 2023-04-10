import json
from random import randint
from time import sleep
import time
# import websockets
import asyncio
import threading
import sys, signal
from channels.db import database_sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer


from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer


from apps.ws.models import ChannelInfo
from apps.ws.utils import variables as ws_vars
from apps.ws.utils.variables import OPC_variables
from apps.front.control.utils import variables as machine_variables



class FrontConsumer(AsyncWebsocketConsumer):
    print("dentro de front consumer")
    async def connect(self):
        # await self.set_channel_info()
        await self.accept()
        # ws_vars.front_channel_name = self.channel_name
        print("FRONT WS CONNECTED")


    async def receive(self, text_data=None, bytes_data=None):
        print("receive")
        error_code = 4011
        await asyncio.sleep(0.5)
        while ws_vars.WEBSOCKET_front == True:
            # print("while front")
            # if ws_vars.WEBSOCKET_front == True:
            try:
                await self.front_message({
                    "type": "websocket.send",
                    "data": {
                        'timer_vf4': machine_variables.VF_4_TIMER,
                        'vf2_piece': machine_variables.ACTUAL_PIECE["vf2"],
                        'vf4_piece': machine_variables.ACTUAL_PIECE["vf4"],
                        'st35_piece': machine_variables.ACTUAL_PIECE["st35"],
                    },
                })
                await asyncio.sleep(OPC_variables.REFRESH_SENDFRONTDATA_TIME)
                await asyncio.sleep(0.5)
            except:
                await self.disconnected({'code': error_code})
                await self.close(error_code)
                raise


        print("la text data",text_data)
    
    async def disconnected(self, close_code):
        print("Front ws disconnected, code", close_code)
        # await self.delete_channel_info()
        await self.close()
        raise StopConsumer()
    
    async def front_message(self, event):
        # print("el evento es", event)
        await self.send(text_data=json.dumps(event['data']))
    
    # @database_sync_to_async
    # def set_channel_info(self):
    #     ChannelInfo.objects.create(
    #         source = 'front',
    #         name = self.channel_name,
    #         log = 0
    #     )
    
    # @database_sync_to_async
    # def delete_channel_info(self):
    #     channel_info = ChannelInfo.objects.get(name=self.channel_name)
    #     channel_info.delete()


