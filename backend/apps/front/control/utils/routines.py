from asyncio import sleep
import threading
import time
from datetime import datetime
from apps.front.control.utils import variables as variables_value


class MasterHandler(threading.Thread):

    def __init__(self, **kwargs):
        super(MasterHandler, self).__init__(**kwargs)
        self.wait_time = 1

    def run(self):
        print("master start")
        variables_value.MasterState.master_running = True
    
    
        while variables_value.MasterState.run_vf2_timer == True or variables_value.MasterState.run_vf4_timer == True or variables_value.MasterState.run_st35_timer == True:
            time.sleep(self.wait_time)
            # print('hola')
            #vf4
            if variables_value.MasterState.run_vf4_timer == True:
                if variables_value.VF_4_TIMER_STATUS["pause"] == False:
                    # print("COMUN")
                    variables_value.VF_4_TIMER['segundos'] += 1
                    if (variables_value.VF_4_TIMER['segundos'] >= 60) :
                        variables_value.VF_4_TIMER['segundos'] = 0
                        variables_value.VF_4_TIMER['minutos'] += 1
                        if (variables_value.VF_4_TIMER['minutos'] >= 60) :
                            variables_value.VF_4_TIMER['minutos'] = 0
                            variables_value.VF_4_TIMER['horas'] += 1
                            if (variables_value.VF_4_TIMER['horas'] >= 24) :
                                variables_value.VF_4_TIMER['horas'] = 0
                else:
                    # print("ROJO")
                    variables_value.VF_4_TIMER['segundos_stoped'] += 1
                    if (variables_value.VF_4_TIMER['segundos_stoped'] >= 60) :  
                        variables_value.VF_4_TIMER['segundos_stoped'] = 0
                        variables_value.VF_4_TIMER['minutos_stoped'] += 1
                        if (variables_value.VF_4_TIMER['minutos_stoped'] >= 60) :
                            variables_value.VF_4_TIMER['minutos_stoped'] = 0
                            variables_value.VF_4_TIMER['horas_stoped'] += 1
                            if (variables_value.VF_4_TIMER['horas_stoped'] >= 24) :
                                variables_value.VF_4_TIMER['horas_stoped'] = 0
            #vf2
            if variables_value.MasterState.run_vf2_timer == True:
                if variables_value.VF_2_TIMER_STATUS["pause"] == False:
                    # print("COMUN")
                    variables_value.VF_2_TIMER['segundos'] += 1
                    if (variables_value.VF_2_TIMER['segundos'] >= 60) :
                        variables_value.VF_2_TIMER['segundos'] = 0
                        variables_value.VF_2_TIMER['minutos'] += 1
                        if (variables_value.VF_2_TIMER['minutos'] >= 60) :
                            variables_value.VF_2_TIMER['minutos'] = 0
                            variables_value.VF_2_TIMER['horas'] += 1
                            if (variables_value.VF_2_TIMER['horas'] >= 24) :
                                variables_value.VF_2_TIMER['horas'] = 0
                else:
                    # print("ROJO")
                    variables_value.VF_2_TIMER['segundos_stoped'] += 1
                    if (variables_value.VF_2_TIMER['segundos_stoped'] >= 60) :  
                        variables_value.VF_2_TIMER['segundos_stoped'] = 0
                        variables_value.VF_2_TIMER['minutos_stoped'] += 1
                        if (variables_value.VF_2_TIMER['minutos_stoped'] >= 60) :
                            variables_value.VF_2_TIMER['minutos_stoped'] = 0
                            variables_value.VF_2_TIMER['horas_stoped'] += 1
                            if (variables_value.VF_2_TIMER['horas_stoped'] >= 24) :
                                variables_value.VF_2_TIMER['horas_stoped'] = 0

            if variables_value.MasterState.run_st35_timer == True:
                if variables_value.ST35_TIMER_STATUS["pause"] == False:
                    # print("COMUN")
                    variables_value.ST35_TIMER['segundos'] += 1
                    if (variables_value.ST35_TIMER['segundos'] >= 60) :
                        variables_value.ST35_TIMER['segundos'] = 0
                        variables_value.ST35_TIMER['minutos'] += 1
                        if (variables_value.ST35_TIMER['minutos'] >= 60) :
                            variables_value.ST35_TIMER['minutos'] = 0
                            variables_value.ST35_TIMER['horas'] += 1
                            if (variables_value.ST35_TIMER['horas'] >= 24) :
                                variables_value.ST35_TIMER['horas'] = 0
                else:
                    # print("ROJO")
                    variables_value.ST35_TIMER['segundos_stoped'] += 1
                    if (variables_value.ST35_TIMER['segundos_stoped'] >= 60) :  
                        variables_value.ST35_TIMER['segundos_stoped'] = 0
                        variables_value.ST35_TIMER['minutos_stoped'] += 1
                        if (variables_value.ST35_TIMER['minutos_stoped'] >= 60) :
                            variables_value.ST35_TIMER['minutos_stoped'] = 0
                            variables_value.ST35_TIMER['horas_stoped'] += 1
                            if (variables_value.ST35_TIMER['horas_stoped'] >= 24) :
                                variables_value.ST35_TIMER['horas_stoped'] = 0
        variables_value.MasterState.master_running = False














        # while variables_value.MasterState.master_running == True:#and variables_value.MasterState.master_running == True
        #     time.sleep(self.wait_time)
        #     if variables_value.VF_4_TIMER_STATUS["pause"] == False:
        #         # print("COMUN")
        #         variables_value.VF_4_TIMER['segundos'] += 1
        #         if (variables_value.VF_4_TIMER['segundos'] >= 60) :
        #             variables_value.VF_4_TIMER['segundos'] = 0
        #             variables_value.VF_4_TIMER['minutos'] += 1
        #             if (variables_value.VF_4_TIMER['minutos'] >= 60) :
        #                 variables_value.VF_4_TIMER['minutos'] = 0
        #                 variables_value.VF_4_TIMER['horas'] += 1
        #                 if (variables_value.VF_4_TIMER['horas'] >= 24) :
        #                     variables_value.VF_4_TIMER['horas'] = 0
        #     else:
        #         # print("ROJO")
        #         variables_value.VF_4_TIMER['segundos_stoped'] += 1
        #         if (variables_value.VF_4_TIMER['segundos_stoped'] >= 60) :
        #             variables_value.VF_4_TIMER['segundos_stoped'] = 0
        #             variables_value.VF_4_TIMER['minutos_stoped'] += 1
        #             if (variables_value.VF_4_TIMER['minutos_stoped'] >= 60) :
        #                 variables_value.VF_4_TIMER['minutos_stoped'] = 0
        #                 variables_value.VF_4_TIMER['horas_stoped'] += 1
        #                 if (variables_value.VF_4_TIMER['horas_stoped'] >= 24) :
        #                     variables_value.VF_4_TIMER['horas_stoped'] = 0

        #     if variables_value.VF_4_TIMER_STATUS["pause"] == False:
        #         # print("COMUN")
        #         variables_value.VF_4_TIMER['segundos'] += 1
        #         if (variables_value.VF_4_TIMER['segundos'] >= 60) :
        #             variables_value.VF_4_TIMER['segundos'] = 0
        #             variables_value.VF_4_TIMER['minutos'] += 1
        #             if (variables_value.VF_4_TIMER['minutos'] >= 60) :
        #                 variables_value.VF_4_TIMER['minutos'] = 0
        #                 variables_value.VF_4_TIMER['horas'] += 1
        #                 if (variables_value.VF_4_TIMER['horas'] >= 24) :
        #                     variables_value.VF_4_TIMER['horas'] = 0
        #     else:
        #         # print("ROJO")
        #         variables_value.VF_4_TIMER['segundos_stoped'] += 1
        #         if (variables_value.VF_4_TIMER['segundos_stoped'] >= 60) :
        #             variables_value.VF_4_TIMER['segundos_stoped'] = 0
        #             variables_value.VF_4_TIMER['minutos_stoped'] += 1
        #             if (variables_value.VF_4_TIMER['minutos_stoped'] >= 60) :
        #                 variables_value.VF_4_TIMER['minutos_stoped'] = 0
        #                 variables_value.VF_4_TIMER['horas_stoped'] += 1
        #                 if (variables_value.VF_4_TIMER['horas_stoped'] >= 24) :
        #                     variables_value.VF_4_TIMER['horas_stoped'] = 0
    # variables_value.MasterState.master_running = False
    
        