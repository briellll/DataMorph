# 🐲 DataMorph API  
Seu tradutor de arquivos juramentado, direto da Amazônia para o mundo!

---

## 🎯 Sobre o Projeto

**DataMorph** é uma API parruda e veloz construída com **FastAPI** para a conversão *bidirecional* de arquivos entre os formatos **CSV** e **JSON**.

Cansado de abrir planilhas e salvar como? Ou de procurar conversores online duvidosos? Seus problemas acabaram! 💾🧙‍♂️

Este projeto utiliza o poder do **Pandas** por baixo dos panos para garantir uma conversão de dados robusta e eficiente, lidando até mesmo com arquivos malformados de forma inteligente.

---

## ✨ Funcionalidades

- ✅ Conversão de arquivos **CSV → JSON**
- ✅ Conversão de arquivos **JSON → CSV**
- ✅ Validação de **formato de arquivo** (aceita só o que promete!)
- ✅ Validação de **conteúdo malformado**, rejeitando arquivos "quebrados"
- ✅ Documentação interativa com **Swagger UI** em `/docs`
- ✅ Respostas de erro claras e padronizadas

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído com o melhor que o ecossistema Python tem a oferecer:

- 🐍 **Python 3.13**
- ⚡ **FastAPI** – construção da API assíncrona
- 🐼 **Pandas** – motor da manipulação e conversão dos dados
- 🚀 **Uvicorn** – servidor ASGI para colocar tudo no ar
- 📦 **Poetry** – gerenciamento de dependências e ambientes
- 🧪 **Pytest** – testes automatizados para manter tudo nos eixos

---

## 🚀 Como Rodar o Projeto

### ✅ Pré-requisitos

- Python 3.13+
- [Poetry](https://python-poetry.org/) instalado

### 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/briellll/datamorph.git
cd datamorph
```

Instale as dependências:

```bash
poetry install
```

Inicie o servidor da API:

```bash
poetry run uvicorn datamorph.main:app --reload
```

> O `--reload` reinicia o servidor automaticamente a cada alteração no código. Mão na roda!

### 🌐 Acesse:

- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🕹️ Como Usar a API

A forma mais prática é via `/docs`, onde é possível fazer upload de arquivos diretamente pelo navegador.

Para os mais "hackers", temos o bom e velho `curl`:

### 📤 Convertendo CSV para JSON

```bash
curl -X POST -F "file=@caminho/para/seu/arquivo.csv" http://127.0.0.1:8000/csv-para-json
```

### 📥 Convertendo JSON para CSV

```bash
curl -X POST -F "file=@caminho/para/seu/lendas.json" http://127.0.0.1:8000/json-para-csv -o convertido.csv
```

---

## 🧪 Rodando os Testes

Para garantir que tudo funcione como deveria:

```bash
poetry run pytest
```

Ou, se tiver `task` configurado:

```bash
task test
```

---

## 📂 Estrutura de Pastas

```
datamorph/
├── src/
│   └── datamorph/        # O pacote principal da aplicação
│       ├── __init__.py
│       ├── core.py       # A "cozinha": lógica de conversão
│       └── main.py       # O "salão": endpoints da API
├── tests/                # A "academia": testes automatizados
│   └── test_main.py
└── pyproject.toml        # O "RG" do projeto
```

---

> Feito com muito ☕, 🍧 açaí e uma pitada de desespero de madrugada em **Santarém - PA, Brasil** 🇧🇷
