import smartsheet
import json,requests
import time

from apps.front.control.utils.variables import ACCESS_TOKEN,SHEET_ID,COLUMN_VALUE_TO_SEARCH,CLIENT,VF_4_TIMER,RESUME_MSG,PAUSE_STRINGS,SHEET_ID_HASS
# from apps.front.control.apps import CLIENTE

def get_response_wos():
    inicio = time.time()

    # Define el token de acceso y la ID de la hoja
    # access_token = 'GrR9WJQrgU2YP7H3jsfEROBBOcmSJdqnA9rYa'

    access_token = ACCESS_TOKEN["token"]
    sheet_id = SHEET_ID['id']
    # column_value_to_search = 'Nesting cortado(chapa)'
    column_value_to_search = COLUMN_VALUE_TO_SEARCH['name_column_nesting']
    cliente = CLIENT

    # # Crea una instancia del cliente Smartsheet
    # cliente = smartsheet.Smartsheet(access_token)
    


    # print(type(cliente))

    url = f"https://api.smartsheet.com/2.0/sheets/{sheet_id}" #CORE ID
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "ddc06181-e8d1-4826-bc95-dbfe966c2c70"
        }
    response = requests.request("GET", url, headers=headers)
    sheetParts = json.loads(response.text)

    # print(sheetParts['columns'])

    filas = sheetParts['rows']

    # print(filas[5]["cells"][1]["columnId"])
    # print(filas)


    # client.Sheets.update_rows("asd", [1])

    def update_cell_value(row_number,col_name,value):
        row_id = row_number
        col_id = col_name
        newCell = cliente.models.Cell()
        newCell.column_id = col_id
        newCell.value = value
        newRow = cliente.models.Row()
        newRow.id = row_id
        newRow.cells.append(newCell)
        cliente.Sheets.update_rows(sheet_id, newRow)
        return None

    # update_cell_value(7570786798266244,1806031757567876,'jaja')

    # for key, value in sheetParts.items() :
    #     print (key)


    # print(get_id_of_column_name('test'))


    # Saca el id de la comuna test
    def get_id_of_column_name(column_name):
        for n in sheetParts['columns']:
            if n['title'] == column_name:
                return(n['id'])
            
    #Obtiene todos los valores de una columna especificada en la variable "column_value_to_search"
    for n in range(0,len(filas)):
        for w in range(0,len(filas[n]["cells"])):
            if filas[n]["cells"][w]['columnId'] == get_id_of_column_name(column_value_to_search):
                update_cell_value(filas[n]['id'],filas[n]["cells"][w]['columnId'],filas[n]["cells"][w]['value']+1)
    
    fin = time.time()
    print("tiempo q tardaaa",fin-inicio)





def ss_submit_single_piece(piece_value,cantidad):
    piece_value = "AR-CHA-"+str(piece_value)
    print(piece_value,cantidad)
    inicio = time.time()

    # Define el token de acceso y la ID de la hoja
    # access_token = 'GrR9WJQrgU2YP7H3jsfEROBBOcmSJdqnA9rYa'

    access_token = ACCESS_TOKEN["token"]
    sheet_id = SHEET_ID['id']
    # column_value_to_search = 'Nesting cortado(chapa)'
    column_value_to_search = COLUMN_VALUE_TO_SEARCH['name_column_single_piece']
    cliente = CLIENT

    # # Crea una instancia del cliente Smartsheet
    # cliente = smartsheet.Smartsheet(access_token)
    


    # print(type(cliente))

    url = f"https://api.smartsheet.com/2.0/sheets/{sheet_id}" #CORE ID
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "ddc06181-e8d1-4826-bc95-dbfe966c2c70"
        }
    response = requests.request("GET", url, headers=headers)
    sheetParts = json.loads(response.text)

    # print(sheetParts['columns'])

    filas = sheetParts['rows']

    # print(filas[5]["cells"][1]["columnId"])
    # print(filas)


    # client.Sheets.update_rows("asd", [1])

    def update_cell_value(row_number,col_name,value):
        row_id = row_number
        col_id = col_name
        newCell = cliente.models.Cell()
        newCell.column_id = col_id
        newCell.value = value
        newRow = cliente.models.Row()
        newRow.id = row_id
        newRow.cells.append(newCell)
        cliente.Sheets.update_rows(sheet_id, newRow)
        return None

    # update_cell_value(7570786798266244,1806031757567876,'jaja')

    # for key, value in sheetParts.items() :
    #     print (key)


    # print(get_id_of_column_name('test'))


    # Saca el id de la comuna column_value_to_search
    def get_id_of_column_name(column_name):
        for n in sheetParts['columns']:
            if n['title'] == column_name:
                return(n['id'])
            
    #Obtiene todos los valores de una columna especificada en la variable "column_value_to_search"
    for n in range(0,len(filas)):
        for w in range(0,len(filas[n]["cells"])):
            # print(filas[n]["cells"][0])
            if filas[n]["cells"][w]['columnId'] == get_id_of_column_name(column_value_to_search) and filas[n]["cells"][0]['value'] == piece_value:
                # print(type(filas[n]["cells"][2]['value']),type(cantidad))
                # print("FILA: ",filas[n]['id'],"COLUMNA: ",filas[n]["cells"][w]['columnId'],"VALOR: ",filas[n]["cells"][2]['value'])
                update_cell_value(filas[n]['id'],filas[n]["cells"][w]['columnId'],filas[n]["cells"][2]['value']+float(cantidad))
    
    fin = time.time()
    print("tiempo q tardaaa",fin-inicio)







