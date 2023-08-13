from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
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

ScreenManager:
	Log:
		name: "logi"
	Oi:
		name: "oi"


<Log>
	MDFloatLayout:
	
		name: "logi"
		md_bg_color: 0.85, 0.95, 1, 1
	
		MDTextField:
			hint_text: "Usuario"
			multiline: True
			id: usuario
		
			size_hint_x: 0.8
			color_mode: 'custom'
		
		
			pos_hint: {"center_x":0.5, "center_y": 0.50}
	
	
		MDTextField:
			hint_text: "Senha"
			id: senha
		
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


<Oi>
	MDFloatLayout:
	
		name: "oi"
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
			on_press: app.aut()
		
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




class Log(Screen):
	pass

class Oi(Screen):
	pass

sc = ScreenManager()


class auto(MDApp, App):
    
    
    #def spam(self, *args):
#    	
#    	
#    	url = f"https://discord.com/api/v10/channels/{chat}/messages"
#    	header = {"authorization": token}
#    	payload = {'content': texto[random.randint(0, 2)]}
#    	r = requests.post(f'https://discord.com/api/v10/channels/{chat}/messages', data=payload, headers=header)
#    
#    	try:
#    		print(r.json()["content"])
#    		self.root.get_screen('oi').ids.mens.text = "Sucesso"
#    	except:
#    		self.root.get_screen('oi').ids.mens.text = "Error\nVerifique seu token ou o id"
#    		pass
    
    
    
    
    
    def start(self):
    	#Clock.schedule_interval(self.spam, 1)
    	
    	try:
    		req = requests.get(f"https://menudoscria.tttsjatei.repl.co/addapp?token={token}&chat={chat}&id={id}")
    		self.root.get_screen('oi').ids.mens.text = f"Auto ligado no chat: {chat}"
    
    	except:
    		self.root.get_screen('oi').ids.mens.text = "Algo deu errao"
    
   
    	

    
    	
    def build(self):
       self.theme_cls.primary_palette = "Gray"
       
       layout = Builder.load_string(kv)
       return layout
    def login(self):
    
    	token = self.root.get_screen('logi').ids.usuario.text
    	#print(token)
    	chat = self.root.get_screen("logi").ids.senha.text
    	req = requests.get(f"https://menudoscria.tttsjatei.repl.co/getusuario?username={token}&senha={chat}")
    	
    	if str(req.json()) == "[]":
    	   	self.root.get_screen('logi').ids.mens.text = "Usuario ou senha incorreto"
    	else:
    		global id
    		global chatsalv
    		id = req.json()[0][0]
    		chatsalv = req.json()[0][1]
    		
    		
    		self.root.current = "oi"
    		if chatsalv == "nao" or chatsalv == "":
    			pass
    		else:
    			self.root.get_screen('oi').ids.mens.text = f"Auto ligado no chat: {chatsalv}"
    
    	
    


    	   	
    	   	
    	   	
    	   	
    def aut(self):
    	global token
    	global chat
    	token = self.root.get_screen('oi').ids.token.text
    	#print(token)
    	chat = self.root.get_screen("oi").ids.chat.text
    	if token and chat:
    	   	self.start()
    	   	
    	   	
    	   
    	   
    	else:
    		self.root.ids.get_screen("oi").mens.text = "Coloque seu token e o ID do chat"

       
	#def login(self):
		
  

auto().run()
