
class Control:
	def __init__(self):
		self.tv = None

	def turnOn(self):
		self.tv.estado = True
	def turnOff(self):
		self.tv.estado = False

	def canalUp(self):
		if self.tv.estado == True:
			if self.tv.canal > 0 and self.tv.canal < 120:
				self.tv.canal = self.tv.canal +1
	def canalDown(self):
		if self.tv.estado == True:
			if self.tv.canal > 1 and self.tv.canal < 121:
				self.tv.canal = self.tv.canal -1
	def volumenUp(self):
		if self.tv.estado == True:
			if self.tv.volumen > -1 and self.tv.volumen < 7:
				self.tv.volumen = self.tv.volumen + 1
	def volumenDown(self):
		if self.tv.estado == True:
			if self.tv.volumen > 1 and self.tv.volumen < 8:
				self.tv.volumen = self.tv.volumen -1

	def enlazar(self,televisor):
		self.tv = televisor
		self.tv.control = self

	def setTv(self,televisor):
		self.tv = televisor
	def getTv(self):
		return self.tv 
	def setCanal(self,canal):
		if self.tv.estado == True:
			if canal >0 and canal < 121:
				self.tv.canal = canal





		







