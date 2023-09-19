import os

MAX_RECORDS = 10


class Records:

    # __file__ hace referencia al archivo actual (records.py)
    filename = 'records.csv'
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(base_dir, 'data', filename)

    def __init__(self):
        pass

    def check_records_file(self):
        pass

    def insertar_record(self, nombre, puntuacion):
        pass

    def puntuacion_menor(self):
        pass

    def guardar(self):
        pass

    def cargar(self):
        pass

    def reset(self):
        pass
