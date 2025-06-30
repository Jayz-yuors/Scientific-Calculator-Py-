import math
class TrigonometricFunction:
	def sine(self, angle, unit):
		if unit == 'DEGREE':
			angle = math.radians(angle)
		elif unit != 'RADIAN':
			print("Error: Unit must be either 'degrees' or 'radians'.")
			return None
		return math.sin(angle)
	def cosine(self, angle,unit):
		if unit == 'DEGREE':
			angle = math.radians(angle)
		elif unit != 'RADIAN':
			print("Error: Unit must be either 'degrees' or 'radians'.")
			return None
		return math.cos(angle)
	def tangent(self, angle,unit):
		if unit == 'DEGREE':
			angle = math.radians(angle)
		elif unit != 'RADIAN':
			print("Error: Unit must be either 'degrees' or 'radians'.")
			return None
		return math.tan(angle)
	def cosecant(self, angle,unit):
		if unit == 'DEGREE':
			angle = math.radians(angle)
		elif unit != 'RADIAN':
			print("Error: Unit must be either 'degrees' or 'radians'.")
			return None
		if math.sin(angle) == 0:
			print("Error: Cosecant is undefined for angles where sine is zero.")
			return None
		return 1 / math.sin(angle)
	def secant(self, angle,unit):
		if unit == 'DEGREE':
			angle = math.radians(angle)
		elif unit != 'RADIAN':
			print("Error: Unit must be either 'degrees' or 'radians'.")
			return None
		if math.cos(angle) == 0:
			print("Error: Secant is undefined for angles where cosine is zero.")
			return None
		return 1 / math.cos(angle)
	def cotangent(self, angle,unit):
		if unit == 'DEGREE':
			angle = math.radians(angle)
		elif unit != 'RADIAN':
			print("Error: Unit must be either 'degrees' or 'radians'.")
			return None
		if math.tan(angle) == 0:
			print("Error: Cotangent is undefined for angles where sine is zero.")
			return None
		return 1 / math.tan(angle)
	def inverse_sine(self, value):
		if value < -1 or value > 1:
			print("Error: Value out of range for inverse sine.")
			return None
		return math.asin(value)
	def inverse_cosine(self, value):
		if value < -1 or value > 1:
			print("Error: Value out of range for inverse sine.")
			return None
		return math.acos(value)
	def inverse_tangent(self,value):
		return math.atan(value)
	def sineh(self,angle):
		return math.sinh(angle)
	def cosineh(self,angle):
		return math.cosh(angle)
	def tangenth(self,angle):
		return math.tanh(angle)
	def asinh(self, angle):
		if angle < 0:
			print("Error: Cannot calculate inverse hyperbolic sine of negative number.")
			return None
		return math.asinh(angle)
	def acosh(self, angle):
		if angle < 0:
			print("Error: Cannot calculate inverse hyperbolic sine of negative number.")
			return None
		return math.acosh(angle)
	def atanh(self,angle):
		if angle < -1 or angle > 1:
			print("Error: Value out of range for inverse hyperbolic tangent.")
			return None
		return math.atanh(angle)
        

		
		