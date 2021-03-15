from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title',
    validators=
    [
        DataRequired()
        ]
    )

    bedrooms=StringField('No. of Rooms', 
    validators=
    [
        DataRequired()
        ]
    )

    bathrooms=StringField('No. of Bathrooms',
    validators=
    [
        DataRequired()
        ]
    )

    location=StringField('Location',
    validators=
    [
        DataRequired()
        ]
    )

    price=StringField('Price',
    validators=
    [
        DataRequired()
        ]
    )

    houseType= SelectField('Property Type',
    choices=[('House','House'),('Apartment','Apartment')])

    description = TextAreaField('Description',
    validators=
    [
        DataRequired()
        ]
    )

    photo=FileField('Photo', 
    validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'Image Files Only'])
    ]
    )