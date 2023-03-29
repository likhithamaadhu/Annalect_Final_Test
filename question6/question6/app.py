from flask import Flask,request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///inventory.sqlite'

db=SQLAlchemy(app)
app.app_context().push()

class Inventory(db.Model):
    ''' This table contains an inventory information such as name of item, quantities ordered, 
    quantities remaining, vendor name, purchase price per item, selling price per item, date and time when 
    the item was added, date and time when the item was updated. '''
    id=db.Column(db.Integer,primary_key=True)
    itemName=db.Column(db.Text)
    vendorName=db.Column(db.Text)
    quantOrdered=db.Column(db.Integer) # i'm not sure if the table should have two columns for quantity of items -quantOrder
    quantRemaining=db.Column(db.Integer) # and quantRemaining. 
    purchasePrice=db.Column(db.Integer)
    sellingPrice=db.Column(db.Integer)
    dateAdded=db.Column(db.Date)
    dateUpdated=db.Column(db.Date)
    

    def __init__(self,itemName,vendorName,quantOrdered,quantRemaining,purchasePrice,sellingPrice,dateAdded,dateUpdated):
        self.itemName=itemName
        self.vendorName=vendorName
        self.quantOrdered=quantOrdered
        self.quantRemaining=quantRemaining
        self.purchasePrice=purchasePrice
        self.sellingPrice=sellingPrice
        self.dateAdded=dateAdded
        self.dateUpdated=dateUpdated

    def __repr__(self):
        return '{}-{}-{}-{}-{}-{}-{}-{}'.format(self.itemName,self.vendorName,self.quantOrdered,self.quantRemaining
                                                ,self.purchasePrice,self.sellingPrice,self.dateAdded,self.dateUpdated)
        
 
db.create_all()

@app.route('/')
def home(): #home page
    name='likhitha'  #testing whether the app is working or not usinf these variables
    age=22
    return render_template('home.html',name=name,age=age)

app.run(debug=True)