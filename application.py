from flask import Flask , render_template , redirect , request
from sqlalchemy import create_engine, ForeignKey, Column, String, Float, CHAR ,Boolean ,Integer ,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask , redirect , render_template ,request
import model
from model import base 


engine2 = create_engine("sqlite:///Regisster4.db", echo=True)
base.metadata.create_all(bind=engine2)
Session = sessionmaker(bind=engine2)
session = Session()

app = Flask(__name__)
@app.route('/' , methods =["post","get"])
def home():
    if request.method == "POST" and request.form.get("email"):
        listy ={'email':"laaouafifatiha@gmail.com" , 'password':'fatiha123'}
        email = request.form.get("email")
        password = request.form.get("password")
        if (email==listy['email'] and password== listy["password"]):
            return render_template('register.html' , email= email , password= password)
    if request.method == "POST" and request.form.get("numero of rapot"):
        res1 = session.query(model.Register3.id,
                             model.Register3.Nrapport,
                             model.Register3.officer,
                             model.Register3.dateOfDoing,model.Register3.Identity ,
                             model.Register3.doctor , 
                             model.Register3.OrderProsecution , 
                             model.Register3.deputy ,
                             model.Register3.NFile ).all()
        lenght = len(res1)
        p1 = model.Register3 (lenght+1,
                            request.form.get("numero of rapot") ,
                            request.form.get("officer") , 
                            request.form.get("dateOfDoing") ,
                              request.form.get("Identity") ,
                                request.form.get("doctor"),
                                request.form.get("OrderProsecution"),
                                request.form.get("deputy"),
                                request.form.get("NFile"))
        session.add(p1)
        session.commit()
        print("add to data base successful")
       
    return render_template('register.html')

@app.route('/register' , methods =["post","get"])
def register():
     res1 = session.query(model.Register3.id,
                             model.Register3.Nrapport,
                             model.Register3.officer,
                             model.Register3.dateOfDoing,
                             model.Register3.Identity ,
                             model.Register3.doctor , 
                             model.Register3.OrderProsecution , 
                             model.Register3.deputy ,
                             model.Register3.NFile ).all()
     if (res1):
         return render_template('fileData.html' , res1=res1 , lenght = len(res1))
     return 'NO Data Found ! '

@app.route('/order' , methods =["post","get"])
def order():
        res1 = session.query(model.Register3.id,
                                model.Register3.Nrapport,
                                model.Register3.officer,
                                model.Register3.dateOfDoing,
                                model.Register3.Identity ,
                                model.Register3.doctor , 
                                model.Register3.OrderProsecution , 
                                model.Register3.deputy ,
                                model.Register3.NFile ).all()
        
        lenght = len(res1)
        if (res1):

            return render_template('order.html' , Nrapport= res1[lenght-1][1] ,
                               officer= res1[lenght-1][2],    
                               dateOfDoing= res1[lenght-1][3],    
                               order= res1[lenght-1][4],    
                               victime= res1[lenght-1][5],    
                               id= res1[lenght-1][6],    
                               doctor= res1[lenght-1][7],   ) 
                              
        return'No data found'