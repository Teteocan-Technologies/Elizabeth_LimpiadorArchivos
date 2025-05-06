# Limpiador de Archivos CSV/Excel

Este proyecto es un script en Python diseñado para limpiar archivos CSV o Excel. El script realiza las siguientes acciones sobre los datos:

1. Elimina las columnas vacías.
2. Elimina las filas vacías.
3. Elimina las filas duplicadas.
4. Rellena celdas vacías con un valor específico (en este caso, un string vacío).

## Requisitos

- Python 3.x
- Librerías:
  - pandas
  - openpyxl

Puedes instalar las librerías necesarias utilizando `pip`:

```bash
pip install pandas openpyxl

##Funcionamiento

1. Descarga el archivo LimpiadorArchivos.py o copia el código en un archivo .py en la misma carpeta en la que se encuentra tu archivo a limpiar. O bien, revisa el paso 2.1
2. Ejecuta el script desde la línea de comandos o terminal con:

    ```bash
    python LimpiadorArchivos.py

    2.1 Si tu archivo a limpiar no se encuentra en la misma carpeta que el código, deberás ingresar la dirección completa de tu archivo.
        Cuando el script te pide:
            Ruta del archivo (CSV o Excel):
        Debes escribir la ruta completa, por ejemplo:
            C:\\Users\\TuUsuario\\Documents\\datos.csv
            ## ASEGÚRATE DE AGREGAR // 


3. El script te pedirá la ruta del archivo CSV o Excel que deseas limpiar. 
    Por ejemplo:
    Ruta del archivo (CSV o Excel): datos_sucios.csv

4. El script limpiará los datos, mostrando en consola el estado antes y después de la limpieza.

5. Después de limpiar el archivo, te pedirá el nombre para guardar el archivo limpio y elegir el formato de salida (CSV o Excel):
    Nombre para guardar el archivo limpio (sin extensión): datos_limpios
    Selecciona el formato de salida:
    1. CSV (.csv)
    2. Excel (.xlsx)
    Elige 1 o 2: 

6. El archivo limpio se guardará en la misma ubicación del script, con el nombre que hayas proporcionado.


##EJEMPLO 
Ruta del archivo (CSV o Excel): datos_sucios.xlsx
Datos cargados correctamente.
       Nombre   Edad     Departamento
0      María     29.0     Ventas
1      Pedro     NaN      Marketing
2      Laura     33.0     NaN
3      María     29.0     Ventas
4      Juan      NaN      Finanzas

Filas antes de limpiar: 50
Filas después de limpiar: 47

Nombre para guardar el archivo limpio (sin extensión): datos_limpios
Selecciona el formato de salida:
1. CSV (.csv)
2. Excel (.xlsx)
Elige 1 o 2: 2

Archivo limpio guardado como: datos_limpios.xlsx

##NOTAS
En caso de usar windows o Linux, el paso 2.1 cambia un poco al ingresar la dirección del archivo. El formato sería el siguiente:
/home/tuusuario/Documentos/archivos/datos.csv
