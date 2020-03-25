from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FloatField, StringField
from wtforms.validators import DataRequired, Length

class ChartForm(FlaskForm):
    start_x = IntegerField("Give a starting number for 'x': ", validators=[DataRequired()])
    end_x = IntegerField("Give an ending number for 'x': ", validators=[DataRequired()])
    coeff_a = FloatField("Give a number to 'a': ", validators=[DataRequired()])
    coeff_b = FloatField("Give a number to 'b': ", validators=[DataRequired()])
    coeff_c = FloatField("Give a number to 'c': ", validators=[DataRequired()])
    color = StringField("Select color of your curve: ")
    submit = SubmitField("Draw!")

class PieColumnForm(FlaskForm):
    number_of_rows = IntegerField("Select number of rows: ", validators=[DataRequired(), Length(min=2)])
    submit = SubmitField("Continue")
    draw = SubmitField("Draw")


