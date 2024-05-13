from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# WTForm for registering new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6), ])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Sign Me Up!")


# WTForm for logging in existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# WTForm for user commenting
class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
