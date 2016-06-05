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
		# Define keyboard buttons
		happybtn = types.KeyboardButton(EmotionsKeyboard.HAPPYSTR)
		sadbtn = types.KeyboardButton(EmotionsKeyboard.SADSTR)
		angerbtn = types.KeyboardButton(EmotionsKeyboard.ANGERSTR)
		fearbtn = types.KeyboardButton(EmotionsKeyboard.FEARSTR)
		surprbtn = types.KeyboardButton(EmotionsKeyboard.SURPRISESTR)
		disgbtn = types.KeyboardButton(EmotionsKeyboard.DISGUSTSTR)
		nonebtn = types.KeyboardButton(EmotionsKeyboard.NONESTR)

		# Add buttons to the keyboard
		markup = types.ReplyKeyboardMarkup()
		markup.row(happybtn, sadbtn)
		markup.row(angerbtn, fearbtn)
		markup.row(surprbtn, disgbtn)
		markup.row(nonebtn)
		return markup
