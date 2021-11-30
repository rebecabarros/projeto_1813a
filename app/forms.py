from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, URL

class ContatoForm(FlaskForm):
    nome = StringField("Nome: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    mensagem = TextAreaField("Mensagem: ", validators=[DataRequired()])
    submit = SubmitField("Enviar")