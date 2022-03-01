class Vehicle:
	def __init__(self,regno,color,vehicleType):
		self.color =  color
		self.regno = regno
		self.vehicleType = vehicleType

class Car(Vehicle):

	def __init__(self,regno,color,vehicleType):
		Vehicle.__init__(self,regno,color,vehicleType)

	def getType(self):
		return "Car"


class Bike(Vehicle):

	def __init__(self,regno,color,vehicleType):
		Vehicle.__init__(self,regno,color,vehicleType)

	def getType(self):
		return "Bike"


class Truck(Vehicle):
	def __init__(self,regno,color,vehicleType):
		Vehicle.__init__(self,regno,color,vehicleType)

	def getType(self):
		return "Truck"
