# 🚀 Flask GitHub Style Authentication

Um sistema de autenticação moderno construído com Flask, apresentando uma interface inspirada no GitHub com design responsivo e foco em UX.

![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![CSS3](https://img.shields.io/badge/CSS3-GitHub%20Style-blue?style=flat-square&logo=css3)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Windows](https://img.shields.io/badge/Windows-Supported-0078D6?style=flat-square&logo=windows)
![Linux](https://img.shields.io/badge/Linux-Supported-FCC624?style=flat-square&logo=linux)
```markdown


## ✨ Funcionalidades

- 🎨 **Design Inspirado no GitHub** - Interface moderna com paleta de cores do GitHub Dark
- 📱 **Totalmente Responsivo** - Adapta-se perfeitamente a todos os dispositivos (mobile, tablet, desktop)
- 🔒 **Sistema de Autenticação** - Formulário de login/cadastro funcional
- 🧩 **Templates Jinja2** - Estrutura modular com herança de templates
- 🎯 **Centralização Perfeita** - Containers alinhados horizontal e verticalmente
- ⚡ **Animações Suaves** - Transições e efeitos hover otimizados
- ♿ **Acessibilidade** - Suporte a navegação por teclado e prefers-reduced-motion
- 🖥️ **Cross-Platform** - Funciona perfeitamente no Windows e Linux

## 📋 Pré-requisitos

### Para ambos os sistemas:
- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)
- Navegador moderno (Chrome, Firefox, Safari, Edge)

### Windows:
- Windows 10 ou superior
- PowerShell ou Command Prompt (CMD)

### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Linux (Fedora/RHEL):
```bash
sudo dnf install python3 python3-pip python3-virtualenv
```

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Jinja2
- **Estilização**: CSS Custom Properties (variáveis CSS)
- **Metodologia**: Mobile First, Responsive Design

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/odiegosilva1/flask-github-style.git
cd flask-github-style
```

### 2. Crie e ative um ambiente virtual

#### 🪟 **Windows (Command Prompt)**
```cmd
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

#### 🪟 **Windows (PowerShell)**
```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Se ocorrer erro de permissão, execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 🐧 **Linux/Mac**
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

### 3. Instale as dependências

Após ativar o ambiente virtual, você verá o nome do ambiente no terminal:
- Windows: `(venv) C:\projeto>`
- Linux: `(venv) usuario@computador:~/projeto$`

#### 📦 **Opção 1: Instalar via requirements.txt (recomendado)**
```bash
# Atualizar o pip para a versão mais recente
pip install --upgrade pip

# Instalar todas as dependências
pip install -r requirements.txt
```

#### 🚀 **Opção 2: Instalação rápida (apenas Flask)**
```bash
# Instalar apenas o Flask
pip install flask

# Criar o arquivo requirements.txt
pip freeze > requirements.txt
```

### 4. Verifique a instalação
```bash
# Verificar se o Flask foi instalado corretamente
python -c "import flask; print(f'✅ Flask {flask.__version__} instalado com sucesso!')"
```

## 🚀 Executando o Projeto

### 1. Certifique-se que o ambiente virtual está ativado
- O terminal deve mostrar `(venv)` no início da linha

### 2. Execute a aplicação
```bash
python app.py
```

### 3. Acesse no navegador
```
http://localhost:5000
```

### 4. Para parar a aplicação
Pressione `CTRL + C` no terminal

## 📁 Estrutura do Projeto

```
flask-github-style/
│
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências do projeto
├── README.md             # Documentação
├── .gitignore            # Arquivos ignorados pelo Git
│
├── templates/            # Templates Jinja2
│   ├── base.html        # Template base
│   ├── index.html       # Página inicial
│   └── form.html        # Página de login
│
└── static/              # Arquivos estáticos
    └── styles/
        └── style.css    # Estilos CSS
```

## 🎨 Paleta de Cores

O projeto utiliza a paleta oficial do GitHub Dark Mode:

| Cor | Código | Uso |
|-----|--------|-----|
| Fundo principal | `#0d1117` | Body background |
| Cards/Containers | `#161b22` | Formulários e containers |
| Bordas | `#30363d` | Separadores e inputs |
| Texto principal | `#f0f6fc` | Títulos |
| Texto secundário | `#8b949e` | Parágrafos e labels |
| Links | `#4493f8` | Navegação e links |
| Botões | `#238636` | Botões de ação |

## 📱 Responsividade

O projeto é totalmente responsivo com breakpoints para:

- **Desktop Grande** (1200px+)
- **Desktop** (992px - 1199px)
- **Tablet** (768px - 991px)
- **Mobile Landscape** (481px - 767px)
- **Mobile Portrait** (320px - 480px)
- **Telas muito pequenas** (abaixo de 320px)

## 🔧 Personalização

### Alterando Cores

As cores são gerenciadas através de variáveis CSS no arquivo `style.css`:

```css
:root {
    --cor-principal: #238636;
    --cor-fundo: #0d1117;
    --cor-card: #161b22;
    --cor-texto-azul: #4493f8;
    /* Altere estas variáveis para personalizar */
}
```

### Adicionando Novas Rotas

No arquivo `app.py`:

```python
@app.route('/nova-rota')
def nova_rota():
    return render_template('nova_pagina.html')
```

### Criando Novas Páginas

1. Crie um novo template estendendo `base.html`:
```html
{% extends "base.html" %}

{% block title %}Minha Página{% endblock %}

{% block content %}
<div class="container">
    <h1>Conteúdo Personalizado</h1>
    <p>Seu conteúdo aqui...</p>
</div>
{% endblock %}
```

## 🌟 Destaques do Código

### Template Base com Jinja2
```html
{% block content %}{% endblock %}
```

### URLs Dinâmicas
```html
<a href="{{ url_for('home') }}">Home</a>
```

### Context Processor para Data Atual
```python
@app.context_processor
def inject_now():
    return {'now': datetime.now()}
```

### CSS Moderno com Variáveis
```css
:root {
    --espacamento-padrao: 20px;
    --fonte-media: 1rem;
    --border-radius: 6px;
}
```

## 🐛 Solução de Problemas Comuns

### Erro: "pip não encontrado"
```bash
# Windows: Use python -m pip
python -m pip install -r requirements.txt

# Linux: Instale o pip
sudo apt install python3-pip
```

### Erro: "python não encontrado"
```bash
# Verifique a instalação do Python
python --version
python3 --version

# Windows: Adicione Python ao PATH
# Linux: Instale o Python
sudo apt install python3
```

### Erro de permissão no PowerShell
```powershell
# Execute como administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro: "Flask não encontrado" mesmo após instalação
```bash
# Verifique se o ambiente virtual está ativado
# O terminal deve mostrar (venv)

# Reinstale o Flask
pip uninstall flask
pip install flask
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Diego Silva** - [@odiegosilva1](https://github.com/odiegosilva1)

## 🙏 Agradecimentos

- [Flask](https://flask.palletsprojects.com/) - Framework web
- [GitHub](https://github.com/) - Inspiração para o design
- Comunidade open-source por todas as ferramentas incríveis

## 📞 Suporte

Se você tiver alguma dúvida ou encontrar algum problema, por favor:
- Abra uma [issue](https://github.com/odiegosilva1/flask-github-style/issues)
- Entre em contato via [email](mailto:seu-email@example.com)

---

⭐️ Desenvolvido com ❤️ e Python | Inspirado no GitHub Design System
```

## 📄 **requirements.txt**

```txt
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.2
click==8.1.7
itsdangerous==2.1.2
markupsafe==2.1.3
```

## 🔧 **Arquivo .gitignore**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
.env
.venv

# Flask
instance/
.webassets-cache

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
*.sqlite
*.sqlite3

# Coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.pytest_cache/
```

