## SuaSaúde.
[![GitHub repo](https://img.shields.io/badge/GitHub-SuaSaude-blue?style=flat-square)](https://github.com/Muhhzx/SuaSaude)  
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?style=flat-square)](https://flask.palletsprojects.com/)  

#**SuaSaúde** é um aplicativo de monitoramento de saúde que ajuda os usuários a gerenciar **hidratação, metas de água, IMC e dicas de nutrição**, oferecendo uma interface simples e intuitiva.  

Este projeto é ideal para **portfólio**, demonstrando habilidades em **desenvolvimento full-stack com Flask e front-end tradicional (HTML + CSS)**.

---

## 🌟 Funcionalidades Principais

### 💧 Monitoramento de Hidratação
- Registro da ingestão diária de água  
- Definição de metas personalizadas  
- Visualização do progresso diário  

### ⚖️ Cálculo de IMC
- Inserção de altura e peso  
- Avaliação automática da faixa de IMC  
- Sugestão de metas de saúde  

### 🥗 Dicas de Nutrição
- Recomendações para emagrecimento e ganho de massa  
- Sugestões personalizadas com base no IMC  

---

## 💻 Tecnologias Utilizadas

### **Back-End**
- **Flask** — framework web leve e rápido  
- **Flask-SQLAlchemy + SQLite** — armazenamento simples de dados (atualmente)  
- **Planejada migração para PostgreSQL** — ambiente mais profissional e escalável  
- **Alembic (opcional)** — migrations de banco de dados  
- **Docker (opcional)** — containerização  

### **Front-End**
- **HTML5 + CSS3** — interface limpa, responsiva e intuitiva  

### **Extras**
- Boas práticas de **Clean Code** e versionamento com **Git**  
- Estrutura modular e escalável  

---

## 🚀 Como Rodar Localmente
git clone https://github.com/Muhhzx/SuaSaude.git
cd SuaSaude
Configure o ambiente do backend:

cd backend
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
Rode a aplicação Flask:

python app.py
Acesse a aplicação no navegador:
http://localhost:5000
