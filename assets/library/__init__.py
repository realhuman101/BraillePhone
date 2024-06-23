class Controller:
	def __init__(self, simulated: bool = False) -> None:
		"""
		simulated = If the code is being run on the raspberry pi, otherwise it'll just output raw text
		"""

		self.simulated = simulated

		if simulated:
			import RPi.GPIO as GPIO # Import (otherwise will fail) only if on raspberry pi

	def text2braille(self, text: str) -> list[bool]:
		"""
		Converts string to a 2D list with each nested element containing 6 elements, each corresponding to a pin

		The pins will be in the format where the dots correspond to the 1-2-3-4-5-6 pattern, with 1 and 2 being the top 2 from left to right, 3 and 4 being the middle two from left to right, etc. 
		
		I.e:
		[[True, False, False, True, True, False]] forms the letter O
		"""

	def output(self, text: str) -> None:
		"""
		Outputs the text (will auto-convert to braille) to the pins
		"""