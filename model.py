from sqlalchemy import create_engine, ForeignKey, Column, String, Float, CHAR ,Boolean ,Integer ,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask , redirect , render_template ,request


# creation of data base 


base = declarative_base()

engine2 = create_engine("sqlite:///Regisster4.db", echo=True)
base.metadata.create_all(bind=engine2)
Session = sessionmaker(bind=engine2)
session = Session()


class Register3(base):
    __tablename__ = 'Register4'
    id = Column(Integer, primary_key=True)
    Nrapport = Column('Nrapport', String)
    officer = Column('officer', String)
    dateOfDoing = Column('dateOfDoing', String)
    Identity = Column('Identity', String)
    doctor = Column('doctor', String)
    OrderProsecution = Column('OrderProsecution', String)
    deputy = Column('deputy', String)
    NFile = Column('NFile', Integer)


    def __init__(self, id, Nrapport ,officer, dateOfDoing , Identity, doctor , OrderProsecution  ,deputy ,NFile ) :
        self.id = id
        self.Nrapport = Nrapport
        self.officer = officer
        self.dateOfDoing = dateOfDoing
        self.Identity = Identity
        self.doctor = doctor
        self.OrderProsecution = OrderProsecution
        self.deputy = deputy
        self.NFile = NFile
       

    def __repr__(self):
        return f"({self.id} {self.officer} {self.Nrapport} {self.dateOfDoing} {self.Identity} {self.doctor} {self.doctor} {self.OrderProsecution} {self.deputy}  {self.NFile})"
    
