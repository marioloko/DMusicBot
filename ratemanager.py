from keyboards import EmotionsKeyboard
class Ratemanager:

	def __init__(self):
		self.emotions = {
			EmotionsKeyboard.HAPPYSTR: self.happy,
			EmotionsKeyboard.SADSTR: self.sad,
			EmotionsKeyboard.ANGERSTR: self.anger,
			EmotionsKeyboard.FEARSTR: self.fear,
			EmotionsKeyboard.SURPRISESTR: self.surprise,
			EmotionsKeyboard.DISGUSTSTR: self.disgust,
			EmotionsKeyboard.NONESTR: self.none
		}
	
	def get_manager(self):
		return self.emotions

	def happy(self):
		print 'HAPPY'

	def sad(self):
		print 'SAD'

	def anger(self):
		print 'ANGER'

	def fear(self):
		print 'FEAR'

	def surprise(self):
		print 'SURPRISE'

	def disgust(self):
		print 'DISGUST'

	def none(self):
		print 'NONE'
