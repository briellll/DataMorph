🐲 DataMorph API
Seu tradutor de arquivos juramentado, direto da Amazônia para o mundo!

🎯 Sobre o Projeto
DataMorph é uma API parruda e veloz construída com FastAPI para a conversão bidirecional de arquivos entre os formatos CSV e JSON. Cansado de abrir planilhas e salvar como, ou de procurar conversores online duvidosos? Seus problemas acabaram!

Este projeto utiliza o poder do Pandas por baixo dos panos para garantir uma conversão de dados robusta e eficiente, lidando até mesmo com arquivos mal formados de forma inteligente.

✨ Funcionalidades
✅ Conversão de arquivos CSV para JSON.

✅ Conversão de arquivos JSON para CSV.

✅ Validação de formato de arquivo na entrada (só aceita o que promete!).

✅ Validação de conteúdo mal formado, rejeitando arquivos "quebrados".

✅ Documentação interativa e automática com Swagger UI (/docs).

✅ Respostas de erro claras e padronizadas.

🛠️ Tecnologias Utilizadas
Esta API foi construída com as melhores ferramentas do ecossistema Python:

🐍 Python 3.13

✨ FastAPI: Para a construção da API assíncrona.

🐼 Pandas: O motor por trás da manipulação e conversão dos dados.

🚀 Uvicorn: O servidor ASGI que coloca nossa API no ar.

📦 Poetry: Para gerenciamento de dependências e do ambiente virtual.

🧪 Pytest: Para garantir que tudo funcione como esperado através de testes automatizados.

🚀 Como Rodar o Projeto
Para ter o DataMorph rodando na sua máquina local, siga estes simples passos.

Pré-requisitos
Ter o Python 3.13+ instalado.

Ter o Poetry instalado.

Instalação
Clone o repositório:

Bash

git clone https://github.com/briellll/datamorph.git
Navegue até a pasta do projeto:

Bash

cd datamorph
Instale as dependências com o Poetry:
(O Poetry criará um ambiente virtual automaticamente)

Bash

poetry install
Inicie o servidor da API:

Bash

poetry run uvicorn datamorph.main:app --reload
O --reload faz com que o servidor reinicie automaticamente a cada alteração no código. Mão na roda!

Pronto! Sua API já está no ar. Abra seu navegador e acesse:

Documentação Interativa (Swagger): http://127.0.0.1:8000/docs

Documentação Alternativa (ReDoc): http://127.0.0.1:8000/redoc

🕹️ Como Usar a API
A maneira mais fácil de testar é usando a documentação interativa (/docs), onde você pode fazer o upload dos arquivos diretamente pelo navegador.

Para os mais "hackers", aqui estão exemplos usando curl no terminal.

Convertendo CSV para JSON
Bash

# O '-F' indica um campo de formulário multipart.
# "file=@caminho/para/seu/arquivo.csv" anexa o seu arquivo.
curl -X POST -F "file=@caminho/para/seu/arquivo.csv" http://127.0.0.1:8000/csv-para-json
Convertendo JSON para CSV
Bash

# O '-o' salva a saída diretamente em um novo arquivo.
curl -X POST -F "file=@caminho/para/seu/lendas.json" http://127.0.0.1:8000/json-para-csv -o convertido.csv
🧪 Como Rodar os Testes
Para garantir a integridade e o bom funcionamento da API, execute a suíte de testes com pytest:

Bash

poetry run pytest
Ou, se você configurou o task, use:

Bash

task test
📂 Estrutura de Pastas
O projeto segue uma estrutura moderna com a pasta src para separar o código-fonte dos arquivos de configuração e testes:

├── src/
│   └── datamorph/      <-- O pacote principal da nossa aplicação
│       ├── __init__.py
│       ├── core.py     <-- A "cozinha": toda a lógica de conversão
│       └── main.py     <-- O "salão": os endpoints da API com FastAPI
├── tests/              <-- A "academia": todos os testes automatizados
│   └── test_main.py
└── pyproject.toml      <-- O "RG" do projeto, com todas as dependências
Feito com muito café, açaí e uma pitada de desespero de madrugada em Santarém-PA, Brasil. 🇧🇷
