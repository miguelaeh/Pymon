# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from pysnmp.hlapi import *

#Variables globales que necesitaremos utilizar para la gestion, se le asignaran valores por defecto

ip = "0.0.0.0"
community = "public"
mib = "RMON-MIB"

 
# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX 
 
TOKEN = '563209742:AAHsXl1ZoUIZDYCBTR52oxezfxHKdCoDb8E' # Nuestro token del bot.
 

GRUPO = -1001201542913 #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá
 
 
 
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
        bot.send_message("Error de formato")

@bot.message_handler(commands=['showconf'])
def command_showconf(m):
    
   
    cid = m.chat.id
    bot.send_message(cid,"IP: " +ip)
    bot.send_message(cid,"Comunidad: " + community)
    bot.send_message(cid, "MIB: " + mib)



bot.polling()