def reset_variables_of_machine(model_machine):
    if model_machine == "vf4":
        RESUME_MSG["vf4"] = ""
        PAUSE_STRINGS["vf4_pause_strings"] = []
        for k in VF_4_TIMER: VF_4_TIMER[k] = 0

def create_ss_msg(resume_msg,dict_pause_msg):
    msg_pause_to_append = ""
    for n in dict_pause_msg:
        msg_pause_to_append += f'{n},'
    resume_msg.append(msg_pause_to_append)
    return resume_msg
    print("resume msg",resume_msg)
    print("pause msg",dict_pause_msg)


def send_ss_cmd(model_machine):
    resume_msg = ""
    pause_msg = ""
    access_token = ACCESS_TOKEN["token"]
    sheet_id = SHEET_ID_HASS['id']
    # column_value_to_search = 'Nesting cortado(chapa)'
    column_value_to_search = COLUMN_VALUE_TO_SEARCH['name_column_single_piece_hass']
    cliente = CLIENT

    if model_machine == "vf4":
        resume_msg = RESUME_MSG["vf4"]
        pause_msg = PAUSE_STRINGS["vf4_pause_strings"]
        resume_msg = create_ss_msg(resume_msg,pause_msg)
    
    print("pause msgaaa",pause_msg)

    
    url = f"https://api.smartsheet.com/2.0/sheets/{sheet_id}" #CORE ID
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "ddc06181-e8d1-4826-bc95-dbfe966c2c70"
        }
    response = requests.request("GET", url, headers=headers)
    sheetParts = json.loads(response.text)

    # print(sheetParts['columns'])

    filas = sheetParts['rows']
    # for n in filas:
    #     print(filas[n])
    # print(filas['id'])

    def update_cell_value(row_number,col_name,value):
        row_id = row_number
        col_id = col_name
        newCell = cliente.models.Cell()
        newCell.column_id = col_id
        newCell.value = value
        newRow = cliente.models.Row()
        newRow.id = row_id
        newRow.cells.append(newCell)
        cliente.Sheets.update_rows(sheet_id, newRow)
        return None

    def test():
        for n in filas:
            for w in range(0,len(n['cells'])):
                print(n['cells'][w])
                if not "value" in n['cells'][w]:
                    print("no esta valor")
                    update_cell_value(n['id'],n['cells'][w]['columnId'],resume_msg[w])
                    print("EL LEN ES", len(resume_msg))
                    if w == len(resume_msg)-1:
                        return

                # update_cell_value(6331128909129604,n['cells'][w]['columnId'],lista_mensajes[w])
                # if w == 5:
                #     return
    test()

    print(resume_msg)
    reset_variables_of_machine("vf4")


    # print(resume_msg, pause_msg)




























# def get_response_wos():
#     # Define el token de acceso y la ID de la hoja
#     sheet_id = SHEET_ID['id']
#     access_token = ACCESS_TOKEN["token"]

#     # Crea una instancia del cliente Smartsheet
#     # client = smartsheet.Smartsheet(ACCESS_TOKEN)


#     url = f"https://api.smartsheet.com/2.0/sheets/{sheet_id}" #CORE ID
#     print("acessssssssssssssssssssss", type(access_token))
#     headers = {
#         'Authorization': f"Bearer {access_token}",
#         'Content-Type': "application/json",
#         'Cache-Control': "no-cache",
#         'Postman-Token': "ddc06181-e8d1-4826-bc95-dbfe966c2c70"
#         }
#     response = requests.request("GET", url, headers=headers)
#     sheetParts = json.loads(response.text)
#     # print(sheetParts)
#     filas = sheetParts['rows']

#     def update_cell_value(row_number,col_name,value):
#         row_id = row_number
#         col_id = col_name
#         newCell = CLIENT.models.Cell()
#         newCell.column_id = col_id
#         newCell.value = value
#         newRow = CLIENT.models.Row()
#         newRow.id = row_id
#         newRow.cells.append(newCell)
#         CLIENT.Sheets.update_rows(sheet_id, newRow)
#         return None

#     # update_cell_value(7570786798266244,1806031757567876,'jaja')


#     # Saca el id de la comuna test
#     def get_id_of_column_name(column_name):
#         # sheetParts,filas = get_response_wos()
#         for n in sheetParts['columns']:
#             if n['title'] == column_name:
#                 return(n['id'])
    
#     #Obtiene todos los valores de una columna especificada en la variable "column_value_to_search"
#     for n in range(0,len(filas)):
#             for w in range(0,len(filas[n]["cells"])):
#                 if filas[n]["cells"][w]['columnId'] == get_id_of_column_name(COLUMN_VALUE_TO_SEARCH):
#                     update_cell_value(filas[n]['id'],filas[n]["cells"][w]['columnId'],filas[n]["cells"][w]['value']+1)
            
#     #Obtiene todos los valores de una columna especificada en la variable "column_value_to_search"
#     # def all_values_column():
#     #     # sheetParts,filas = get_response_wos()
#     #     for n in range(0,len(filas)):
#     #         for w in range(0,len(filas[n]["cells"])):
#     #             if filas[n]["cells"][w]['columnId'] == get_id_of_column_name(COLUMN_VALUE_TO_SEARCH):
#     #                 update_cell_value(filas[n]['id'],filas[n]["cells"][w]['columnId'],filas[n]["cells"][w]['value']+1)