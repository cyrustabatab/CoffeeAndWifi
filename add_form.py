from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired,URL



class AddForm(FlaskForm):

    name = StringField('Cafe Name',validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps(URL)',validators=[DataRequired(),URL()])
    opening= StringField('Opening Time e.g. 8AM',validators=[DataRequired()])
    closing= StringField('Closing Time e.g. 7PM',validators=[DataRequired()])
    rating= SelectField('Coffee Rating',choices=[(u'\u2615',u'\u2615'),(u'\u2615\u2615',u'\u2615\u2615'),(u'\u2615\u2615\u2615',u'\u2615\u2615\u2615'),(u'\u2615\u2615\u2615\u2615',u'\u2615\u2615\u2615\u2615'),(u'\u2615\u2615\u2615\u2615\u2615',u'\u2615\u2615\u2615\u2615\u2615')],validators=[DataRequired()])
    wifi= SelectField('Wifi Strength Rating',choices=[(u'\u274C',u'\u274C'),(u'\U0001F4AA',u'\U0001F4AA'),(u'\U0001F4AA\U0001F4AA',u'\U0001F4AA\U0001F4AA'),(u'\U0001F4AA\U0001F4AA\U0001F4AA',u'\U0001F4AA\U0001F4AA\U0001F4AA'),(u'\U0001F4AA\U0001F4AA\U0001F4AA\U0001F4AA',u'\U0001F4AA\U0001F4AA\U0001F4AA\U0001F4AA'),(u'\U0001F4AA\U0001F4AA\U0001F4AA\U0001F4AA\U0001F4AA',u'\U0001F4AA\U0001F4AA\U0001F4AA\U0001F4AA\U0001F4AA')],validators=[DataRequired()])
    powersocket= SelectField('Power Socket Availability',choices=[(u'\u274C',u'\u274C'),(u'\U0001F50C',u'\U0001F50C'),(u'\U0001F50C\U0001F50C',u'\U0001F50C\U0001F50C'),(u'\U0001F50C\U0001F50C\U0001F50C',u'\U0001F50C\U0001F50C\U0001F50C'),(u'\U0001F50C\U0001F50C\U0001F50C\U0001F50C',u'\U0001F50C\U0001F50C\U0001F50C\U0001F50C'),(u'\U0001F50C\U0001F50C\U0001F50C\U0001F50C\U0001F50C',u'\U0001F50C\U0001F50C\U0001F50C\U0001F50C\U0001F50C')],validators=[DataRequired()])
    submit = SubmitField("Add")
