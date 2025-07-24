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
        files={'file': ('content_fake.txt', fake_buffer, 'text/plain')},
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


def test_json_to_csv_ok():
    json_content_string = (
        '[{"nome":"gabriel","cidade":"santarem"},'
        '{"nome":"tico","cidade":"santarem"}]'
    )

    json_content_byte = json_content_string.encode('utf-8')
    json_buffer = io.BytesIO(json_content_byte)

    response = client.post(
        '/json-para-csv',
        files={'file': ('pessoas.json', json_buffer, 'application/json')},
    )

    assert response.status_code == HTTPStatus.OK
    assert 'text/csv' in response.headers['content-type']
    assert 'attachment' in response.headers['content-disposition']
    assert 'convertido_pessoas.csv' in response.headers['content-disposition']

    expected_csv_content = 'nome,cidade\ngabriel,santarem\ntico,santarem\n'

    assert response.text == expected_csv_content


def test_json_to_csv_type_invalidate():
    fake_file_buffer = io.BytesIO(b'texto qualquer')

    response = client.post(
        '/json-para-csv',
        files={'file': ('text.txt', fake_file_buffer, 'text/plain')},
    )

    msg_error = 'Arquivo invalido. Por favor envie um arquivo .json'
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert msg_error in response.json()['detail']


def test_json_to_csv_invalidate():
    fake_json_broken = b'[{"lenda": "Boto"} {"lenda": "Iara"}]'

    fake_csv_broken = io.BytesIO(fake_json_broken)

    response = client.post(
        '/json-para-csv',
        files={'file': ('fake.json', fake_csv_broken, 'application/json')},
    )

    msg_error = 'Não foi possivel processar arquivo'
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert msg_error in response.json()['detail']
