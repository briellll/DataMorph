import io

import pandas as pd


def convert_csv_to_json(file: bytes) -> str | None:
    try:
        buffer = io.BytesIO(file)
        dataframe = pd.read_csv(buffer)
        return dataframe.to_json(orient='records', indent=4)

    except Exception as erro:
        print(f'Erro ao processar csv: {erro}')
        return None


def convert_json_to_csv(file: bytes) -> str | None:
    try:
        buffer = io.BytesIO(file)
        dataframe = pd.read_json(buffer)
        return dataframe.to_csv(index=False)
    except Exception as erro:
        print(f'Erro ao processar json: {erro}')
        return None
