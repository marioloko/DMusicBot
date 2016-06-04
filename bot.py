# -*- coding: utf-8 -*-

import telebot # Library fot the bot API.
import dmusicbot as dmb # Library with the posible bot actions.
from telebot import types # Types for the bot API.
import time # Library for avoid the bot end.
import os # Library for get the environment variables.
 
TOKEN = os.environ['DMUSICBOT'] # Our bot token (the one given to us by @BotFather)
 
bot = telebot.TeleBot(TOKEN) # Create our bot object

@bot.message_handler(commands=['search'])
def search(message):
	track = message.text[8:] # remove /search word from the string
	url = dmb.search(track)
	bot.send_message(message.chat.id, url) # Send the user the youtube url

@bot.message_handler(commands=['download'])
def download(message):
	track = message.text[10:] # remove /download word from the string
	url = dmb.download(track)
	bot.send_message(message.chat.id, url) # Send the user the download url

@bot.message_handler(commands=['usearch'])
def usearch(message):
	track = message.text[9:] # remove /usearch word from the string
	url = dmb.usearch(track)
	bot.send_message(message.chat.id, url) # Send the user the youtube url

@bot.message_handler(commands=['udownload'])
def udownload(message):
	track = message.text[11:] # remove /udownload word from the string
	url = dmb.udownload(track)
	bot.send_message(message.chat.id, url) # Send the user the download url
 
def listener(messages): # For debug
    for m in messages: 
        if m.content_type == 'text': # Filter text messages
            cid = m.chat.id # Store chat id
            print "[" + str(cid) + "]: " + m.text 
 
bot.set_update_listener(listener) # Use function "listener" declared above as listener.

bot.polling(none_stop=True) # The bot will continue working even with errors.
