from datetime import date,datetime
import os, ConfigParser



def read_config(conf_file):
    config = ConfigParser.ConfigParser()
    conf = os.path.join(os.path.expanduser("~/.sillyolimpics/"), conf_file )
    config.read(conf)
    return config
    
    '''
    for loc in os.curdir, os.path.expanduser(".sillyolimpics/"), "/etc/myproject/":
        conf = os.path.join(loc,"sillyolimpics.conf")
        try:
            print "reading: ",conf
            Config.read(conf)
        except IOError:
            print "not a valid file ...."
            #pass
        print conf    
    '''    

class Athlete:
    """The Athlete class.

    you can define an athlete here.  If no argument is given, the Athlete is
    is define from the default configuration file.
    
    .. note::

       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class.

     Args:
        foo (str): We all know what foo does.
     Kwargs:
           bar (str): Really, same as foo.

        """

    def __init__(self,nickname='DEFAULT'):
        self.c = read_config('athletes.conf')
        secs = self.c.sections()
        for s in secs:
            if nickname == 'DEFAULT':
                s = secs[0]
                self._updateFromConfig(s)
            if s == nickname:   
                self._updateFromConfig(s)
    
    def _updateFromConfig(self,s):
        """ Update from the secton s"""
        self.setName(self,(self.c.get(s, 'name'),self.c.get(s, 'surname')))
        self.setCTSTHR(self.c.get(s, 'CTSTHR'))
        self.setMaxHR(self.c.get(s,'MaxHR'))
        self.setAge(self.c.get(s, 'Birthday'))
            
    def setName(self,name,surname):
        self.name = name
        self.surname = surname
        
    def setAge(self,birthday):        
        born = datetime.strptime( birthday , "%Y/%m/%d" )
        today = date.today()
        self.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
    def setCTSTHR(self,CTSTHR):
        self.ctsthr = int(CTSTHR)
        
    def setJFLT(self,JFLTHR):
        self.setJFLTHR = JFLTHR

    def setMaxHR(self,MaxHR):
	self.maxhr = int(MaxHR)
        
    def __repr__(self):
        return self.name,self.surname,self.age
        
    def __str__(self):
        return "%d"%self.age
           
	
class Zone:
    def __init__(self,name):
        self.name = name
        self.minhr_p = None
        self.maxhr_p = None
       
    def setHR(self,minhr_p,maxhr_p,ref):
           #if ref == 'CTSTHR':
           #       hr_ref = athlete.ctsthr
		self.minhr_p = minhr_p  
		self.maxhr_p = maxhr_p
    def setRPM(self,minrpm,maxrpm):
		self.minrpm = minrpm
		self.maxrpm = maxrpm   
    def setRPE(self,rpe):
           self.rpe = rpe
    def getRPE(self):
         print self.rpe
    def __str__(self):           
           msg = "%s\n  Hearth rate: %d-%d \n  Cadence: %d-%d\n  RPE: %d" %(self.name,self.minhr,self.maxhr,self.minrpm,self.maxrpm,self.rpe)
           return msg
                     

class TS:
    """Training System Class
        
    """
    def __init__(self,name):
		self.name = name
		self.zones = []
  
    def setAthlete(self,athlete,hr_ref):
            self.athlete = athlete
            self._updateHR(hr_ref)
  
    def _updateHR(self,hr_ref):         
        for z in self.zones:            
                if not z.minhr_p: z.minhr_p = 0
                z.minhr = int(round(z.minhr_p / 100.0 * hr_ref))
                if not z.maxhr_p: z.maxhr_p = 0
                z.maxhr = int(round(z.maxhr_p / 100.0 * hr_ref))
  
    def addZone(self,zone):
		self.zones.append(zone)
  
    def listZones(self):
        for z in self.zones: 
            print z






