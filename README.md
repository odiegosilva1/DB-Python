
```
# Projeto com Peewee

## Descrição
Projeto simples utilizando Python e Peewee ORM para gerenciamento de registros com geração automática de IDs.

## Pré-requisitos
- Python 3.x
- pip3

## Configuração do Ambiente

1. **Clone o repositório**
```bash
git clone https://github.com/odiegosilva1/DB-Python
cd DB-Python
```

2. **Crie e ative o ambiente virtual**
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip3 install peewee
```

## Como Executar

Execute o script principal:
```bash
python3 main.py
```

## Funcionalidades
- Cada novo registro na tabela gera um ID automaticamente
- Utiliza Peewee como ORM para interação com o banco de dados

## Estrutura do Projeto
```
├── .venv/          # Ambiente virtual
├── main.py         # Script principal
└── README.md       # Este arquivo
```

## Observações
- Certifique-se de estar com o ambiente virtual ativado antes de executar o projeto
- O ID é gerado automaticamente a cada novo registro inserido na tabela
```

