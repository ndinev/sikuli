from sikuli import *
import unittest
import iHTMLTestRunner.iHTMLTestRunner as HTMLTestRunner
from _uimap import *

class Calc:
	@classmethod
	def Start(self):
		type('r', KeyModifier.WIN)
		sleep(2)
		type('calc')
		sleep(2)
		type(Key.ENTER)
		sleep(1)
	
	@classmethod
	def Close(self):
		type(Key.F4, KeyModifier.ALT)

