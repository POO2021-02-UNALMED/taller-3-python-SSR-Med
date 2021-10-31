
class TV:
	numTV = 0
	def __init__(self,marca,estado):
		self.marca = marca
		self.estado = estado
		self.canal = 1
		self.volumen = 1
		self.precio = 500
		TV.numTV = TV.numTV + 1
	def setMarca(self,marca):
		self.marca = marca 
	def setControl(self,control):
		self.control = control 
		


	def setPrecio(self,precio):
		self.precio = precio 
	def getPrecio(self):
		return self.precio

	def setVolumen(self,volumen):
		if self.estado == True:
			if volumen > -1 and volumen < 8:
				self.volumen = volumen
	def setCanal(self,canal1):
		if self.estado == True:
			if canal1 >0 and canal1 < 121:
				self.canal = canal1




	def getMarca(self):
		return self.marca
	def getControl(self):
		return self.control 





	def getVolumen(self):
		if self.estado == True:
			return self.volumen
	def getCanal(self):
		return self.canal 





	@classmethod
	def getNumTV(cls):
		return cls.numTV
	@classmethod
	def setNumTV(cls,numero):
		cls.numTV = numero

	def turnOn(self):
		self.estado = True
	def turnOff(self):
		self.estado = False

	def getEstado(self):
		return self.estado 



	def canalUp(self):
		if self.estado == True:
			if self.canal > 0 and self.canal < 120:
				self.canal = self.canal + 1
	def canalDown(self):
		if self.estado == True:
			if self.canal > 1 and self.canal < 121:
				self.canal = self.canal - 1


	def volumenUp(self):
		if self.estado == True:
			if self.volumen > -1 and self.volumen < 7:
				self.volumen = self.volumen + 1
	def volumenDown(self):
		if self.estado == True:
			if self.volumen > 1 and self.volumen < 8:
				self.volumen = self.volumen - 1























