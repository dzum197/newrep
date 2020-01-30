from sqlalchemy import (Column, String, Integer, 
                        Text, Date, Boolean, ForeignKey, 
                        create_engine)
from sqlalchemy import Session, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///app.db', echo=True)
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    registered_on = Column(Date, default=datetime.date.today())

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(20), unique=True, nullable=False)
    description = Column(Text)
    created_on = Column(Date, default=datetime.date.today()) 
    deadline = Column(Date)    
    status = Column(Boolean, default=0)                  
    
    def __str__(self):
        return '\n'.join([self.id,
                        self.user_id, 
                        self.title, 
                        self.description, 
                        self.created_on, 
                        self.deadline,
                        self.status])

Base.metadata.create_all()








def add_user(name, email, password):
    engine = create_engine('sqlite:///app.db', echo=True)
    session = Session(bind=engine)
    session.add(User(name=name, email=email, password=password))
    session.commit()
    session.close()

def check_user(email, password):
    engine = create_engine('sqlite:///app.db', echo=True)
    session = Session(bind=engine)
    session.query(User).filter_by(email=email, password=password).first()


