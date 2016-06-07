from telebot import types # Types for the bot API.
import emoji as emo # Library with emoji codification

class EmotionsKeyboard:
	"""
		EmotionsKeyboard: keyboard markup which contains the basis emotions
	"""
	# String stored in buttons
	HAPPYSTR = 'Happy' + emo.HAPPY 
	SADSTR = 'Sad' + emo.SAD
	ANGERSTR = 'Anger' + emo.ANGER
	FEARSTR = 'Fear' + emo.FEAR
	SURPRISESTR = 'Surprise' + emo.SURPRISE
	DISGUSTSTR = 'Disgust' + emo.DISGUST
	NONESTR = 'None' + emo.CROSS

	@staticmethod
	def get_keyboard():
		"""
			get_keyboard: return the emotions keyboard
		"""
		# Alias the class name for readability
		ek = EmotionsKeyboard
		
		# Define keyboard buttons
		happybtn = types.KeyboardButton(ek.HAPPYSTR)
		sadbtn = types.KeyboardButton(ek.SADSTR)
		angerbtn = types.KeyboardButton(ek.ANGERSTR)
		fearbtn = types.KeyboardButton(ek.FEARSTR)
		surprbtn = types.KeyboardButton(ek.SURPRISESTR)
		disgbtn = types.KeyboardButton(ek.DISGUSTSTR)
		nonebtn = types.KeyboardButton(ek.NONESTR)

		# Add buttons to the keyboard
		markup = types.ReplyKeyboardMarkup()
		markup.row(happybtn, sadbtn)
		markup.row(angerbtn, fearbtn)
		markup.row(surprbtn, disgbtn)
		markup.row(nonebtn)
		return markup
