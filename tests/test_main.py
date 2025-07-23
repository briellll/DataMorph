import io
from http import HTTPStatus

from fastapi.testclient import TestClient

from datamorph.main import app

client = TestClient(app)


def test_csv_to_json_ok():
    csv_content_string = 'nome,idade\nGabriel,30\nAna,25'

    csv_content_byte = csv_content_string.encode('utf-8')

    buffer = io.BytesIO(csv_content_byte)

    response = client.post(
        '/csv-para-json', files={'file': ('dados.csv', buffer, 'text/csv')}
    )

    assert response.status_code == HTTPStatus.OK
    expected_json = [
        {'nome': 'Gabriel', 'idade': 30},
        {'nome': 'Ana', 'idade': 25},
    ]
    assert response.json() == expected_json


def test_csv_to_json_extension_invalidates():
    fake_file_content = 'fake file'

    fake_file_content_bytes = fake_file_content.encode('utf-8')

    fake_buffer = io.BytesIO(fake_file_content_bytes)

    response = client.post(
        '/csv-para-json',
        files={'file': ('content_fake.txt', fake_buffer, 'tex/plain')},
    )

    error_detail = 'Arquivo inválido. Por favor envie um arquivo .csv'
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert error_detail in response.json()['detail']


def test_csv_to_json_content_invalidate():
    content_invalidate = 'col1,col2\nvalor1,valor2\nvalor3'

    content_invalidate_byte = content_invalidate.encode('utf-8')

    buffer_invalidate = io.BytesIO(content_invalidate_byte)

    response = client.post(
        '/csv-para-json',
        files={'file': ('quebrado.csv', buffer_invalidate, 'text/csv')},
    )

    error_detail = 'Não foi possivel processar arquivo'
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert error_detail in response.json()['detail']
