import os
import sys
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_dir, 'planta.csv')

     
try:
    with open(file_path, 'r') as file:
        content = file.readlines()
        for linea in content:
             linea_sin_puntuacion = linea.replace(',', '  ')
             print(linea_sin_puntuacion.strip(" "))
except FileNotFoundError:
    print(f"Error: El archivo no se encontró en la ruta: {file_path}")
    


    
