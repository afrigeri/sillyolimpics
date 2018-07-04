"""
Training Systems
"""

from sillyolympics import TS,Zone


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


MCM = TS("McMillan Running")

RJ = Zone("Recovery Jog")
RJ.setHR(60,70,"MAXHR")
RJ.setRPE(2)
MCM.addZone(RJ)

LR = Zone("Long Run")
LR.setHR(60,85,"MAXHR")
LR.setRPE(2)
MCM.addZone(LR)

ER = Zone("Easy Run")
ER.setHR(60,85,"MAXHR")
ER.setRPE(2)
MCM.addZone(ER)

SS = Zone("Steady State Run")
SS.setHR(83,87,"MAXHR")
SS.setRPE(3)
MCM.addZone(SS)

TR = Zone("Tempo Run")
TR.setHR(85,90,"MAXHR")
TR.setRPE(4)
MCM.addZone(TR)

TI = Zone("Tempo Interval")
TI.setHR(87,92,"MAXHR")
TI.setRPE(4)
MCM.addZone(TI)



