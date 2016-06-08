# -*- coding: utf-8 -*-

import telebot # Library fot the bot API.
from telebot import types # Types for the bot API.
import dmusicbot as dmb # Library with the posible bot actions.
from keyboards import EmotionsKeyboard as ek # Library with markup keyboard for emotions
from ratemanager import Ratemanager
import time # Library for avoid the bot end.
import os # Library for get the environment variables.
 
TOKEN = os.environ['DMUSICBOT'] # Our bot token (the one given to us by @BotFather)
 
bot = telebot.TeleBot(TOKEN) # Create our bot object

emotions_markup = ek.get_keyboard() # Unique instance for emotions keyboard

rate_mng = Ratemanager().get_manager() # get a rate manager

rate_queue = {} # user waiting for rating

@bot.message_handler(commands=['search'])
def search(message):
	track = message.text[8:] # remove /search word from the string
	url = dmb.search(track)
	bot.send_message(message.chat.id, url) # Send the user the youtube url
	ask_rate(message)

@bot.message_handler(commands=['download'])
def download(message):
	track = message.text[10:] # remove /download word from the string
	url = dmb.download(track)
	bot.send_message(message.chat.id, url) # Send the user the download url
	ask_rate(message)

@bot.message_handler(commands=['usearch'])
def usearch(message):
	track = message.text[9:] # remove /usearch word from the string
	url = dmb.usearch(track)
	bot.send_message(message.chat.id, url) # Send the user the youtube url
	ask_rate(message)

@bot.message_handler(commands=['udownload'])
def udownload(message):
	track = message.text[11:] # remove /udownload word from the string
	url = dmb.udownload(track)
	bot.send_message(message.chat.id, url) # Send the user the download url
	ask_rate(message)

@bot.message_handler(commands=['help','start'])
def help(message):
	content = dmb.help()
	bot.send_message(message.chat.id, content) # Send the user the bot's help

def ask_rate(message):
	"""
		ask_rate: ask the users how the songs have make them feel, and display
			the EmotionalKeyboard for answering.
	"""
	bot.send_message(message.chat.id, "How did the song make you feel?",
		reply_markup=emotions_markup)
	rate_queue[message.chat.id] = 1 # Set user as pending for rating

@bot.message_handler(func=lambda message: message.chat.id in rate_queue.keys() 
	and rate_queue[message.chat.id] == 1)
def read_rate(message):
	"""
		read_rate: check that the user is using the EmotionalKeyboard for rating
			and perform the appropiate action to that emotion.
			Then hide the EmotionalKeyboard.
	"""
	response = message.text.encode('utf8')
	if response in rate_mng.keys():
		rate_mng[response]() # call the model handler
		hide_markup = types.ReplyKeyboardHide(selective=False) # hide markup 
		bot.send_message(message.chat.id, "Thanks, for rate!!!", 
			reply_markup=hide_markup)
		rate_queue[message.chat.id] = 0 # Set user as NOT pending for rating
	else:
		bot.send_message(message.chat.id, "Please use the provide buttons")
 
def listener(messages): # For debug
    for m in messages: 
        if m.content_type == 'text': # Filter text messages
            cid = m.chat.id # Store chat id
            print "[" + str(cid) + "]: " + m.text 
 
bot.set_update_listener(listener) # Use function "listener" declared above as listener.

bot.polling(none_stop=True) # The bot will continue working even with errors.
