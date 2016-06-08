from telebot import types # Types for the bot API.
from emoji import EmojiStr as es # Library with emoji codification

class EmotionsKeyboard:
	"""
		EmotionsKeyboard: keyboard markup which contains the basis emotions
	"""
	# String stored in buttons

	@staticmethod
	def get_keyboard():
		"""
			get_keyboard: return the emotions keyboard
		"""
		# Define keyboard buttons
		happybtn = types.KeyboardButton(es.HAPPYSTR)
		sadbtn = types.KeyboardButton(es.SADSTR)
		angerbtn = types.KeyboardButton(es.ANGERSTR)
		fearbtn = types.KeyboardButton(es.FEARSTR)
		surprbtn = types.KeyboardButton(es.SURPRISESTR)
		disgbtn = types.KeyboardButton(es.DISGUSTSTR)
		nonebtn = types.KeyboardButton(es.NONESTR)

		# Add buttons to the keyboard
		markup = types.ReplyKeyboardMarkup()
		markup.row(happybtn, sadbtn)
		markup.row(angerbtn, fearbtn)
		markup.row(surprbtn, disgbtn)
		markup.row(nonebtn)
		return markup
