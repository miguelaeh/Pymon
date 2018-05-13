# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from pysnmp.hlapi import *
from funciones_snmp import *


#Variables globales que necesitaremos utilizar para la gestion, se le asignaran valores por defecto

ip = "0.0.0.0"
community = "public"
mib = "RMON-MIB"

 
# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX 
 
TOKEN = '563209742:AAHsXl1ZoUIZDYCBTR52oxezfxHKdCoDb8E' # Nuestro token del bot.
 

GRUPO = -1001201542913 #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá
 
AYUDA = "Hola buenas, bienvenido a mi servicio de gestión de conmutadores. Me llamo Pymon y voy a darte información sobre los comandos que puedes utilizar conmigo: \n\nComandos de configuración:\n\n/confip - configuración de la ip del conmutador a gestionar.\n/confmib - configuración de la mib a utilizar.\n/confcommunity - configuración de la comunidad que vayas a utilizar.\n/showconf - te muestra la configuración actual.\n\nComandos para la gestión:\n\n/get - realizamos un get con snmp.\n/set - realizamos un set con snmp.\n/getnext - realizamos un getnext con snmp.\n/getbulk - realizamos un getbulk con snmp.\n/createvent - creamos un evento para la sonda RMON ( tenemos que tener previamente la MIB de RMON configurada).\n/createalarm - creamos una alarma para la sonda RMON ( tenemos que tener previamente la MIB de RMON configurada.\n/receptortraps - el último usuario que utilice este comando será el que reciba los traps en su chat con el bot.\n\nSi desea saber que paŕametros han de recibir estos comandos utilice el comando /comandos, los comandos que no aparezcan al introducirlo no necesitarán parámetros."

COMANDOS = "Ahora paso a enseñarte que parámetros has de pasarle a mis comandos:\n\n/get <oidObjeto> <oidInstancia\n/set <oidObjeto> <oidInstancia> <value>\n/getnext <oidObjeto>\n/getbulk <nonRepeaters> <maxRepetitions> <introducidos>\n/createvent <eventDescription> <eventType> <eventCommunity> <eventOwner> <eventIndex>\n/createalarm <indiceAlarma> <indiceEvento> <owner> <interval> <variable> <sampleType> <risingthr> <fallingth>"

BIENVENIDA = "Bienvenido, soy un bot de telegram llamado Pymon utilizado para la gestión de la red. Si desea conocer mi guía de uso utilice el comando /ayuda."

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
############################################# 
#Listener


 


@bot.message_handler(commands=['confip'])
def command_confip(m):

    global ip
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux) == 2:
        ip = aux[1]
        bot.send_message(cid, "IP cambiada satisfactoriamente")
        print "Cambiada la ip a " + ip
    else:
        bot.send_message(cid, "Error de formato")

@bot.message_handler(commands=['confcommunity'])
def command_confcommunity(m):

    global community
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux) == 2:
        community = aux[1]
        bot.send_message(cid, "Comunidad cambiada satisfactoriamente")
        print "Cambiada la comunidad a " + community
    else: 
        bot.send_message(cid, "Error de formato")

@bot.message_handler(commands=['confmib'])
def command_confmib(m):

    global mib
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux) == 2:
        mib = aux[1]
        bot.send_message(cid, "MIB cambiada satisfactoriamente")
        print "Cambiada la MIB utilizada a " + mib
    else:
        bot.send_message(cid, "Error de formato")


@bot.message_handler(commands=['get'])
def command_get(m):

    
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux)==3:
        oidObjeto = aux[1]
        oidInstancia = aux[2]
        varBinds = snmp_get(ip, community, mib, oidObjeto, int(oidInstancia))
        if varBinds != None:
            for varBind in varBinds:
                    bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))
        else:
            bot.send_message(cid, "Error en parámetro del comando")
    else:
        bot.send_message(cid,"Error de formato")

@bot.message_handler(commands=['set'])
def command_set(m):

    
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux)==4:
        oidObjeto = aux[1]
        oidInstancia = aux[2]
        value = aux[3]
        varBinds = snmp_set(ip, community, mib, oidObjeto, int(oidInstancia), value)
        if varBinds != None:
            for varBind in varBinds:
                    bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))
        else:
            bot.send_message(cid, "Error en parámetro del comando")
    else:
        bot.send_message(cid,"Error de formato")


@bot.message_handler(commands=['getnext'])
def command_getnext(m):

    
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux)==2:
        oidObjeto = aux[1]
        varBinds = snmp_getNext(ip, community, mib, oidObjeto)
        if varBinds != None:
            for varBind in varBinds:
                    bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))
        else:
            bot.send_message(cid, "Error en parámetro del comando")
    else:
        bot.send_message(cid,"Error de formato")

@bot.message_handler(commands=['getbulk'])
def command_getbulk(m):

    
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux)==4:
        nonRepeaters = aux[1]
        maxRepetitions = aux[2]
        introducidos = aux[3]
        varBinds = snmp_getbulk(ip, community, mib, int(nonRepeaters), int(maxRepetitions), int(introducidos))
        if varBinds != None:
            for varBind in varBinds:
                    bot.send_message(cid,' = '.join([x.prettyPrint() for x in varBind]))
        else:
            bot.send_message(cid, "Error en parámetro del comando")
    else:
        bot.send_message(cid,"Error de formato")

@bot.message_handler(commands=['receptortraps'])
def command_receptortraps(m):
    file = open("trap.txt","w")
    file.write(str(m.chat.id))
    file.close
    print "Cambiado receptor de traps"



@bot.message_handler(commands=['createvent'])
def command_createvent(m):

    
    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux)==6:
        eventDescription = aux[1]
        eventType = aux[2]
        eventCommunity = aux[3]
        eventOwner = aux[4]
        eventIndex = aux[5]
        varBinds = snmp_crear_evento(ip, community, eventDescription, eventType, eventCommunity, eventOwner, eventIndex)
        if varBinds != None:
           bot.send_message(cid, "Evento creado con éxito")
           print "Evento creado"
        else:
            bot.send_message(cid, "Error en parámetro del comando")
    else:
        bot.send_message(cid,"Error de formato")

@bot.message_handler(commands=['createalarm'])
def command_createalarm(m):

    cid = m.chat.id
    aux = m.text.split(" ")
    if len(aux)==9:
        indiceAlarma = aux[1]
        indiceEvento = aux[2]
        owner = aux[3]
        interval = aux[4]
        variable = aux[5]
        sampleType = aux[6]
        risingthr = aux[7]
        fallingth = aux[8]
        varBinds = snmp_crear_alarma(ip, community, indiceAlarma, indiceEvento, owner, interval, variable, sampleType, risingthr, fallingth)
        if varBinds != None:
            bot.send_message(cid, "Alarma creada con éxito")
            print "Alarma creada"
        else:
            bot.send_message(cid, "Error en parámetro del comando")
    else:
        bot.send_message(cid,"Error de formato")

@bot.message_handler(commands=['showconf'])
def command_showconf(m):
    
   
    cid = m.chat.id
    bot.send_message(cid,"IP: " +ip)
    bot.send_message(cid,"Comunidad: " + community)
    bot.send_message(cid, "MIB: " + mib)


@bot.message_handler(commands=['ayuda'])
def command_ayuda(m):
	
	cid = m.chat.id
	bot.send_message(cid,AYUDA)

@bot.message_handler(commands=['comandos'])
def command_comandos(m):

	cid = m.chat.id
	bot.send_message(cid,COMANDOS)

@bot.message_handler(commands=['start'])
def start(m):

	cid = m.chat.id
	bot.send_message(cid, BIENVENIDA)

bot.polling()