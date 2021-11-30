from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__) #construtor
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'batatinha123'

#importar as views
from app import views