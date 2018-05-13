# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from pysnmp.hlapi import *

 
 
# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX 
 
TOKEN = '563209742:AAHsXl1ZoUIZDYCBTR52oxezfxHKdCoDb8E' # Nuestro token del bot.
 
AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'
 
GRUPO = -1001201542913 #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá
 
 
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
############################################# 
#Listener

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'
 
@bot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_chat_action(cid, 'typing') # Enviando ...
    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
    bot.send_message( cid, AYUDA) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

@bot.message_handler(commands=['info']) # Indicamos que lo siguiente va a controlar el comando '/info'
def command_info(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    if cid == GRUPO:
        
            bot.send_message( GRUPO, 'mensaje A') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    else :
            bot.send_message( cid, 'mensaje B')

@bot.message_handler(commands=['get'])
def command_get(m):
    
    puerto = 161 
    cid = m.chat.id
    ip = '10.10.10.1'
    community = "public"
    mib = 'SNMPv2-MIB'
    oidObjeto = 'snmpInPkts'
    oidInstancia = 0




    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData(community, mpModel=0),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, oidObjeto, oidInstancia).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))) #el 0 es porque es la instancia               

    if errorIndication:
        print(errorIndication)
        bot.send_message(cid,'Error')
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        bot.send_message(cid,'Error')
    else:
        for varBind in varBinds:
            bot.send_chat_action(cid, 'typing') # Enviando ...
            time.sleep(1)
            bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))



@bot.message_handler(commands=['set'])
def command_set(m):

	puerto = 161
	cid = m.chat.id


	ip = raw_input("Introduzca IP: ")
	community = raw_input("Introduzca community: ")
	mib = raw_input("Introduzca nombre de la MIB: ") #la mib es el oid de la mib
	idObjeto = raw_input("Introduzca Id del objeto: ")
	oidInstancia = raw_input("Introduzca oid de la instancia: ")
	value = raw_input("Introduzca el nuevo valor: ")

	errorIndication, errorStatus, errorIndex, varBinds = next(
		setCmd(SnmpEngine(),
         	CommunityData(community),
            UdpTransportTarget((ip, puerto)),
            ContextData(),
            ObjectType(ObjectIdentity(mib, idObjeto, oidInstancia), value).addAsn1MibSource('file:///usr/share/snmp',
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))


	if errorIndication:
    	print(errorIndication)
    	bot.send_message(cid,'Error')
	elif errorStatus:
    	print('%s at %s' % (errorStatus.prettyPrint(),
                     	   errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    	bot.send_message(cid, 'Error')
	else:
    	for varBind in varBinds:
    		bot.send_chat_action(cid, 'typing') # Enviando ...
        	time.sleep(1)
        	bot.send_message(cid, ' = '.join([x.prettyPrint() for x in varBind]))

bot.message_handler(commands=['prueba'])
def command_prueba(m):

	cid = m.chat.id
	send_message(cid,'Envia')
	mensaje = update.m.text
	send_message(cid,mensaje)


bot.polling()