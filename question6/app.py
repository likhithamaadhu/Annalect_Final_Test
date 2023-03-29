from flask import Flask,request,redirect,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

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
    dateAdded=db.Column(db.String)
    dateUpdated=db.Column(db.String)

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
def home():     #home page
    name='likhitha'  #testing whether the app is working or not using these variables
    age=22
    inventory_items=Inventory.query.all()
    return render_template('home.html',name=name,age=age,inventory_items=inventory_items)

@app.route('/showInventory',methods=['GET'])
def displayInventory():              #it displays all the data in the inventory table
    # inventory_items=Inventory.query.all()
    return jsonify({"message":"Data Displayed Successfully"})

@app.route('/add',methods=['POST'])
def addInventory():                       #it adds the data to the table
    acc=request.get_json()
    itemName=acc['itemName']
    vendorName=acc['vendorName']
    quantOrdered=acc['quantOrdered']
    quantremaining=acc['quantRemaining']
    purchasePrice=acc['purchasePrice']
    sellingPrice=acc['sellingPrice']
    dateAdded=acc['dateAdded']
    dateUpdated=acc['dateUpdated']
    row=Inventory(itemName=itemName,vendorName=vendorName,quantOrdered=quantOrdered,quantRemaining=quantremaining
                  ,purchasePrice=purchasePrice,sellingPrice=sellingPrice,dateAdded=dateAdded,dateUpdated=dateUpdated)
    db.session.add(row)
    db.session.commit()
    return jsonify({"message":"Row Added successfully"})

@app.route('/update/<id>',methods=['PUT'])
def updateInventory(id):                           #it updates a row in the table
    row=Inventory.query.filter_by(id=id).first()
    acc=request.get_json()
    row.itemName=acc['itemName']
    row.vendorName=acc['vendorName']
    row.quantOrdered=acc['quantOrdered']
    row.quantremaining=acc['quantRemaining']
    row.purchasePrice=acc['purchasePrice']
    row.sellingPrice=acc['sellingPrice']
    row.dateAdded=acc['dateAdded']
    row.dateUpdated=acc['dateUpdated']
    db.session.commit()
    return jsonify({"message":"Row Updated Successfully"})



@app.route('/delete/<id>',methods=['DELETE'])
def deleteInventory(id):        #it deletes a row in the table
    row=Inventory.query.filter_by(id=id).first()
    db.session.delete(row)
    db.session.commit()
    return jsonify({"message":"Row Deleted Successfully"})

    
app.run(debug=True)