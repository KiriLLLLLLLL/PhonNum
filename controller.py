import user_input, import_data, export

def import_data_controller(data):
    import_data.row_imp(data)
    import_data.rows_imp(data)

import_data_controller(user_input.input_data())

# def export_data_controller(data):
#     if