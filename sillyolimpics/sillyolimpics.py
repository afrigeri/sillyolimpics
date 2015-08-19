
import os, ConfigParser

Config = ConfigParser.ConfigParser()

def read_config():

	for loc in os.curdir, os.path.expanduser("~/sillyolimpics/"), "/etc/myproject/" :
    		conf = os.path.join(loc,"sillyolimpics.conf")
    	try: 
	    	Config.read(conf)
    	except IOError:
            	pass

class Athlete:
	def __init__(self):
		read_config()
		Config.add_section('athlete')
		Config.set('athlete', 'an_int', '15')
		print Config.get('athlete', 'Name')
		
	


class CTS:
	def __init__(self,athlete):
		self.CTSTHR = athlete.CTSTHR
		
	def Tempo(self):
		name = ('Tempo','T')
		rpm = (70,75)
		hr = (self.CTSTHR*.88,self.CTSHR*.90)
		RPE = 7





