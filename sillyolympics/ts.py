"""
Training Systems
"""

#from . import TS,Zone

#from  import TS, Zone
from sillyolympics.sillyolympics import *


CTS = TS("CTS: Carmichael Training Systems")

Tempo = Zone("Tempo: T")
Tempo.setHR(88,90,"CTSTHR")
Tempo.setRPM(70,75)
Tempo.setRPE(7)
CTS.addZone(Tempo)

EM = Zone("Endurance Miles: EM")
EM.setHR(50,91,"CTSTHR")
EM.setRPM(85,95)
EM.setRPE(5)
CTS.addZone(EM)

FP = Zone("FastPedal: FP")
FP.setRPM(108,120)
FP.setRPE(7)
CTS.addZone(FP)

SS = Zone("Steady State: SS")
SS.setRPM(108,120)
SS.setHR(92,94,"CTSTHR")
SS.setRPE(7)
CTS.addZone(SS)

CR = Zone("Climbing Repeat: CR")
CR.setRPM(70,85)
CR.setHR(95,97,"CTSTHR")
CR.setRPE(8)
CTS.addZone(CR)

PI = Zone("Power Intervals: PI")
PI.setRPM(100,200)
PI.setHR(100,150,"CTSTHR")
PI.setRPE(10)
CTS.addZone(PI)

# How to Train Using Heart Rate Zones
REI = TS("REI")

Z1 = Zone("Zone1: recovery/easy")
REI.addZone(Z1)
Z2 = Zone("Zone2: aerobic/base")
REI.addZone(Z2)
Z3 = Zone("Zone3: tempo")
REI.addZone(Z3)
Z4 = Zone("Zone4: lactate threshold")
REI.addZone(Z4)
Z5 = Zone("Zone5: anaerobic")
REI.addZone(Z5)

# Polar
POLAR = TS("POLAR")

Z1 = Zone("Zone1: Very light") 
Z1.setHR(50,60,"a")
POLAR.addZone(Z1)
Z2 = Zone("Zone2: Light")
Z2.setHR(60,70,"a")
POLAR.addZone(Z2)
Z3 = Zone("Zone3: Moderate") 
Z3.setHR(70,80,"a")
POLAR.addZone(Z3)
Z4 = Zone("Zone4: Hard") 
Z4.setHR(80,90,"a")
POLAR.addZone(Z4)
Z5 = Zone("Zone5: Maximum") 
Z5.setHR(90,100,"a")
POLAR.addZone(Z5)

# Three zone system
TZS = TS("Three Zone System")

Z1 = Zone("Zone1: Easy") 
Z1.setHR(50,60,"a")
TZS.addZone(Z1)
Z2 = Zone("Zone2: Threshold")
Z2.setHR(60,70,"a")
TZS.addZone(Z2)
Z3 = Zone("Zone3: Over Threshold") 
Z3.setHR(70,80,"a")
TZS.addZone(Z3)

# Karvonen
Karvonen = TS("Karvonen, Five Zone System")

Z1 = Zone("Zone 1")
Z1.setHR(50,60,"a")
Karvonen.addZone(Z1)
Z2 = Zone("Zone 2")
Z1.setHR(60,70,"a")
Karvonen.addZone(Z2)
Z3 = Zone("Zone 3")
Z1.setHR(70,80,"a")
Karvonen.addZone(Z3)
Z4 = Zone("Zone 4")
Z1.setHR(80,90,"a")
Karvonen.addZone(Z4)
Z5 = Zone("Zone 5")
Z1.setHR(90,100,"a")
Karvonen.addZone(Z5)




