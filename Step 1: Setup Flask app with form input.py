from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import requests
from bs4 import BeautifulSoup
import os
from io import BytesIO
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup SQLite DB
engine = create_engine('sqlite:///cases.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class CaseQuery(Base):
    __tablename__ = 'case_queries'
    id = Column(Integer, primary_key=True)
    case_type = Column(String)
    case_number = Column(String)
    year = Column(String)
    raw_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
