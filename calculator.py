#generally prefer class over static methods
#CLS represents whole class, allows it to see methods
#Why would you do a static method? adds context, we know its related to the class


class Calculator(object):
	def __init__(self):
		pass

	@staticmethod
	def add(num1, num2):
		return num1 + num2

	@classmethod
	def subtract(cls, num1, num2):
		return cls.add(num1, num2 * -1)

print(Calculator.add(1,2))