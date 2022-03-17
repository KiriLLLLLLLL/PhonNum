import user_input, import_data, export

def console():
    type_action = user_input.type_get_data()
    if type_action == 1:
        import_data.import_data_controller(user_input.input_data())
    if type_action == 2:
        export.row_exp()
    if type_action == 3:
        export.rows_exp()

