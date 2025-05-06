import pandas as pd

# Función para limpiar el archivo
def clean_file(file_path):
    # Cargar el archivo
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            print("Formato de archivo no soportado.")
            return
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return
    
    print("Datos cargados correctamente.")
    print(df.head())

    # Eliminar columnas vacías
    df = df.dropna(axis=1, how='all')
    
    # Eliminar filas completamente vacías
    df = df.dropna(how='all')
    
    # Eliminar filas con valores vacíos (NaN o espacios en blanco) en alguna columna
    df = df.dropna(how='any')

    # Rellenar valores nulos o vacíos con un string vacío
    df = df.fillna('')

    print(f"\nFilas antes de limpiar: {len(df)}")
    
    # Mostrar el resultado de la limpieza
    print(df.head())
    
    return df

# Función para guardar el archivo limpio
def save_cleaned_file(df):
    # Pedir el nombre del archivo limpio
    output_filename = input("Nombre para guardar el archivo limpio (sin extensión): ")
    
    # Elegir el formato de salida
    print("Selecciona el formato de salida:")
    print("1. CSV (.csv)")
    print("2. Excel (.xlsx)")
    
    choice = input("Elige 1 o 2: ")
    
    if choice == '1':
        df.to_csv(f'{output_filename}.csv', index=False)
        print(f"Archivo limpio guardado como: {output_filename}.csv")
    elif choice == '2':
        df.to_excel(f'{output_filename}.xlsx', index=False)
        print(f"Archivo limpio guardado como: {output_filename}.xlsx")
    else:
        print("Opción no válida.")

# Función principal
def main():
    # Pedir al usuario la ruta del archivo a limpiar
    file_path = input("Ruta del archivo (CSV o Excel): ")

    # Limpiar el archivo
    cleaned_df = clean_file(file_path)
    
    if cleaned_df is not None:
        # Guardar el archivo limpio
        save_cleaned_file(cleaned_df)

# Ejecutar el script
if __name__ == "__main__":
    main()
