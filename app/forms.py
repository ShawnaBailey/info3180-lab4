from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField
from wtforms.validators import DataRequired

class uploadForm(FlaskForm):
    image = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])