from http import HTTPStatus

from fastapi import FastAPI, File, HTTPException, Response, UploadFile
from starlette.responses import StreamingResponse

from .core import convert_csv_to_json, convert_json_to_csv

app = FastAPI()


@app.post('/csv-para-json', tags=['conversor genérico'])
async def endpoint_csv_to_json(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):  # type:ignore
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Arquivo inválido. Por favor envie um arquivo .csv',
        )
    content = await file.read()

    converted = convert_csv_to_json(content)

    if converted is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Não foi possivel processar arquivo',
        )

    return Response(content=converted, media_type='application/json')


@app.post('/json-para-csv', tags=['conversor genérico'])
async def endpoint_json_to_csv(file: UploadFile = File(...)):
    if file.content_type != 'application/json':
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Arquivo invalido. Por favor envie um arquivo .json',
        )

    content = await file.read()

    converted = convert_json_to_csv(content)

    if converted is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Não foi possivel processar arquivo, verifique o formato',
        )

    nome_arquivo_saida = f'convertido_{file.filename.split(".")[0]}.csv'  # type: ignore
    return StreamingResponse(
        iter([converted]),
        media_type='text/csv',
        headers={
            'Content-Disposition': f'attachment;filename={nome_arquivo_saida}'
        },
    )
