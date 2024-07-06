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
			'd': [True, True, False, True, False, False],
			'e': [True, False, False, True, False, False],
			'f': [True, True, True, False, False, False],
			'g': [True, True, True, True, False, False],
			'h': [True, False, True, True, False, False],
			'i': [False, True, True, False, False, False],
			'j': [False, True, True, True, False, False],
			'k': [True, False, False, False, True, False],
			'l': [True, False, True, False, True, False],
			'm': [True, True, False, False, True, False],
			'n': [True, True, False, True, True, False],
			'o': [True, False, False, True, True, False],
			'p': [True, True, True, False, True, False],
			'q': [True, True, True, True, True, False],
			'r': [True, False, True, True, True, False],
			's': [False, True, True, False, True, False],
			't': [False, True, True, True, True, False],
			'u': [True, False, False, False, True, True],
			'v': [True, False, True, False, True, True],
			'w': [False, True, True, True, False, True],
			'x': [True, True, False, False, True, True],
			'y': [True, True, False, True, True, True],
			'z': [True, False, False, True, True, True],
			'1': [True, False, False, False, False, False],
			'2': [True, False, True, False, False, False],
			'3': [True, True, False, False, False, False],
			'4': [True, True, False, True, False, False],
			'5': [True, False, False, True, False, False],
			'6': [True, True, True, False, False, False],
			'7': [True, True, True, True, False, False],
			'8': [True, False, True, True, False, False],
			'9': [False, True, True, False, False, False],
			'0': [False, True, True, True, False, False]
		}

	def get_pwm(self, angle):
		return (angle/18.0) + 2.5


	def output(self, text: str, waitTime: int = 0.5) -> None:
		"""
		Outputs the text (will auto-convert to braille) to the pins
		"""

		braille = self.text2braille(text)
		brailleSep = []

		for character in braille:
			brailleSep.append([(character[0], character[1]), (character[2], character[3]), (character[4], character[5])])

		if not self.simulated:
			from RPi import GPIO


