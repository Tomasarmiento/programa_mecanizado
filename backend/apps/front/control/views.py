import json
import http.client
import time


from django.http import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from apps.front.control.utils.functions import get_response_wos,ss_submit_single_piece,reset_variables_of_machine,send_ss_cmd
# from apps.front.control.utils.variables import SHEETS_NESTINGS,SHEET_ID
from apps.front.control.utils import variables as sheets_variables
from apps.front.control.utils.routines import MasterHandler

@csrf_exempt
def nesting_select(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    nesting = req_data[0][1]
    print(nesting)


    if nesting == "nesting_a":
        sheets_variables.SHEET_ID['id'] = (sheets_variables.SHEETS_NESTINGS['sheet_nesting_bancales_a'])
    elif nesting == "nesting_b":
        # print(sheets_variables.SHEET_ID[0]['id'])
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_bancales_b']
    elif nesting == "nesting_c":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_bancales_c']
    elif nesting == "nesting_d":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_bancales_d']
    elif nesting == "nesting_col_a":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_columnas_a']
    elif nesting == "nesting_col_b":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_columnas_b']
    elif nesting == "nesting_2mm":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_2mm']
    elif nesting == "nesting_3mm":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_3mm']
    elif nesting == "nesting_475mm":
        sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_nesting_475mm']

    print(sheets_variables.SHEET_ID['id'])
    # all_values_column()
    get_response_wos()


    return JsonResponse({})



@csrf_exempt
def piece_select(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    piece_code = req_data[0][1]
    cantidad = req_data[1][1]

    # piece_code = 'AR-CHA-010'
    # cantidad = 1
    print(piece_code,cantidad)

    sheets_variables.SHEET_ID['id'] = sheets_variables.SHEETS_NESTINGS['sheet_single_pieces']

    ss_submit_single_piece(piece_code,cantidad)



    return JsonResponse({})


@csrf_exempt
def timer_vf4(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    state_button = req_data[0][1]
    machine = req_data[1][1]
    print(state_button)

    if machine == "vf2":
        sheets_variables.MasterState.run_vf2_timer = True
        if state_button == "start":
            sheets_variables.VF_2_TIMER_STATUS['pause'] = False
        else:
            sheets_variables.VF_2_TIMER_STATUS['pause'] = True

    elif machine == "vf4":
        sheets_variables.MasterState.run_vf4_timer = True
        if state_button == "start":
            sheets_variables.VF_4_TIMER_STATUS['pause'] = False
        else:
            sheets_variables.VF_4_TIMER_STATUS['pause'] = True

    elif machine == "st35":
        sheets_variables.MasterState.run_st35_timer = True
        if state_button == "start":
            sheets_variables.ST35_TIMER_STATUS['pause'] = False
        else:
            sheets_variables.ST35_TIMER_STATUS['pause'] = True

    if sheets_variables.MasterState.master_running != True:
        MasterHandler().start()


    return JsonResponse({})



@method_decorator(csrf_exempt, name='dispatch')
class StartRoutine(View):
    def post(self, request):
        if sheets_variables.MasterState.master_running == True:
            print('Master ya está ejecutándose')
        else:
            MasterHandler().start()
        
        return JsonResponse({})
    
@csrf_exempt
def finish_cicle(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    machine = req_data[0][1]
    if machine == "vf4":
        sheets_variables.MasterState.run_vf4_timer = False
    elif machine == "vf2":
        sheets_variables.MasterState.run_vf2_timer = False
        # sheets_variables.MasterState.master_running = False
    elif machine == "st35":
        sheets_variables.MasterState.run_st35_timer = False

    return JsonResponse({})

@csrf_exempt
def finish_start_vf4(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    state_button = req_data[0][1]
    machine = req_data[1][1]
    print(state_button)
    if machine == "vf4":
        if state_button == "reset":
            for k in sheets_variables.VF_4_TIMER: sheets_variables.VF_4_TIMER[k] = 0
            # reset_variables_of_machine("vf4")
        if state_button == "reset_all":
            reset_variables_of_machine("vf4")

        sheets_variables.MasterState.run_vf4_timer = False
    elif machine == "vf2":
        if state_button == "reset":
            for k in sheets_variables.VF_2_TIMER: sheets_variables.VF_2_TIMER[k] = 0
            # reset_variables_of_machine("vf4")
        if state_button == "reset_all":
            reset_variables_of_machine("vf2")

        sheets_variables.MasterState.run_vf2_timer = False
        # sheets_variables.MasterState.master_running = False
    elif machine == "st35":
        if state_button == "reset":
            for k in sheets_variables.ST35_TIMER: sheets_variables.ST35_TIMER[k] = 0
            # reset_variables_of_machine("vf4")
        if state_button == "reset_all":
            reset_variables_of_machine("st35")

        sheets_variables.MasterState.run_st35_timer = False

    return JsonResponse({})
    

@csrf_exempt
def selected_piece(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    piece = req_data[0][1]
    machine = req_data[1][1]
    print(piece)

    if machine == "vf4":
        sheets_variables.ACTUAL_PIECE["vf4"] = "AR-FRE-"
        sheets_variables.ACTUAL_PIECE["vf4"] = sheets_variables.ACTUAL_PIECE["vf4"] + piece
    elif machine == "vf2":
        sheets_variables.ACTUAL_PIECE["vf2"] = "AR-FRE-"
        sheets_variables.ACTUAL_PIECE["vf2"] = sheets_variables.ACTUAL_PIECE["vf2"] + piece
    elif machine == "st35":
        sheets_variables.ACTUAL_PIECE["st35"] = "AR-TOR-"
        sheets_variables.ACTUAL_PIECE["st35"] = sheets_variables.ACTUAL_PIECE["st35"] + piece
    
    return JsonResponse({})


@csrf_exempt
def msg_pause(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    pause_msg = req_data[0][1]
    machine = req_data[1][1]
    print(machine,pause_msg)

    if machine == "vf4" and pause_msg != "":
        sheets_variables.PAUSE_STRINGS['vf4_pause_strings'].append(pause_msg)
        # print(sheets_variables.PAUSE_STRINGS['vf4_pause_strings'])
    if machine == "vf2" and pause_msg != "":
        sheets_variables.PAUSE_STRINGS['vf2_pause_strings'].append(pause_msg)
        # print(sheets_variables.PAUSE_STRINGS['vf4_pause_strings'])
    if machine == "st35" and pause_msg != "":
        sheets_variables.PAUSE_STRINGS['st35_pause_strings'].append(pause_msg)
        # print(sheets_variables.PAUSE_STRINGS['vf4_pause_strings'])

    print("pause msggggg",pause_msg)


    # sheets_variables.RESUME_MSG['vf4_pause_strings'].append(ss_pause_msg)


    return JsonResponse({})

@csrf_exempt
#boton terminar
def msg_ss(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    ss_msg = req_data[0][1]
    ss_machine = req_data[1][1]
    # print(ss_msg,ss_machine)
    # print(type(ss_msg))
    ss_msg_list = []
    ss_msg = ss_msg.split(",")
    print(ss_msg)

    ss_msg.pop()
    ss_msg.pop(0)
    new_arr = []

    for n in range (0, len(ss_msg)):
        print(ss_msg[n])
        if n == 0 or n == 1 or n == 6 or n == 7:
            new_arr.append(ss_msg[n].split(":",1)[1])
        elif n == 2:
            new_arr.append(ss_msg[n].split(":",1)[1]+ss_msg[n+1])
        elif n == 4:
            new_arr.append(ss_msg[n].split(":",1)[1]+ss_msg[n+1])
    new_arr.reverse()
            
    print(new_arr)
        


    if ss_machine == "vf4" and ss_msg != "":
        sheets_variables.RESUME_MSG['vf4'] = new_arr
        # print(sheets_variables.RESUME_MSG['vf4'])
    if ss_machine == "vf2" and ss_msg != "":
        sheets_variables.RESUME_MSG['vf2'] = new_arr
        # print(sheets_variables.RESUME_MSG['vf4'])
    if ss_machine == "vf2" and ss_msg != "":
        sheets_variables.RESUME_MSG['st35'] = new_arr
        # print(sheets_variables.RESUME_MSG['vf4'])


    # sheets_variables.RESUME_MSG['vf4_pause_strings'].append(ss_pause_msg)


    return JsonResponse({})


@csrf_exempt
#boton enviar SS
def send_ss(request):
    
    post_req = request.POST
    print(post_req)

    req_data = []
        
    for item in post_req.items():   # Item is in (key, value) format
        req_data.append(item)


    ss_send_machine = req_data[0][1]
    print(ss_send_machine)

    if ss_send_machine == "vf4":
        sheets_variables.SHEET_ID_HASS['id'] = sheets_variables.SHEETS_HASS['vf4']
        send_ss_cmd("vf4")
    if ss_send_machine == "vf2":
        sheets_variables.SHEET_ID_HASS['id'] = sheets_variables.SHEETS_HASS['vf2']
        send_ss_cmd("vf2")
    if ss_send_machine == "st35":
        sheets_variables.SHEET_ID_HASS['id'] = sheets_variables.SHEETS_HASS['st35']
        send_ss_cmd("vf2")


    return JsonResponse({})