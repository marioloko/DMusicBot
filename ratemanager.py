from emoji import EmojiStr as es

class Ratemanager:

	def __init__(self):
		self.emotions = {
			es.HAPPYSTR: self.happy,
			es.SADSTR: self.sad,
			es.ANGERSTR: self.anger,
			es.FEARSTR: self.fear,
			es.SURPRISESTR: self.surprise,
			es.DISGUSTSTR: self.disgust,
			es.NONESTR: self.none
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
