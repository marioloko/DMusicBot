# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
 
TOKEN = '219104614:AAE7MO4Eojv11jgRBDH6DjDo1_LH8wb31LQ' # Nuestro tokken del bot (el que @BotFather nos dió).
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
 
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
