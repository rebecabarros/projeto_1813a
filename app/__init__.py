from flask import Flask

app = Flask(__name__) #construtor

#importar as views
from app import views