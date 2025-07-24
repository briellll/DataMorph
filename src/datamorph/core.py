import io

import pandas as pd


def convert_csv_to_json(file: bytes) -> str | None:
    try:
        buffer = io.BytesIO(file)
        dataframe = pd.read_csv(buffer, on_bad_lines='error', engine='python')
        # if abaixo implementado devivo pandas
        #  estar deixando passar célula vazia
        if dataframe.isnull().values.any():
            raise ValueError(
                '"CSV contém valores ausentes ou linhas mal formadas."'
            )
        return dataframe.to_json(orient='records', indent=4)

    except Exception as erro:
        print(f'Erro ao processar csv: {erro}')
        return None


def convert_json_to_csv(file: bytes) -> str | None:
    try:
        buffer = io.BytesIO(file)
        dataframe = pd.read_json(buffer)
        return dataframe.to_csv(index=False, lineterminator='\n')
    except Exception as erro:
        print(f'Erro ao processar json: {erro}')
        return None
