import telebot # Libreria de la API del bot.
from telebot import * # Tipos para la API del bot.
import time # Libreria para hacer que el programa que controla el bot no se acabe.
from snmp_get import snmp_get

 
 
# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondriamos grupo= -XXXXX 
 
TOKEN = '563209742:AAHsXl1ZoUIZDYCBTR52oxezfxHKdCoDb8E' # Nuestro token del bot.
 
AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'
 
ip = "0.0.0.0"

 
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

@bot.message_handler(commands=['prueba'])
def command_prueba(m):

	global ip
	cid = m.chat.id
	aux = m.text.split(" ")
	if len(aux)==3:
		oidObjeto = aux[1]
		oidInstancia = aux[2]
		varBinds = snmp_get(ip, "public", "IF-MIB", oidObjeto,oidInstancia)
		for varBind in varBinds:
	        	bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))
	else:
		bot.send_message(cid,"Error de formato")

@bot.message_handler(commands=['printip'])
def command_printip(m):
	
	cid = m.chat.id
	bot.send_message(cid, ip)

bot.polling()
