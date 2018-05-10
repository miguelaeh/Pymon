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
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        cid = m.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        if cid > 0:
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
        else:
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.
        f = open( 'log.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
        f.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
        f.close() # Cerramos el fichero para que se guarde.
        print mensaje # Imprimimos el mensaje en la terminal, que nunca viene mal :) 
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

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
    
    cid = m.chat.id
    puerto=161
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
                                                                                 'http://mibs.snmplabs.com/asn1/@mib@')))) #el 0 es porque es la instancia, 
                                                        #para tablas poner donde esta el 0 el oid del objeto columna
    
    if cid == GRUPO:
        
            bot.send_message( GRUPO, 'grupo') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    else :
            bot.send_message( cid, 'individual')
                                                                      

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            bot.send_chat_action(cid, 'typing') # Enviando ...
            time.sleep(1)
            bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))



bot.polling()