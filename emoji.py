class Emoji:
	"""
		Emoji's unicode constant
	"""
	# Basic Emotions
	HAPPY = '\xf0\x9f\x98\x84'
	SAD = '\xf0\x9f\x98\xa2'
	ANGER = '\xf0\x9f\x98\xa1'
	FEAR = '\xf0\x9f\x98\xb1'
	SURPRISE = '\xf0\x9f\x98\xb3'
	DISGUST = '\xf0\x9f\x98\x96'

	# Simbologism
	CROSS = '\xe2\x9d\x8c'

class EmojiStr:
	"""
		Emoji's definition + Emoji's unicode
	"""
	e = Emoji # Shortcut to Emoji for readability
	HAPPYSTR = 'Happy' + e.HAPPY 
	SADSTR = 'Sad' + e.SAD
	ANGERSTR = 'Anger' + e.ANGER
	FEARSTR = 'Fear' + e.FEAR
	SURPRISESTR = 'Surprise' + e.SURPRISE
	DISGUSTSTR = 'Disgust' + e.DISGUST
	NONESTR = 'None' + e.CROSS
