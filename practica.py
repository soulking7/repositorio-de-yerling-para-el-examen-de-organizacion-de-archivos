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
    
    
# --- Petición de input ---
try:
    # Usamos input() dentro de un try/except para manejar posibles errores de valor
    input_id = str(input("\nIngrese el ID del objeto que desea buscar: "))
except Exception:
    print("Entrada inválida. Saliendo.")
    sys.exit()
print(f"\n--- Búsqueda del ID {input_id} ---")

try:
    registro_encontrado = False
    
    with open(file_path, 'r', encoding='utf-8') as file:

        for linea in file:
            # Quitar espacios en blanco de la línea
            linea_limpia = linea.strip()
            
            # Extraer el ID (todo lo que esté antes de la primera coma)
            try:
                id_linea = linea_limpia.split(',', 1)[0].strip()
            except IndexError:
                continue 
            
            # Comparar el ID extraído con el ID de entrada
            if id_linea == input_id:
                registro_encontrado = True
                
                # Formatear e imprimir la línea completa
                linea_sin_puntuacion = linea_limpia.replace(',', '    ')
                print("Registro Encontrado:")
                print(linea_sin_puntuacion)
                break # Detiene la búsqueda una vez que se encuentra el registro

    if not registro_encontrado:
        print(f"No existe ese elemento con ID '{input_id}' en los registros.")

except FileNotFoundError:
    print(f"Error: El archivo '{file_path}' no se encontró para la búsqueda.")
except Exception as e:
    print(f"Ocurrió un error inesperado durante la búsqueda: {e}")

