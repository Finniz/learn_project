from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль',validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "from-check-input"})
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-dark"})

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя',validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Электронная почта',validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль',validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль',validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-dark"})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('Это имя уже занято!')

    def validate_email(self, email):
        mail_count = User.query.filter_by(email=email.data).count()
        if mail_count > 0:
            raise ValidationError('Пользователь с такой почтой уже существует!')
