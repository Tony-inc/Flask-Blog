from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterUser(FlaskForm):
    name = StringField("Your name", validators=[DataRequired()])
    email = EmailField("Your email", validators=[DataRequired(), Email()])
    password = PasswordField("Your password", validators=[DataRequired(), Length(min=3, message="The min number of characters is 3")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Your email", validators=[DataRequired(), Email()])
    password = PasswordField("Your password", validators=[DataRequired()])
    submit = SubmitField("Log in")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")