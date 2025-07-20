<<<<<<< HEAD
from flask import Flask, render_template, request
from extensions import db
from controllers.agua_controller import agua_bp
from controllers.plano_controller import bp as plano_bp



=======
from flask import Flask
from extensions import db
from controllers.agua_controller import agua_bp
from controllers.plano_controller import plano_bp
>>>>>>> e45a6c4f1ecd2c38b1d73029cade3c243dd2f10c

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
app.config['SECRET_KEY'] = 'chave_super_segura'

db.init_app(app) 

app.register_blueprint(agua_bp)
app.register_blueprint(plano_bp)
<<<<<<< HEAD
@app.route('/SOBRE')
def sobre():
    return render_template('sobre.html')

=======
>>>>>>> e45a6c4f1ecd2c38b1d73029cade3c243dd2f10c

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
