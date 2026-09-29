# Automação de cadastro de produtos

Projeto em Python que lê uma base de produtos em CSV e automatiza o cadastro
dos dados em um formulário web usando PyAutoGUI.

## Funcionalidades

- leitura dos produtos com pandas;
- preenchimento automático dos campos do formulário;
- tratamento de observações vazias;
- leitura segura de e-mail e senha, sem armazená-los no código.

## Requisitos

- Python 3.11 ou superior;
- Google Chrome;
- coordenadas do PyAutoGUI calibradas para o seu monitor.

## Instalação

Abra o PowerShell na pasta do projeto e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

No VS Code, selecione o interpretador `.venv\Scripts\python.exe`.

## Configuração

Execute o arquivo auxiliar para descobrir a posição atual do mouse:

```powershell
python pegar_posicao.py
```

Depois, ajuste em `codigo.py` as coordenadas dos campos de login e de código do
produto. Coordenadas negativas podem ser normais quando se utiliza um segundo
monitor posicionado à esquerda do monitor principal.

## Execução

```powershell
python codigo.py
```

O programa pedirá o e-mail e a senha antes de abrir o navegador. Para interromper
a automação, mova rapidamente o mouse para um dos cantos da tela.

## Arquivo de dados

O arquivo `produtos.csv` deve possuir as seguintes colunas:

```text
codigo, marca, tipo, categoria, preco, custo, obs
```

## Observação

Use esta automação somente em sistemas nos quais você tenha autorização para
inserir dados.
