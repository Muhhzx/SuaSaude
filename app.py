from flask import Flask, render_template
from extensions import db
from controllers.agua_controller import agua_bp
from controllers.plano_controller import bp as plano_bp
from controllers.IMC_controller import imc_bp
import os

app = Flask(__name__)

# --- Configuração dinâmica do banco ---
database_url = os.getenv("DATABASE_URL")

if database_url:
    # Corrige caso Render forneça postgres:// (SQLAlchemy espera postgresql://)
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Local → usa SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "chave_super_segura")

# Inicializa DB
db.init_app(app)

# --- Blueprints ---
app.register_blueprint(agua_bp)
app.register_blueprint(plano_bp)
app.register_blueprint(imc_bp)

# --- Rotas extras ---
@app.route('/Sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/Imc')
def imc():
    return render_template('imc.html')


# --- Execução ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
