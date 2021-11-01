from googletrans import Translator
from language_translator import app
from flask import render_template, url_for, redirect, flash, request

#from language_translator.forms import UserInput
#from language_translator.models import TranslateModule

'''class TranslateModule:
	def __init__(self,user):
		self.user = user
	def translate(user):	
		translator = Translator()
		print(translator.translate(user));

TranslateModule.translate(user)'''

#index page route
@app.route('/')
def index():
	#return to user index page upon typing /index.html at end of url
	return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def translate_form_post():
	#make user the variable to pass into the class
	user = request.form['text']
	translator = Translator()
	#variable using translator translating the object 'user'
	processed_text = translator.translate(user)
	#update index.html with the proessed text
	return render_template('index.html', message=processed_text.text, language=processed_text.src)




#need to process text with the class
#import class, pass it into the function?