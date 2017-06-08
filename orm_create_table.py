#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

eng = create_engine('sqlite:///:memory:')

Base = declarative_base()
 
class Car(Base):
    __tablename__ = "Cars"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)  
    Price = Column(Integer)
        
Base.metadata.bind = eng        
Base.metadata.create_all()        
        
Session = sessionmaker(bind=eng)
ses = Session()    
