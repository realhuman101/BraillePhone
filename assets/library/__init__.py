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

		A full string would contain multiple lists within itself, each list being a character and containing 6 Booleans.
		
		I.e:
		[True, False, False, True, True, False] forms the letter O
		"""

		characterList = {
			'a': [True, False, False, False, False, False],
			'b': [True, False, True, False, False, False],
			'c': [True, True, False, False, False, False],
			'd': [True, True, False, True, False, False]
		}

	def get_pwm(self, angle):
		return (angle/18.0) + 2.5


	def output(self, text: str, waitTime: int = 30, singleDegree: float = 45.00) -> None:
		"""
		Outputs the text (will auto-convert to braille) to the pins
		"""

		braille = self.text2braille(text)
		brailleSep = []

		for character in braille:
			brailleSep.append([(character[0], character[1]), (character[2], character[3]), (character[4], character[5])])

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

			for character in brailleSep:
				top = character[0]
				middle = character[1]
				bottom = character[2]

				# Setting top pins
				if top[0] and top[1]:
					TopPin.ChangeDutyCycle(self.get_pwm(0))
				elif top[0] and not top[1]:
					TopPin.ChangeDutyCycle(self.get_pwm(-singleDegree))
				elif not top[0] and top[1]:
					TopPin.ChangeDutyCycle(self.get_pwm(singleDegree))
				
				# Setting middle pins
				if middle[0] and middle[1]:
					MiddlePin.ChangeDutyCycle(self.get_pwm(0))
				elif middle[0] and not middle[1]:
					MiddlePin.ChangeDutyCycle(self.get_pwm(-singleDegree))
				elif not middle[0] and middle[1]:
					MiddlePin.ChangeDutyCycle(self.get_pwm(singleDegree))

				# Setting bottom pins
				if bottom[0] and bottom[1]:
					BottomPin.ChangeDutyCycle(self.get_pwm(0))
				elif bottom[0] and not bottom[1]:
					BottomPin.ChangeDutyCycle(self.get_pwm(-singleDegree))
				elif not bottom[0] and bottom[1]:
					BottomPin.ChangeDutyCycle(self.get_pwm(singleDegree))
				
				time.sleep(waitTime)
			
			# End connection
			TopPin.stop()
			MiddlePin.stop()
			BottomPin.stop()

			GPIO.cleanup()
