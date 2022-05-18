from calendar import week
from flask import Flask, flash, url_for, redirect, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKeyConstraint, ForeignKey


from forms import AddEsp, AddProduct

#Creates a Flask Instance and 
app= Flask(__name__)

# CRF token
app.config['SECRET_KEY'] = 'future teksystem consultant'


############################################

# SQL DATABASE SET UP AND MODELS

##########################################
# Connects this paget to db 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ethio4life(001)@localhost/tractortek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

################ MODELS ##########################

# each class will end up as tables in db

class ProductPrice(db.Model):
    __tablename__='prod_price'
    prod_code = db.Column(db.VARCHAR(10), primary_key = True)
    sales_year = db.Column(db.Integer, primary_key = True)
    sales_quarter = db.Column(db.VARCHAR(10), primary_key = True)
    prod_price = db.Column(db.Integer)


    def __init__(self,prod_code,sales_year,sales_quarter,prod_price):
        self.prod_code = prod_code
        self.sales_year = sales_year
        self.sales_quarter = sales_quarter
        self.prod_price = prod_price

class EspPrice(db.Model):
    __tablename__='esp_price'
    esp_code = db.Column(db.VARCHAR(10), primary_key = True)
    sales_year = db.Column(db.Integer, primary_key = True)
    esp_price = db.Column(db.Integer)

    def __init__(self, esp_code,sales_year,esp_price):
        self.esp_code = esp_code
        self.sales_year = sales_year
        self.esp_price = esp_price


class Employee(db.Model):
    __tablename__=('employee')
    
    emp_id = db.Column(db.VARCHAR(10), primary_key = True)
    emp_name = db.Column(db.VARCHAR(50))
    region = db.Column(db.VARCHAR(10))
    pay_grade = db.Column(db.VARCHAR(10))

    def __init__(self,emp_name,region,pay_grade):
        self.emp_name = emp_name
        self.region = region
        self.pay_grade = pay_grade

class ProdoctInfo(db.Model):
    __tablename__='prod_info'

    prod_code = db.Column(db.VARCHAR(10), primary_key=True)
    prod_name = db.Column(db.VARCHAR(100))
    prod_manu = db.Column(db.VARCHAR(100))
    prod_url = db.Column(db.VARCHAR(500))
    prod_link = db.Column(db.VARCHAR(500))

    def __init__(self,prod_code,prod_name,prod_manu,prod_url,prod_link):
        self.prod_code = prod_code
        prod_name = prod_name
        prod_manu = prod_manu
        prod_url = prod_url
        prod_link = prod_link


class DateTable(db.Model):
    __tablename__='date_table'
    week_of_date = db.Column(db.VARCHAR(20), primary_key=True)
    sales_period = db.Column(db.Integer)
    sales_quarter = db.Column(db.VARCHAR(5))
    sales_year = db.Column(db.Integer)

    def __init__(self,week_of_date,sales_period,sales_quarter,sales_year):
        self.week_of_date = week_of_date
        self.period = sales_period
        self.quarter = sales_quarter
        self.sales_year = sales_year


class ProductSale(db.Model):
    __tablename__ = 'prod_sales'

    prod_id = db.Column(db.Integer, primary_key = True)
    emp_id = db.Column(db.VARCHAR(10), ForeignKey('employee.emp_id'))
    week_of_date = db.Column(db.VARCHAR(20), ForeignKey('date_table.week_of_date'))
    prod_code = db.Column(db.VARCHAR(10), ForeignKey('prod_info.prod_code'))
    sales_year = db.Column(db.Integer)
    sales_quarter = db.Column(db.VARCHAR(10))
    unit_sold = db.Column(db.Integer)
    __table_args__=(ForeignKeyConstraint([prod_code, sales_year, sales_quarter], [ProductPrice.prod_code, ProductPrice.sales_year, ProductPrice.sales_quarter]),{})

    def __init__(self,emp_id,week_of_date,prod_code,sales_year,sales_quarter,unit_sold):
        self.emp_id = emp_id
        self.week_of_date = week_of_date
        self.prod_code = prod_code
        self.sales_year = sales_year
        self.sales_quarter = sales_quarter
        self.unit_sold = unit_sold

class EspSale(db.Model):
    __tablename__= 'esp_sales'

    esp_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    emp_id = db.Column(db.VARCHAR(10), ForeignKey('employee.emp_id'))
    week_of_date = db.Column(db.VARCHAR(20), ForeignKey('date_table.week_of_date'))
    esp_code = db.Column(db.VARCHAR(10))
    sales_year = db.Column(db.Integer)
    week_num = db.Column(db.Integer)
    unit_sold = db.Column(db.Integer)
    __table_args__ = (ForeignKeyConstraint([esp_code, sales_year], [EspPrice.esp_code, EspPrice.sales_year]),{})

    def __init__(self,emp_id,week_of_date,esp_code,sales_year,week_num, unit_sold):
        self.emp_id = emp_id
        self.week_of_date = week_of_date
        self.esp_code = esp_code
        self.sales_year = sales_year
        self.week_num = week_num
        self.unit_sold = unit_sold




db.create_all()

############### View function -- Have forms #########################

@app.route('/')
def index ():
    return render_template('home.html')


@app.route('/prod_add', methods = ['GET','POST'])
def prod_add():
    form = AddProduct()

    if form.validate_on_submit():
        emp_id = form.emp_id.data
        week_of_date = form.week_of_date.data
        sales_year = form.sales_year.data
        sales_quarter = form.sales_quarter.data
        prod_code = form.prod_code.data
        unit_sold = form.unit_sold.data

        new_prod = ProductSale(emp_id,week_of_date,sales_year,sales_quarter,prod_code,unit_sold)
        db.session.add(new_prod)
        db.session.commit()

        return redirect(url_for('prod_add'))
    return render_template('prod_add.html', form = form)

# This makes the esp_add page, where employees will enter data
@app.route('/esp_add', methods = ['GET','POST'])
def esp_add():
    form = AddEsp()

    if form.validate_on_submit():
       
        emp_id = form.emp_id.data
        week_of_date = form.week_of_date.data
        esp_code = form.esp_code.data
        sales_year = form.sales_year.data
        week_num = form.week_num.data
        unit_sold = form.unit_sold.data

        new_esp = EspSale(emp_id,week_of_date,esp_code,sales_year,week_num,unit_sold)
        db.session.add(new_esp)
        db.session.commit()

        form.emp_id.data = form.emp_id.data
        flash("Sale Submitted Successfully")

        return redirect(url_for('esp_add'))
    return render_template("esp_add.html", form = form)


if __name__ == '__main__':
    app.run(debug=True)



        



    





