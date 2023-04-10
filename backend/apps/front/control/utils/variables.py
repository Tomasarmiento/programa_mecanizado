# -------------------------------------------------------------------------------------------- #
# ---------------------------------- NESTING SHEETS ---------------------------------------- #
# -------------------------------------------------------------------------------------------- #
SHEETS_NESTINGS = {
    'sheet_nesting_bancales_a' : 4240815590532996,
    'sheet_nesting_bancales_b' : 4516088634468228,
    'sheet_nesting_bancales_c' : 3227615625537412,
    'sheet_nesting_bancales_d' : 8490617010448260,
    'sheet_nesting_columnas_a' : 1603688490919812,
    'sheet_nesting_columnas_b' : 3707037054986116,
    'sheet_nesting_2mm': 6923393376249732,
    'sheet_single_pieces' : 3027194144644,
}

SHEETS_HASS = {
    'vf2' : 6805331167733636,
    'vf4' : 4083661931865988,
    'st35' : 3451545825109892,
}

# -------------------------------------------------------------------------------------------- #
# ---------------------------------- ACCESS TOKEN ---------------------------------------- #
# -------------------------------------------------------------------------------------------- #

ACCESS_TOKEN = {
    'token':'GrR9WJQrgU2YP7H3jsfEROBBOcmSJdqnA9rYa',
}


CLIENT = ''



# -------------------------------------------------------------------------------------------- #
# ---------------------------------- ACCESS TOKEN ---------------------------------------- #
# -------------------------------------------------------------------------------------------- #

SHEET_ID = {
    'id': ""
}

SHEET_ID_HASS = {
    'id': ""
}

# COLUMNA QUE BUSCA PARA SUMAR 1(QUE SE CORTÓ)
COLUMN_VALUE_TO_SEARCH = {
    'name_column_nesting' : 'Nesting cortado(chapa)',
    'name_column_single_piece' : 'Cantidad Cortado',
    'name_column_single_piece_hass' : 'Codigo',
}


VF_4_TIMER = {
    'horas' : 0,
    'minutos' : 0,
    'segundos' : 0,
    'horas_stoped' : 0,
    'minutos_stoped' : 0,
    'segundos_stoped' : 0,
}


VF_4_TIMER_STATUS = {
    'pause' : False,
}


ACTUAL_PIECE = {
    'vf2' : "AR-FRE-",
    'vf4' : "AR-FRE-",
    'st35' : "AR-TOR-",
}


PAUSE_STRINGS = {
    'vf2_pause_strings' : [],
    'vf4_pause_strings' : [],
    'st35_pause_strings' : [],
}

RESUME_MSG = {
    'vf2' : [],
    'vf4' : [],
    'st35' : [],
}


class MasterState:
    master_running = False