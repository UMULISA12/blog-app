from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    # category = StringField('Write a pitch category', validators=[Required()])
    blog = TextAreaField('Write a blog', validators=[Required()])
    # author = StringField('enter your name', validators=[Required()])
    Submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    Bio = TextAreaField('Tell us about you.',validators = [Required()])
    Submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment= TextAreaField('comment', validators=[Required()])
    author = StringField('enter your name', validators=[Required()])
    Submit = SubmitField('Submit')