# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# Ciclo for que itere en files/input/test y train/negative, neutral y positive/*.txt (Ya está todo extraído)
# De cada txt necesito extraer la información de cada línea iterada y la guarde en "train_dataset.csv" y "test_dataset.csv". respectivamente
# La información dentro de estos será capturada por cada línea y se guardará en la columna phrase, tras
# cada línea tendrá un número de ínidice a la izquierda empezando de 0



def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    import pandas as pd
    import os

    # 2. Definir la estructura de salida
    # Creamos la carpeta output si no existe
    if not os.path.exists('files/output'):
        os.makedirs('files/output')

    # Diccionario para iterar facilmente
    datasets = ["train", "test"]
    sentiments = ["positive", "negative", "neutral"]

    # 3. Ciclo de ETL
    for dataset in datasets: # Iterar train y test
        data = [] # Lista para guardar diccionarios con la data

        for sentiment in sentiments: # Iterar positive, negative, neutral
            # Construir ruta: ej. input/train/positive
            path = os.path.join("files/input", dataset, sentiment)
            
            # Verificar que la ruta exista antes de listar archivos
            if os.path.exists(path):
                # Iterar sobre cada archivo .txt en esa carpeta
                for filename in os.listdir(path):
                    if filename.endswith(".txt"):
                        filepath = os.path.join(path, filename)
                        
                        # LEER EL ARCHIVO (Corrección principal a tu análisis)
                        with open(filepath, "r", encoding="utf-8") as f:
                            phrase = f.read() # Leemos todo el contenido, no por líneas
                        
                        # Agregar a la data
                        data.append({
                            "phrase": phrase,
                            "target": sentiment # El target es el nombre de la carpeta
                        })

        # 4. Crear DataFrame y Guardar
        df = pd.DataFrame(data)
        
        # Guardar en output/train_dataset.csv o test_dataset.csv
        # index=True es por defecto, pero lo pongo explícito porque lo mencionaste
        df.to_csv(f"files/output/{dataset}_dataset.csv", index=True)

    print("Archivos generados exitosamente en la carpeta output/")


pregunta_01()
