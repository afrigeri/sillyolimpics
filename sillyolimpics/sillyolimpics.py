
import os, ConfigParser

Config = ConfigParser.ConfigParser()

for loc in os.curdir, os.path.expanduser("~/sillyolimpics/"), "/etc/myproject/" :
    conf = os.path.join(loc,"sillyolimpics.conf")
    try: 
	    Config.read(conf)
    except IOError:
            pass


class CTS:
	def __init__(self,athlete):
		self.CTSTHR = athlete.CTSTHR
		
	def Tempo(self):
		name = ('Tempo','T')
		rpm = (70,75)
		hr = (self.CTSTHR*.88,self.CTSHR*.90)
		RPE = 7





