from django.apps import AppConfig
import time
from opcua import Client, ua

import threading
from collections import deque
import asyncio
import smartsheet

from apps.front.control.utils import variables as variables_client
from apps.front.control.utils.routines import MasterHandler


class ControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.front.control'

    def ready(self) -> None:
        # Crea una instancia del cliente Smartsheet
        variables_client.CLIENT = smartsheet.Smartsheet(variables_client.ACCESS_TOKEN['token'])
        
