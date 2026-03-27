
# 🚀 Flask GitHub Style Authentication

Um sistema de autenticação moderno construído com Flask, apresentando uma interface inspirada no GitHub com design responsivo e foco em UX.

![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![CSS3](https://img.shields.io/badge/CSS3-GitHub%20Style-blue?style=flat-square&logo=css3)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
```markdown


## ✨ Funcionalidades

- 🎨 **Design Inspirado no GitHub** - Interface moderna com paleta de cores do GitHub Dark
- 📱 **Totalmente Responsivo** - Adapta-se perfeitamente a todos os dispositivos (mobile, tablet, desktop)
- 🔒 **Sistema de Autenticação** - Formulário de login/cadastro funcional
- 🧩 **Templates Jinja2** - Estrutura modular com herança de templates
- 🎯 **Centralização Perfeita** - Containers alinhados horizontal e verticalmente
- ⚡ **Animações Suaves** - Transições e efeitos hover otimizados
- ♿ **Acessibilidade** - Suporte a navegação por teclado e prefers-reduced-motion

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Flask 2.0 ou superior
- Navegador moderno (Chrome, Firefox, Safari, Edge)

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Jinja2
- **Estilização**: CSS Custom Properties (variáveis CSS)
- **Metodologia**: Mobile First, Responsive Design

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/flask-github-style.git
cd flask-github-style
```

2. Crie e ative um ambiente virtual:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install flask
```

## 🚀 Executando o Projeto

1. Execute a aplicação:
```bash
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

## 📁 Estrutura do Projeto

```
flask-github-style/
│
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências do projeto
├── README.md             # Documentação
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

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Seu Nome - [@seu-usuario](https://github.com/odiegosilva1)

---

⭐️ Desenvolvido com Flask e inspirado no GitHub Design System
```

## 📄 **requirements.txt**

```txt
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.2
```

## 🔧 **Arquivo .gitignore** (adicional recomendado)

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

# Flask
instance/
.webassets-cache

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

## 🎯 **Como Contribuir**

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 **Suporte**

Se você tiver alguma dúvida ou encontrar algum problema, por favor:
- Abra uma [issue](https://github.com/odiegosilva1/flask-github-style/issues)
- Entre em contato via email

---

**Feito com ❤️ e Python**
