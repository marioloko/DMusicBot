from keyboards import EmotionsKeyboard as ek

class Ratemanager:

	def __init__(self):
		self.emotions = {
			ek.HAPPYSTR: self.happy,
			ek.SADSTR: self.sad,
			ek.ANGERSTR: self.anger,
			ek.FEARSTR: self.fear,
			ek.SURPRISESTR: self.surprise,
			ek.DISGUSTSTR: self.disgust,
			ek.NONESTR: self.none
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
