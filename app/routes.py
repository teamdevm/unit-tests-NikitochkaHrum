from flask import Flask, render_template, request
from .converter import Converter
from app import app
import os

app.template_folder = os.path.abspath('templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    currency = request.form['currency']
    amount = float(request.form['amount'])
    
    converter = Converter()
    converted_amount = converter.convert_bitcoins(currency, amount)
    converted_amount = '{:,.6f}'.format(converted_amount)
    
    return render_template('result.html', currency=currency, amount=amount, converted_amount=converted_amount)