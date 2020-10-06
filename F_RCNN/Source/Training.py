import os
import time

import psutil

# Definicion de rutas de localización del proyecto y del conjunto de datos
PATH_PROJECT = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir))
PATH_DATASET = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir, 'Dataset'))

start_time = time.time() - psutil.boot_time()
Left = 12 * 3600 - start_time

os.environ[
    'PYTHONPATH'] += ':/content/gdrive/My Drive/Desktop/models/research/:/content/gdrive/My Drive/Desktop/models/research/slim'
