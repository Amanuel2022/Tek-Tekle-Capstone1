from random import choices
from wsgiref.validate import validator
from flask_wtf import FlaskForm
# from pymysql import Date
from wtforms import StringField,IntegerField,SubmitField,DateField,SelectField
from wtforms.validators import DataRequired


# ProductNum = [('PROD_001','PROD_001'),('PROD_002','PROD_002'),('PROD_003','PROD_003'),('PROD_004','PROD_004'),('PROD_005','PROD_005'),('PROD_006','PROD_006'),('PROD_007','PROD_007'),('PROD_008','PROD_008')]

# EspNum = [('ESP_001','PROD_001'),('ESP_002','PROD_002'),('ESP_003','PROD_003'),('ESP_004','PROD_004'),('ESP_005','PROD_005'),('ESP_006','PROD_006'),('ESP_007','PROD_007'),('ESP_008','PROD_008')]

class AddProduct(FlaskForm):

    emp_id = SelectField('Employee ID: ',choices=[('EMP224','Gina Evans'),('EMP256','Harry Lawson'),('EMP234','Jane Bachmann'),('EMP267','Beverly Clement'),('EMP290','Maude Allen')])
    week_of_date = StringField('Todays Date: ')
    sales_year = IntegerField('Sale Year: ')
    sales_quarter = IntegerField('Sale Quarter: ')
    prod_code = SelectField(u'Product Code', choices=[('PROD_001','PROD_001'),('PROD_002','PROD_002'),('PROD_003','PROD_003'),('PROD_004','PROD_004'),('PROD_005','PROD_005'),('PROD_006','PROD_006'),('PROD_007','PROD_007'),('PROD_008','PROD_008')])
    unit_sold = IntegerField('Units sold: ')
    submit = SubmitField('Submit')

class AddEsp(FlaskForm):

    emp_id = SelectField('Employee ID: ',choices=[('EMP224','Gina Evans'),('EMP256','Harry Lawson'),('EMP234','Jane Bachmann'),('EMP267','Beverly Clement'),('EMP290','Maude Allen')])
    week_of_date = StringField('Todays Date: ',validators=[DataRequired()])
    sales_year = IntegerField('Sale Year: ',validators=[DataRequired()])
    week_num = IntegerField('Week Number: ',validators=[DataRequired()])
    esp_code = SelectField(u'ESP Code: ', choices=[('ESP_001','ESP_001'),('ESP_002','ESP_002'),('ESP_003','ESP_003'),('ESP_004','ESP_004'),('ESP_005','ESP_005'),('ESP_006','ESP_006'),('ESP_007','ESP_007'),('ESP_008','ESP_008')])
    unit_sold = IntegerField('Units sold: ',validators=[DataRequired()])
    submit = SubmitField('Submit')