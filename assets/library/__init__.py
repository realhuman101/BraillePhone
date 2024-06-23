import time

class Controller:
	def __init__(self, simulated: bool = False) -> None:
		"""
		simulated = If the code is being run on the raspberry pi, otherwise it'll just output raw text
		"""

		self.simulated = simulated

	def text2braille(self, text: str) -> list[list[bool]]:
		"""
		Converts string to a 2D list with each nested element containing 6 elements, each corresponding to a pin

		The pins will be in the format where the dots correspond to the 1-2-3-4-5-6 pattern, with 1 and 2 being the top 2 from left to right, 3 and 4 being the middle two from left to right, etc. 
		
		I.e:
		[True, False, False, True, True, False] forms the letter O
		"""

	def ConvertRadsInPulseWidth(self, angle):
		"""
		thanks to https://raspberrypi.stackexchange.com/a/112989
		"""
		everyRadianInPulseWidth = 439.267642
		rounded = "{:.10f}".format(float(angle))
		pulseWithFromRadians = (everyRadianInPulseWidth * float(rounded))

		moveFromCentre = 1435 + pulseWithFromRadians

		return moveFromCentre

	def output(self, text: str) -> None:
		"""
		Outputs the text (will auto-convert to braille) to the pins
		"""

		braille = self.text2braille(text)

		if not self.simulated:
			import RPi.GPIO as GPIO

			GPIO.setmode(GPIO.BOARD)

			# Pins 11, 13 and 15 will be used to control the servos. 11 will be the top servo, 15 will be the bottom.

			GPIO.setup(11, GPIO.OUT)
			GPIO.setup(13, GPIO.OUT)
			GPIO.setup(15, GPIO.OUT)

			# Set up pins
			TopPin = GPIO.PWM(11, GPIO.OUT) # Top servo
			MiddlePin = GPIO.PWM(13, GPIO.OUT) # Middle
			BottomPin = GPIO.PWM(15, GPIO.OUT) # Bottom

			TopPin.start(0)
			MiddlePin.start(0)
			BottomPin.start(0)

