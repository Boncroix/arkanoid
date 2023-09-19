import csv
import os

MAX_RECORDS = 10


class Records:

    # __file__ hace referencia al archivo actual (records.py)
    filename = 'records.csv'
    file_dir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        self.game_records = []
        self.data_path = os.path.join(
            os.path.dirname(self.file_dir),
            'data'
        )
        self.file_path = os.path.join(
            self.data_path, self.filename
        )
        self.check_records_file()
        self.cargar()

    def check_records_file(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
            print('No había directorio para datos, pero lo he creado!!!')
        if not os.path.exists(self.file_path):
            self.reset()

    def insertar_record(self, nombre, puntuacion):
        """
        1. recorrer todo el archivo y ver donde insertarlo
        2. escribir el archivo
        """
        self.game_records.append([nombre, puntuacion])
        self.game_records.sort(key=lambda item: item[1], reverse=True)
        self.game_records = self.game_records[:MAX_RECORDS]
        self.guardar()

    def puntuacion_menor(self):
        return self.game_records[-1][1]

    def guardar(self):
        # lector = open(self.file_path, mode='w')
        # lector.close()
        with open(self.file_path, mode='w') as records_file:
            writer = csv.writer(records_file)
            writer.writerow(('Nombre', 'Puntos'))
            writer.writerows(self.game_records)

    def cargar(self):
        with open(self.file_path, mode='r') as records_file:
            reader = csv.reader(records_file)
            contador = 0
            self.game_records = []
            for linea in reader:
                contador += 1
                if contador == 1:
                    continue
                self.game_records.append([linea[0], int(linea[1])])

    def reset(self):
        """
        Crea el archivo de records VACÍO
        """
        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(['-----', 0])
        self.guardar()
