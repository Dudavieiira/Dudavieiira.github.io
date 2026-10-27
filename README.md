# Similaridade Textual

Aplicação que calcula a similaridade entre dois textos usando **TF-IDF** e **similaridade do cosseno**.

- **Backend:** API em Python com FastAPI (`backend/app`)
- **Frontend:** página HTML/CSS/JS que envia os textos para a API (`frontend/`)

## Pré-requisitos

- [Python](https://www.python.org/downloads/) 3.10 ou superior
- [Git](https://git-scm.com/downloads) (opcional, para clonar o repositório)

## Como rodar

### 1. Baixar o código

```bash
git clone https://github.com/dudavieiira/dudavieiira.github.io.git
cd dudavieiira.github.io
```

Ou baixe o ZIP pelo botão **Code → Download ZIP** no GitHub e extraia.

### 2. Criar o ambiente virtual e instalar as dependências

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Iniciar a API

```bash
cd backend
uvicorn app.main:app --reload
```

A API fica disponível em `http://127.0.0.1:8000`.
A documentação interativa (Swagger) fica em `http://127.0.0.1:8000/docs`.

### 4. Abrir o frontend

Com a API rodando, abra o arquivo `frontend/index.html` no navegador (duplo clique no arquivo),
digite os dois textos e clique em **Comparar**.

## Endpoint

`POST /similaridade`

Requisição:

```json
{
  "texto1": "o gato subiu no telhado",
  "texto2": "o gato desceu do telhado"
}
```

Resposta:

```json
{
  "similaridade_percentual": 33.61
}
```

## Scripts de teste

Os scripts em `backend/app/teste_*.py` testam as funções isoladamente. Para rodá-los:

```bash
cd backend/app
python teste_similaridade.py
```

## Estrutura

```
backend/app/
  main.py              ← API FastAPI (rota /similaridade)
  text_analysis.py     ← pré-processamento e cálculo da similaridade
  teste_*.py           ← scripts de teste
frontend/
  index.html, script.js, style.css
docs/                  ← diagramas e prints
requirements.txt       ← dependências Python
```
